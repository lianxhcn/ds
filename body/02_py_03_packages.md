## Python 常用扩展包

截至 2024 年 5 月 6 日，Python 社区已发布超过 **530,000** 个包（[来源](https://en.wikipedia.org/wiki/Python_Package_Index)），涵盖了从科学计算、数据分析到机器学习、Web 开发的几乎所有领域。用户可通过 [PyPI](https://pypi.org/) 进行查找和安装。

然而，对于经济、金融、管理、社会科学等领域的初学者来说，要在如此庞大的生态中快速识别出高效实用的工具包，并不容易。为此，本文梳理了这些领域中较为常用、应用成熟的 Python 扩展包，按功能分类整理，并附上官网或 GitHub 链接，便于进一步了解与使用。

## 数据处理与分析

这些库是处理结构化数据的核心工具，适用于经济建模、金融分析和社会学研究。

1.  **pandas** ([官网](https://pandas.pydata.org/))\
    数据分析的瑞士军刀，支持数据清洗、转换和统计分析。

2.  **NumPy** ([官网](https://numpy.org/))\
    高性能数值计算的基础库，支持多维数组和矩阵运算。

3.  **scipy** ([官网](https://scipy.org/))\
    构建在 NumPy 基础上的科学计算库，包含优化、积分、插值等模块。

4.  **Dask** ([官网](https://dask.org/))\
    并行计算库，支持超大数据集的处理，API 与 pandas 高度兼容。

5.  **Polars** ([GitHub](https://github.com/pola-rs/polars))\
    基于 Rust 的极速 DataFrame 库，适合高频金融数据处理。

6.  **cuDF** ([文档](https://docs.rapids.ai/api/cudf/stable/))\
    RAPIDS.AI 提供的 GPU 加速 DataFrame 库，语法类似 pandas。

## 数据可视化

用直观图表展示经济趋势、金融指标或社会现象。

1.  **Matplotlib** ([官网](https://matplotlib.org/))\
    Python 最基础的绘图库，适合精细定制各类图表。

2.  **Seaborn** ([官网](https://seaborn.pydata.org/))\
    用于统计图表绘制，默认风格美观，适合快速可视化。

3.  **Plotly** ([官网](https://plotly.com/python/))\
    支持交互式图表，适合构建金融仪表盘或 Web 分析应用。

4.  **Bokeh** ([官网](https://bokeh.org/))\
    适合 Web 端交互式可视化和实时流式数据图表。

## 统计与计量经济学

从基础统计到复杂计量模型，覆盖社会科学研究需求。

1.  **statsmodels** ([官网](https://www.statsmodels.org/))\
    回归分析、时间序列建模的首选工具，类似于 R 中的 `lm` 和 `glm`。

2.  **linearmodels** ([GitHub](https://github.com/bashtage/linearmodels))\
    提供工具变量、面板数据、系统 GMM 等高级计量方法。

3.  **ARCH** ([GitHub](https://github.com/bashtage/arch))\
    金融时间序列分析的经典库，支持 GARCH、EGARCH 等模型。

## 机器学习与 AutoML

从传统算法到经济预测，助力数据驱动决策。

1.  **scikit-learn** ([官网](https://scikit-learn.org/))\
    入门首选，集成分类、回归、聚类、降维等算法。

2.  **XGBoost / LightGBM** ([官网](https://xgboost.ai/), [文档](https://lightgbm.readthedocs.io/))\
    高性能梯度提升框架，广泛应用于风控、信贷评分等金融预测场景。

3.  **cuML** ([文档](https://docs.rapids.ai/api/cuml/stable/))\
    RAPIDS.AI 的 GPU 加速机器学习库，与 scikit-learn API 保持一致。

4.  **tslearn** ([GitHub](https://github.com/tslearn-team/tslearn))\
    专注于时间序列聚类、分类与对齐的机器学习工具。

5.  **PyCaret** ([GitHub](https://github.com/pycaret/pycaret))\
    自动化机器学习框架，封装 sklearn 流程，适合快速原型开发。

6.  **H2O.ai** ([官网](https://docs.h2o.ai/))\
    Java 编写的分布式 AutoML 平台，支持 Python、R、Java 接口，擅长大数据机器学习。

7.  **TPOT** ([GitHub](https://github.com/EpistasisLab/tpot))\
    基于遗传编程的 AutoML 工具，可自动搜索最优模型管道。

8.  **auto-sklearn** ([GitHub](https://github.com/automl/auto-sklearn))\
    基于贝叶斯优化的 AutoML 工具，兼容 sklearn 风格。

9.  **FLAML** ([GitHub](https://github.com/microsoft/FLAML))\
    微软开源的轻量级 AutoML 工具，支持低资源、高效率搜索。

## 金融科技与量化计算

专为金融数据、交易策略和经济建模设计。

1.  **QuantLib** ([GitHub](https://github.com/lballabio/quantlib))\
    金融工程标准工具，适用于衍生品定价与风险管理。

2.  **TA-Lib** ([官网](https://ta-lib.org/))\
    包含 150 多种技术指标（如 MACD、RSI），适合交易策略构建。

3.  **ccxt** ([官网](https://ccxt.com/))\
    统一 API 接入加密货币交易所，适合实时行情获取与策略执行。

4.  **PyPortfolioOpt** ([GitHub](https://github.com/robertmartin8/PyPortfolioOpt))\
    投资组合优化库，支持均值-方差、最小方差、风险平价等策略。

## 网络爬虫与自动化

高效获取公开经济数据或社会舆情信息。

1.  **Requests** ([官网](https://requests.readthedocs.io/))\
    简洁的 HTTP 库，适用于 API 抓取和基本数据请求。

2.  **BeautifulSoup** ([官网](https://www.crummy.com/software/BeautifulSoup/))\
    HTML/XML 解析利器，适合静态网页数据提取。

3.  **Selenium** ([官网](https://www.selenium.dev/))\
    浏览器自动化框架，支持处理 JavaScript 动态加载页面。

## 宏观与市场数据获取

1.  **yfinance** ([GitHub](https://github.com/ranaroussi/yfinance))\
    从 Yahoo Finance 抓取股票、汇率、指数等历史数据。

2.  **FRED API** ([官网](https://fred.stlouisfed.org/))\
    获取美国联储宏观经济数据（需配合 `fredapi` 包）。

3.  **Alpha Vantage** ([官网](https://www.alphavantage.co/))\
    免费金融数据 API，涵盖股票、外汇、加密货币等。

4.  **OECD API** ([官网](https://data.oecd.org/))\
    提供全球经济合作组织（OECD）各国经济社会数据。

## 自然语言处理（NLP）

适用于社会科学、金融情感分析、文本挖掘与用户舆情分析。

1.  **NLTK** ([官网](https://www.nltk.org/))\
    自然语言处理的经典教学工具，内置 50+ 语料库与词典资源（如 WordNet），适合快速原型构建与教学使用。

2.  **spaCy** ([官网](https://spacy.io/))\
    工业级 NLP 库，内建高效的文本处理组件，支持 GPU、多语言、预训练模型（如 BERT）、NER 与句法分析，适合大规模信息提取与生产部署。

3.  **Gensim** ([官网](https://radimrehurek.com/gensim/))\
    专用于主题建模、文档相似度计算与文本向量化，支持 LDA、LSA、word2vec 等主流算法，适合海量语料处理与信息检索场景。

## 参考资料与延伸阅读

-   [spaCy 官方网站](https://spacy.io/)
-   [NLTK 教程](https://www.nltk.org/book/)
-   [Gensim 教程与文档](https://radimrehurek.com/gensim/)
-   [spaCy Cheatsheet (PDF)](https://cheatography.com/kaochenlong/cheat-sheets/spacy/pdf/)
-   [Python Package Index (PyPI)](https://pypi.org/)
-   [RAPIDS.AI 官方文档](https://rapids.ai/ecosystem/#overview)
-   [ML-Python Best Of](https://ml-python.best-of.org/)
-   [scikit-learn 官方文档](https://scikit-learn.org/)
-   [statsmodels 官方文档](https://www.statsmodels.org/)
-   [H2O.ai 官方文档](https://docs.h2o.ai/)
-   [PyCaret 教程](https://github.com/pycaret/pycaret)
-   [auto-sklearn 教程](https://github.com/automl/auto-sklearn)
-   [TPOT 教程](https://github.com/EpistasisLab/tpot)
-   [FLAML 教程](https://github.com/microsoft/FLAML)

## 相关推文

> Note：产生如下推文列表的 Stata 命令为：\
>   `lianxh 扩展包 Python金融 selenium 可复现数据科学 , md nocat`\
> 安装最新版 `lianxh` 命令：\
>   `ssc install lianxh, replace`

-   范思妤, 2023, [Python：基于selenium爬取科创板审核问询](https://www.lianxh.cn/details/1172.html), 连享会 No.1172.
-   连小白, 2025, [R语言：Top期刊中使用最多的50个R扩展包](https://www.lianxh.cn/details/1550.html), 连享会 No.1550.
-   陈卓然, 2023, [Python金融分析系列-1：日期和时间变量的处理和转换](https://www.lianxh.cn/details/1294.html), 连享会 No.1294.
-   陈卓然, 2023, [Python金融分析系列-2：数据可视化](https://www.lianxh.cn/details/1295.html), 连享会 No.1295.
-   陈卓然, 2023, [Python金融分析系列-3：金融时间序列](https://www.lianxh.cn/details/1298.html), 连享会 No.1298.
-   陈卓然, 2023, [Python金融分析系列-4：数学工具-近似、凸优化、积分和符号运算](https://www.lianxh.cn/details/1300.html), 连享会 No.1300.
-   陈卓然, 2023, [Python：爬虫雅虎财经数据-selenium](https://www.lianxh.cn/details/1306.html), 连享会 No.1306.
-   高瑜, 2024, [新书推荐：可复现数据科学及 Python 应用](https://www.lianxh.cn/details/1485.html), 连享会 No.1485.