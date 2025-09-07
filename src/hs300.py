# filepath: hs300-indicator/src/hs300.py
import csv
import os
from datetime import datetime
from utils.wind_query import get_a_stock_rate, get_10_year_treasury_rate, get_hs300_dividend_yield

def calculate_indicators():
    # 计算A股利率
    a_stock_rate = get_a_stock_rate()
    # 获取10年国债利率
    risk_free_rate = get_10_year_treasury_rate()
    # 获取沪深300的股息率
    dividend_yield = get_hs300_dividend_yield()
    
    # 计算股债性价比和股债利差
    stock_bond_ratio = a_stock_rate / risk_free_rate
    stock_bond_spread = a_stock_rate - risk_free_rate
    
    return {
        "A股利率": a_stock_rate,
        "无风险利率": risk_free_rate,
        "股债性价比": stock_bond_ratio,
        "股债利差": stock_bond_spread,
        "股息率": dividend_yield
    }

def safety_margin_advice(indicators: dict) -> str:
    ratio = indicators["股债性价比"]
    spread = indicators["股债利差"]
    dividend_yield = indicators["股息率"]
    spread_pct = spread * 100

    warnings = []
    if dividend_yield < 2:
        warnings.append("⚠️ 沪深300股息率低于2，要小心了")
    if spread_pct < 3:
        warnings.append("⚠️ 股债利差小于3，非常小心")
    if ratio < 2:
        warnings.append("⚠️ 股债性价比小于2，可以远离股市了")

    # 买股条件：股债比>3；股债差>6；股息率>3  以上三个条件满足两项，则卖出手上的债，买入股。
    buy_stock_count = 0
    if ratio > 3:
        buy_stock_count += 1
    if spread_pct > 6:
        buy_stock_count += 1
    if dividend_yield > 3:
        buy_stock_count += 1

    # 633买，322卖
    # 买债条件：股债比<2；股债差<3；股息率>1.5  以上三个条件满足两项，则卖出手上的股，买入债。
    buy_bond_count = 0
    if ratio < 2:
        buy_bond_count += 1
    if spread_pct < 3:
        buy_bond_count += 1
    if dividend_yield > 1.5:
        buy_bond_count += 1

    if buy_stock_count >= 2:
        advice = "满足买股条件（至少两项），建议：卖债买股"
    elif buy_bond_count >= 2:
        advice = "满足买债条件（至少两项），建议：卖股买债"
    elif ratio > 3 and spread_pct > 6:
        advice = "建议：买股，卖债"
    elif ratio < 2 and spread_pct < 3:
        advice = "建议：买债，卖股"
    else:
        advice = "建议：买货基、短债"

    return "\n".join(warnings + [advice])

def save_indicators_to_csv(indicators: dict, advice: str, filename: str = "hs300_indicators.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='gbk') as f:
        writer = csv.writer(f)
        if not file_exists:
            # 写表头，增加“建议”列
            writer.writerow(["日期"] + list(indicators.keys()) + ["建议"])
        # 写数据
        today = datetime.today().strftime('%Y-%m-%d')
        writer.writerow([today] + [f"{v:.4f}" for v in indicators.values()] + [advice.replace('\n', ' ')])


if __name__ == "__main__":
    day_str = "20240725"
    print("计算沪深300相关指标...")
    print(f"市场先生:{day_str}")
    indicators = calculate_indicators()
    for key, value in indicators.items():
        print(f"{key}: {value:.4f}")
    advice = safety_margin_advice(indicators)
    print(advice)
    save_indicators_to_csv(indicators, advice)