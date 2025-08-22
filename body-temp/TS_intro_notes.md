

# 金融时间序列简介
- 金融资产回报率的计算
- 金融时间序列的特征：序列相关和异方差性
- 平稳和非平稳时间序列
- 协整特征

以上通过一些简单时序来说明

Financial time series analysis is concerned with the theory and practice of asset valuation over time. It is a highly empirical discipline, but like other scientific fields theory forms the foundation for making inference. There is, however, a key feature that distinguishes financial time series analysis from other time series analysis. Both financial theory and its empirical time series contain an element of uncertainty. For example, there are various definitions of asset volatility, and for a stock return series, the volatility is not directly observable. As a result of the added uncertainty, statistical theory and methods play an important role in financial time series analysis.




## 金融时间序列的特征


![](https://fred.stlouisfed.org/graph/fredgraph.png?g=1INmm&height=490)




<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1INmm&width=750&height=475" scrolling="no" frameborder="0" style="overflow:hidden; width:750px; height:425px;" allowTransparency="true" loading="lazy"></iframe>

> Source: U.S. Bureau of Labor Statistics, Unemployment Rate [UNRATE], retrieved from FRED, Federal Reserve Bank of St. Louis; <https://fred.stlouisfed.org/series/UNRATE>, May 5, 2025.   
> [-more data-](https://fred.stlouisfed.org/release/tables?rid=50&eid=463#snid=471)

---

### Gross Domestic Product (GDP)

![](https://fred.stlouisfed.org/graph/fredgraph.png?g=1IHdx&height=490)

<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1IHdx&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden; width:670px; height:525px;" allowTransparency="true" loading="lazy"></iframe>

> Source: U.S. Bureau of Economic Analysis, Gross Domestic Product [GDP], retrieved from FRED, Federal Reserve Bank of St. Louis; <https://fred.stlouisfed.org/series/GDP>, May 5, 2025.

---

### Consumer Price Index (CPI)

![](https://fred.stlouisfed.org/graph/fredgraph.png?g=1Inod&height=490)

<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1Inod&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden; width:670px; height:525px;" allowTransparency="true" loading="lazy"></iframe>

> Source: U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S. City Average [CPIAUCNS], retrieved from FRED, Federal Reserve Bank of St. Louis; <https://fred.stlouisfed.org/series/CPIAUCNS>, May 5, 2025.