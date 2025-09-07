# hs300-indicator

该项目旨在通过从Wind数据库获取数据，计算A股的相关财务指标，包括A股利率、无风险利率、股债性价比和股债利差。

## 文件结构

```
hs300-indicator
├── src
│   ├── hs300.py          # 实现计算逻辑的主文件
│   └── utils
│       └── wind_query.py # 与Wind数据库交互的工具文件
├── requirements.txt      # 项目所需的Python库和依赖项
└── README.md             # 项目的文档
```

## 功能

- **A股利率**：通过沪深300的市盈率计算得出。
- **无风险利率**：使用10年国债利率作为无风险利率。
- **股债性价比**：计算A股利率与无风险利率的比值。
- **股债利差**：计算A股利率与无风险利率的差值。

## 使用方法

1. 确保已安装Python环境。
2. 安装项目依赖项：
   ```
   pip install -r requirements.txt
   ```
3. 运行计算逻辑：
   ```
   python src/hs300.py
   ```

## 依赖项

请查看 `requirements.txt` 文件以获取项目所需的所有库和版本信息。