def get_hs300_pe_ratio():
    # 这里应该是与Wind数据库交互的代码
    # 返回沪深300的市盈率
    return 11.68  # 示例值，实际应从数据库获取

def calc_a_stock_rate(e_ratio):
    #计算A股利率
    return 100 * (1 / e_ratio)

def get_a_stock_rate():
    pe_ratio = get_hs300_pe_ratio()
    return calc_a_stock_rate(pe_ratio)

def get_10_year_treasury_rate():
    # 这里应该是与Wind数据库交互的代码
    # 返回10年国债利率
    return 2.22  # 示例值，实际应从数据库获取

def get_hs300_dividend_yield():
    # 这里应该是与Wind数据库交互的代码
    # 返回沪深300的股息率
    return 3.2894  # 示例值，实际应从数据库获取

def get_data():
    pe_ratio = get_hs300_pe_ratio()
    treasury_rate = get_10_year_treasury_rate()
    dividend_yield = get_hs300_dividend_yield()
    return pe_ratio, treasury_rate, dividend_yield