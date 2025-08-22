

folder: HousePrice_city_China

### 数据来源
- Soure: [国家统计局](https://data.stats.gov.cn/easyquery.htm?cn=E0105)
  - 首页 >> 地区数据 >> 主要城市年度数据
  - 财政和金融 >> 依次将如下三个指标对应的 EXcel 表格存储到本地
    - 地方一般公共预算收入: `city_income.xlsx`
    - 地方一般公共预算支出: `city_expenditure.xlsx`
    - 住户存款余额: `individual_deposit.xlsx`
  - 国民经济核算 >> 获取如下指标：
    - 地区生产总值（当年价格）(亿元): `gdp.xlsx`

  <img style="width: 550px" src="https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250520221111.png">

  - 将上述数据合并为一个数据框，包括变量：
    - city: 城市名称
    - year: 年度
    - income: 财政收入
    - expend: 财政支出
    - gdp: 地区生产总值

