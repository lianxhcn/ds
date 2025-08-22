# 课程概览

## 课程内容

- **Part I：数据分析**
  - 数据获取
  - 数据清洗：合并、纵横变换、变量生成与转换
  - 数据清洗：缺失值、离群值、文字变量
  - 可视化：直方图、类别变量、散点图、三维图、动图
  - 复现报告
- **Part II：建模**
  - 线性回归分析：OLS，虚拟变量，交乘项，高阶项
  - 面板数据模型：高维固定效应模型、DID
  - 因果推断：反事实架构 
  - 机器学习：Lasso，随机森林，支持向量机 ……

<!-- --- - -- -->

## 课程提要

- **课程概述** 1 次
  - 金融数据分析的基本流程：目标、方法、工具、报告
  - 数据获取来源
  - 找资料找代码：[Github](https://github.com/arlionn), [Gitee-码云](https://gitee.com/arlionn/An-Introduction-to-Statistical-Learning)
  - 统计方法和计量模型概览
  - 可重复性报告：Markdown, VScode, Quarto, Jupyter Notebook
- **数据清洗** 2 次
  - 数据导入
  - 数据合并和追加
  - 离群值、缺失值
  - 数据转换
  - 基本统计分析

<!-- --- - -- -->

- **可视化** 2 次
  - 直方图、密度函数图
  - 分类变量可视化分析
  - 连续变量可视化分析
  - 变量相关性、时序变量、因果关系可视化
  - 三维图形和动态图形
- **回归分析** 3 次
  - 线性回归分析：OLS，虚拟变量，交乘项，面板数据模型
  - 广义线性模型：GLM，Logit，计数模型，MLE 估计
  - 结果输出和可视化
  - 案例：投资组合优化

<!-- --- - -- -->

- **时间序列分析** 1 次
  - ARMA 模型
  - GARCH 模型
- **机器学习** 3 次
  - Bootstrap、Monte Carlo 模拟、交叉验证
  - Lasso，变量筛选
  - K 近邻、随机森林、支持向量机等



<!-- --- - -- -->

## 作业和小组报告

**关于 AI 工具**

- 可以使用 AI 工具写作业和报告，可以使用 AI 写代码
- 但要提供提示词链接或提示词原文，如：[豆包-SVM 解读](https://www.doubao.com/thread/w9d7da7ee6fa0bc32)；&emsp;[ChatGPT-BAGTE 模型](https://chatgpt.com/share/67f0a7d3-cbcc-8005-857d-bbcfe4e680cd)；&emsp;[连玉君-UseChatGPT](https://github.com/arlionn/UseChatGPT/tree/main/Examples)

**软件**

- 不限制：用 Stata，R，Python 均可

**小组作业：**

- 6-8 次，每个小组有 2 次展示机会 (每次 20mins)
- 人数：每个小组 3 人 
- 技能：成员中至少一人会用 Stata；一人会用 Python
- 报告：需要用 VScode 或 Quarto 写报告
  - 用 [Marp](https://www.lianxh.cn/search.html?s=marp)，[Quarto](https://quarto.org/docs/get-started/) ([Presentation](https://quarto.org/docs/reference/formats/presentations/revealjs.html)) 或其他基于 Markdown 语法的工具制作 Slides
  - 不建议使用 PowerPoint 幻灯片


<!-- --- -->

## 参考书

**数据分析**

- Wes McKinney, **2023**. Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3E). [Online-Read](https://wesmckinney.com/book/), [github](https://github.com/wesm/pydata-book), [gitee-码云](https://gitee.com/wesmckinn/pydata-book)
  - 专注于数据处理，讲的比较细致 

- &#x1F34E; **PDSH** &emsp; VanderPlas, 2023. **Python Data Science Handbook**, [github](https://github.com/jakevdp/PythonDataScienceHandbook), [Online-Read](https://jakevdp.github.io/PythonDataScienceHandbook/index.html), [PDF-2E](https://dokumen.pub/python-data-science-handbook-essential-tools-for-working-with-data-2nbsped-1098121228-9781098121228.html) 
  - 数据分析 + 可视化 + 机器学习
  - 提供了 Colab版本，可以无需安装 Python，直接在线运行
    ![20250407145932](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250407145932.png)
  - 本地已经下载：**VanderPlas_2023_PDSH_Python_Data_Science_Handbook-2E.pdf**

<!-- --- - -- -->

**Finance**

- Scheuch, C., Voigt, S., Weiss, P., & Frey, C. (**2024**). **Tidy Finance with Python** (1st ed.). Chapman and Hall/CRC, [Online-Read](https://www.tidy-finance.org/python/index.html), [github](https://github.com/tidy-finance/website/tree/main/python)
  - [tidyfinance package](https://github.com/tidy-finance/py-tidyfinance)
  - 股票回报, CAPM, 投资组合, Fama-French 因子模型等
  - 整体上比较简单，依赖于作者开发的 `tidyfinance` 扩展包。
- Hilpisch Y., **Python for Finance**. 2019. [-PDF-](https://www.sea-stat.com/wp-content/uploads/2021/05/Yves-Hilpisch-Python-for-Finance_-Mastering-Data-Driven-Finance-Book-OReilly-2018.pdf#page=225.11), [github](https://github.com/yhilpisch/py4fi2nd)

**因果推断**

- Alves, Matheus Facure. **2022**, **Causal Inference for The Brave and True**. [Online Read](https://matheusfacure.github.io/python-causality-handbook/landing-page.html), [-github-](https://github.com/matheusfacure/python-causality-handbook)
  - 基本上覆盖了目前文献中使用多的多数因果推断方法，包括 IV, DID, SDID, PSM, Matching, Panel, SCM, RDD 
  - 提供了完整的 Python 代码，可以 Fork [-github-](https://github.com/matheusfacure/python-causality-handbook) 仓库，然后在本地运行 **.ipynb** 文档 (Jupyter Notebook)


**机器学习**


- &#x1F34E; **ISLP** &emsp; James, G., D. Witten, T. Hastie, R. Tibshirani. **An introduction to statistical learning**: with Applications in Python (ISLP)[M]. Springer, **2023**, [website](https://www.statlearning.com/), [Resources](https://www.statlearning.com/resources-python), [github](https://github.com/intro-stat-learning/ISLP_labs), [-PDF-](https://bayanbox.ir/view/1060725898744657072/An-Introduction-to-Statistical-Learning-with-Applications-in-Python.pdf)
  - [ISLP documentation](https://intro-stat-learning.github.io/ISLP/)：书中数据文件的详细说明
  - [各章 Python 实操部分](https://intro-stat-learning.github.io/ISLP/labs/Ch02-statlearn-lab.html)
    ![20250407145932](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250407145932.png)
  - [github-Notebooks](https://github.com/ogulcancicek/An-Introduction-to-Statistical-Learning-Python)&emsp; |&emsp; [Excercises and Solultions](https://github.com/hardikkamboj/An-Introduction-to-Statistical-Learning)
 
- Tatsat, H., Puri, S., & Lookabaugh, B. (2020). **Machine Learning and Data Science Blueprints for Finance**. O'Reilly Media. [-PDF-](https://soclibrary.futa.edu.ng/books/Machine%20Learning%20and%20Data%20Science%20Blueprints%20for%20Finance%20(Hariom%20Tatsat,%20Sahil%20Puri,%20Brad%20Lookabaugh)%20(Z-Library).pdf), [github-2022](https://github.com/tatsath/fin-ml), [githu-new-2024](https://github.com/alecontuIT/ml_for_finance)
  - 分成监督学习和非监督学习两大部分，包含了常用的机器学习方法
  - 13 cases，涉及债券市场，股票市场分析等
  - 书里边的所有案例对应的 Python 代码可以不用本地安装，而在作者提供的 [在线平台](https://mybinder.org/v2/gh/tatsath/fin-ml/master) 上直接运行。
    ![20250407145932](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250407145932.png)
  - 用的 Jupyter Notebook

<!-- --- - -- -->

## 获取数据

**中大图书馆**

> [中大图书馆-统计类数据库](https://library.sysu.edu.cn/page/3640?title=&eresource_sel2_ref%5B0%5D=133)

- CSMAR (国泰安数据库-公司金融-股票-债券): 
  - &#x1F34E; <https://data.csmar.com/>
- EPS数据平台
- [Wind资讯金融终端](https://library.sysu.edu.cn/eresource/364)
- [中经网产业数据](https://cyk.cei.cn/jsps/Default)
  - 国内宏观层面的数据基本上都能够找到。Excel &rarr; Python/Stata
  - [例：宏观数据](https://cyk.cei.cn/jsps/Banner?p=7a577a323842682b577237412b6b4b6e44416930556f3875357a4579464a6e56304d3752445359423745784b705547722f6b3563322b2f56755a614d36714d2b516f47584d79446175395874327970706241524e4730375662586264683577343752714c647562354133735832383158516f4434576154556164693332666f2b6b7677454f4759514c4c42584e4f6f4b553473757251533471354969715238653457567a6c354b42732f393076753773376b61305635694d544e3279426e4e6375534447497942782f7a4f4875416e5952647a346a6f685444457269776231344b486c584e4e6339535072554a3745526543316f4e6c4f766331624a65455650674e395a484c344d3142636f542f4f44724d6265564e696e5a413136684b62766959585a6b49505431646e52577938413267544151482f73713647576456667843373452747166563664566a7671664e707874616e37595855486255374765454241723045564c436274773d)
- [中经网统计数据库](https://library.sysu.edu.cn/eresource/771)
- [EMIS—Emerging Markets Information Service（新兴市场动态及商务信息数据库）](https://library.sysu.edu.cn/eresource/769)
  - 新闻，股指，最新统计数据等
  - [China - Financial markest](https://www.emis.cn/v2/countries/profile/CN/financial-markets/)

<!-- --- - -- -->

**RESSET系列数据库**

- [RESSET系列数据库](https://library.sysu.edu.cn/eresource/1540) | [RESSET企业大数据平台](https://library.sysu.edu.cn/eresource/1541)
  - 需要输入账号和密码
  - 1、中山大学校园网IP范围内，直接点击访问。
  - 2、官方网站访问： http://www.resset.cn，点击页面“快速登录”右边的“企业大数据平台”链接后输入对应的用户名及密码进行登录。用户名：sysu和密码：sysu1903。
  - 3、校外不限IP访问，通过CARSI平台访问登陆，访问地址：http://db.resset.com/，点击页面的：CARIS 平台登陆，选择学校，然后输入验证身份信息后登陆使用。

**全球数据**

- 连小白, 2025, [GMD：最新全球宏观数据库-243个国家46个宏观变量](https://www.lianxh.cn/details/1559.html), 连享会 No.1559.
  - <https://www.globalmacrodata.com/data.html>

<!-- --- - -- -->

**到哪里找数据？**

> Source: 黄湘云, [R 语言数据分析实战-介绍](https://bookdown.org/xiangyun/data-analysis-in-action/preface.html) 

- [数据获取概述](https://bookdown.org/xiangyun/data-analysis-in-action/wrangling-collection.html)，写的不错

- 各国、各级政府的统计局，比如[美国人口调查局](https://www.census.gov/data.html)、[中国国家统计局](http://www.stats.gov.cn/)等。
- 国际、国内各类组织机构，比如[世界银行](https://www.shihang.org/zh/home)、[美国疾病预防控制中心](https://www.cdc.gov/)等。
- 各类网站提供的数据集，比如 GitHub 开放数据集列表 [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)，[kaggle](https://www.kaggle.com/datasets) 网站提供大量数据分析竞赛及相应的数据集。
- R 包内置数据集，已整理得很好，比如 [**spData**](https://github.com/Nowosad/spData/) 包 收集整理了很多空间统计方面的数据集。[Rdatasets](https://github.com/vincentarelbundock/Rdatasets) 更是收集约 1900 个数据集，全部来自 CRAN 上发布的 R 包。


