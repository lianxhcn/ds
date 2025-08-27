---
marp: true
size: 16:9        # 宽版：4:3
paginate: true  
#header: '[连享会](https://www.lianxh.cn/news/46917f1076104.html)'
footer: '[lianxh.cn](https://www.lianxh.cn)&ensp;|&ensp;[Books](https://www.lianxh.cn/Books.html)'
---

<style>
/*一级标题局中*/
section.lead h1 {
  text-align: center; /*其他参数：left, right*/
}
section {
  font-size: 24px;      /* 正文字号 */
}
h1 {
  color: blackyellow;   /* 标题的颜色 */
  /*font-size: 28px; */ /* 标题的字号, 其它标题也可以这样修改 */
}
h2 {
  color: green;
}
h3 {
  color: darkblue;
}
h4 {
  color: brown;
}
/* 右下角添加页码 */
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total); 
}
header,
footer {
  position: absolute;
  left: 50px;
  right: 50px;
  height: 25px;
}
/* 调整图片与文本之间的间距 */
section img {
  margin-right: 10px;   /* 设置图片右侧的间距 */
  margin-left: 10px;   /* 设置图片左侧的间距 */
}

/* 设置正文区域的边距，确保文本能更紧凑地放置 */
section {
  #padding-right: 20px;  /* 设置右侧边距 */
  #padding-left: 20px;  /* 设置左侧边距 */
}

/* ====== 新增：设置代码块字号 ====== */

/* 默认代码块字号 */
pre {
  font-size: 22px;
}

/* 可选类：小字号代码块 */
.small-code pre {
  font-size: 12px;
}

/* 可选类：大字号代码块 */
.large-code pre {
  font-size: 20px;
}

/* 5:5 等宽双栏 */
.columns { display: flex; gap: 24px; align-items: flex-start; }
.col-5 { flex: 5 1 0; }   /* 左右各 5 */
</style>

<!--顶部文字-->


<!--封面图片-->


![bg right:55% w:500 brightness:. sepia:50%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/qrcode_ds_share_2025-PDF.png)


<!--幻灯片标题-->

## 课程建设经验分享
# 数据分析与经济决策

<br>
<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>

> **课程主页**：
> <https://lianxhcn.github.io/ds>   

> **Github 仓库**：
> <https://github.com/lianxhcn/ds>

<!-- backgroundColor: #FFFFF9 -->


--- - --
<!-- backgroundColor: white -->

&emsp; &emsp; &emsp; &emsp; &emsp; ![w:1200](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250828000841.png)

--- - --

- 整体感受
- 课程内容
- 教什么？
- 如何教？
- 讨论


---

# 整体感受

- 敬畏之心：和学生一起学习 
  - Stata/R &rarr; Python；LLM；GenAI
  - 课前准备：确定主题、摸底、与相关课程老师沟通

- 让学生卷起来
  - 作业设计、课堂讨论、私下讨论 (线人)

- 思路转变
  - 钓鱼
  - 推理和拆解 

---

![w:1400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250828003453.png)

---
<!-- backgroundColor: #cdf27eff -->
# 教指委的课程指南

--- 
<!-- backgroundColor: white -->
## 一、课程概述

- 《数据分析与经济决策》是数字经济专业硕士研究生的核心课程之一。
- 课程目标：为学生提供全面的数据分析技能，支持数字经济领域的决策与实践。
- 学习内容涵盖：
  - 数据分析在经济决策中的作用与意义
  - 数据预处理、统计推断与因果推断
  - 机器学习与深度学习 *
  - 贝叶斯方法 * 
  - 网络分析与社交媒体数据分析 *
  - 大语言模型及自然语言处理 *
- 强调数据分析方法在辅助经济决策中的应用。
- 学生将具备扎实的数据处理、分析、解释及决策能力。
- 为未来从事科研、政策制定或企业决策打下坚实基础。

---

## 三、课程目标

1. 熟练掌握数据分析方法；
2. 运用机器学习和深度学习算法；
3. 掌握网络和社交媒体数据分析能力；
4. 了解经济决策的基本原理和方法；
5. 培养数据驱动决策的能力。

---

## 五、授课方式

- 本课程采用多种教学方法，包括课堂教师讲授和课堂互动讨论相结合。
- 基础理论知识由教师进行课堂讲授，而应用和数据分析则通过课堂讨论互动的方式实现。
- 另外，积极引入在线学习平台和资源，为学生提供更丰富的学习资源和学习方式。
- 利用智能辅助教学工具，以及数据可视化工具和软件，来提升学习效果。



---
<!-- backgroundColor: #d1f5f7ff -->

# 课前摸底

> 学生人数：55 人；age：24-49 岁

1. 你会用哪些软件？（多选题）
2. 你了解以下哪些方法?（多选题）
3. 你期望学习哪方面的内容？（多选）
4. 你经常使用哪些 AI 工具？
5. 你更喜欢哪种授课方式？

--- - --
<!-- backgroundColor: white -->

![20250820170751](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820170751.png)

--- - --


![h:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820171019.png)

---

![20250820170253](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820170253.png)

---

![h:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820171303.png)

---

## 教学模式选择

### 9-1 模式

  - 90% 以上由老师讲授，学生课后完成作业

### 6-4 模式

  1. 老师讲授核心概念和原理、数据分析流程等
  2. **小组作业**：一个小型的数据处理和分析项目
  3. 课堂上留出大概 2/5 的时间，由学生报告，并与同学和老师做详细的讨论。

![bg right:45% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820171611.png)

---

## 学生背景 (1)

![bg right:55% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250821183906.png)

**制造与实业**: 21 人
- 中国联合网络通信集团
- 广东裁成律师事务所
- 广州安迅经济发展有限公司
- 广东天禾农资股份有限公司

**政府与事业单位**: 11 人
- 广州市烟草专卖局
- 佛山市商务局
- 萍乡市发展和改革委员会
- 广州市荔湾区财政局
  
<!-- ---

## 学生背景 (2)

**互联网与信息科技**（人数最多，典型单位）
- 数字广东网络建设有限公司
- 荣耀终端有限公司
- 深圳市积加跨境网络科技有限公司
- 阿里巴巴集团

**银行与金控**（示例单位）
- 交通银行股份有限公司广州花都支行
- 中国工商银行股份有限公司广东省分行
- 广发银行股份有限公司信用卡中心

**保险**（示例单位）
- 富德财产保险股份有限公司
- 大家人寿保险股份有限公司广东分公司
- 中国人寿保险股份有限公司广东省分公司

**证券与期货**（示例单位）
- 招商证券股份有限公司
- 广发期货
- 中信证券

**媒体出版**（示例单位）
- 南方财经全媒体集团 -->

---

## 学生背景 (2)

<div class="columns">
  <div class="col-5">

**互联网与信息科技**
- 数字广东网络建设有限公司
- 荣耀终端有限公司
- 深圳市积加跨境网络科技有限公司
- 阿里巴巴集团

**银行与金控**
- 交通银行股份有限公司广州花都支行
- 中国工商银行股份有限公司广东省分行
- 广发银行股份有限公司信用卡中心
  </div>
  <div class="col-5">

**保险**
- 富德财产保险股份有限公司
- 大家人寿保险股份有限公司广东分公司
- 中国人寿保险股份有限公司广东省分公司

**证券与期货**
- 招商证券股份有限公司
- 广发期货
- 中信证券

**媒体出版**
- 南方财经全媒体集团

  </div>
</div>




---

<!-- backgroundColor: #d1f5f7ff -->

# 教什么？

- 教指委的课程指南
  
- 我们实际教授的内容

---
<!-- backgroundColor: white -->
## 教指委 · 课程指南（1）

1. **基础**
   - 数据获取与清洗  
   - 描述性统计与可视化  
   - 统计推断：估计、检验、方差分析  

2. **因果与机器学习**
   - 因果推断：实验与政策评估  
   - 机器学习：监督 / 非监督  
   - 分类与聚类：树、KNN、K-means  

---
## 教指委 · 课程指南（2）
3. **高级方法**
   - 深度学习与神经网络  
   - 贝叶斯方法与风险管理  
   - 网络分析与社交媒体数据  
   - 大语言模型（LLM）与文本分析  


--- 

# 我们教的主要内容

- 数据分析的 **目的**
  - **搞清楚事实**：数据清理和可视化 
  - **搞清楚关系**：回归分析、因果推断
  - **预测**：时间序列分析、机器学习
  - **辅助决策**：优化、模拟

- 数据分析的 **流程**
  - 目标 &rarr; 数据 &rarr; 方法 &rarr; 结果 &rarr; 决策 
- 数据分析的 **工具**
  - AI 工具 + Python + Jupyter Notebook
  - Github + Github Desktop
  - Markdown + Marp


---

### 主要模块 (1)

- 数据的获取
  - 常用数据库：CSMAR、Wind、CEIC
  - API：`yfinance`、`tushare`、`akshare` ……
  - 爬虫
- 数据清洗和格式化
  - 项目文档结构
  - 格式化数据与非格式化数据
  - 数据变换、二次编码、离群值
- 数据可视化 
  - 常用图表 (密度函数图、箱线图、分仓散点图)
  - 可视化的一些基本原则

---

### 主要模块 (2)

- 探索性数据分析 (EDA)
  - 了解数据的基本特征、变量之间的关系
  - 初步建模
- 常用统计和计量模型
  - 入手：数据类型和分布特征
  - 假设检验和统计推断：传统 &rarr; Bootstrap + 交叉验证
  - 线性模型 &rarr; GLM &rarr; 离散选择和受限因变量
  - 机器学习方法
    - 分类、回归、聚类、降维
    - 树模型、随机森林、XGBoost

---

### 主要模块 (3)

- 数据分析案例
  - 上市公司财务分析：负债率
  - 宏观经济分析：GDP、失业率、通胀率
  - 金融市场分析：股票收益率、波动率、风险溢价
  - 消费行为分析：客户细分、购买预测
  - 文本数据分析：情感分析、主题建模
  - 网络数据分析：社交网络、影响力传播




---

<!-- backgroundColor: #d1f5f7ff -->

# 如何教？

--- - --
<!-- backgroundColor: white -->
## 如何教？整体思路

&#x1F34E; 搭好戏台 &rarr; 缺啥补啥 &rarr; 先让代码跑起来

- AI 辅助教学
- 原理 + 流程 + 规范
- 统计软件和工具的选择
  - Python + Jupyter Notebook
  - Github + GitHub Copilot + Github Desktop
  - 好处：提高编程效率，便于协作和版本控制

- Markdown
  - 一定要多写：想不清楚的东西一定写不清楚
  - 使用 Marp 制作幻灯片


---

## 如何教？作业

- 个人作业：每周一次 (2-3 小时)
  - [ex_P01.md](https://github.com/lianxhcn/ds/blob/main/homework/ex_P01.md)&emsp;|&emsp;[ex_P02.md](https://github.com/lianxhcn/ds/blob/main/homework/ex_P02.md)

- 小组作业：2-3 个 (每组 4-5 人)
  - 根据兴趣选择案例 (最好能提供 [备选主题](https://github.com/lianxhcn/ds/tree/main/homework/Topics))
  - 展示和讨论 (2-3 个小组做同一个案例)

- 老师：设计作业 v.s. 布置作业

---

## 如何教？收作业

- 目前：坚果云 [交作业](https://github.com/lianxhcn/ds/tree/main/homework)

- 以后：github [助教工作指南](https://github.com/arlionn/lianxhta)



---

## 如何教？教材和讲义

- 教材：理论基础扎实、结构完整
  - [2  课程简介和资源](https://lianxhcn.github.io/ds/body/00_intro.html)

- AI 辅助生成，参见 连玉君, 2025, [Empirical Research with AI](https://lianxhcn.github.io/research_with_AI/) 
  - 关键：学会写提示词 - 结构、逻辑

- Github 仓库
  - [2  课程简介和资源](https://lianxhcn.github.io/ds/body/00_intro.html)
  - [6100+ 仓库](https://github.com/search?q=data+science+python&type=repositories)

- 在线讲义：Quarto + GitHub Pages
  - 连玉君，2025，[Quarto Book](https://lianxhcn.github.io/quarto_book/)
  - [用 Quarto book 写的书](https://lianxhcn.github.io/quarto_book/body/05_references.html#%E7%94%A8-quarto-book-%E5%86%99%E7%9A%84%E4%B9%A6)
 
---

## Python 

- [Problem Solving with Python](https://problemsolvingwithpython.com/) by Kazarinoff
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Sweigart
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by VanderPlas
- [Think Python: How to Think Like a Computer Scientist](https://greenteapress.com/thinkpython2/html/) by Downey
- [A Bite of Python](https://python.swaroopch.com/)
- [Dive Into Python 3](https://diveintopython3.net/) by Pilgrim


---

<!-- backgroundColor: #d1f5f7ff -->

# 讨论

---
<!-- backgroundColor: #FFFFF9 -->

## 讨论 1：彼此的优势

### 老师

- 理论基础
- 工具地图和分析流程
- 前沿工具

### 学生

- 实践经验 &rarr; 应用场景 (提问)
- 案例分析能力
- 内卷的潜力：对新工具的适应能力

---

## 讨论 2：教学模式

- 环境配置：让代码跑起来 (信心)

- 学生没有能力或者需要花很多时间才能理解的内容
  - 线性回归 &rarr; 非参数估计 (KNN, 核密度函数图, 随机森林) 
  - 条件期望 + 条件概率 &rarr; GLM (广义线性模型) &rarr; Logit/Duration
- 分析流程和规范 (经验)
  - EDA &rarr; 可视化 &rarr; 回归分析 &rarr; 机器学习
  - 离群值
  - 非结构化数据 &rarr; 结构化数据
- 阅读和检索能力 &rarr; 知道周围在发生什么 &rarr; 趋势敏感性

---
<!-- backgroundColor: #FFFFF9 -->
## 一些典型的大纲

- Harvard University, [Data Analysis Courses](https://pll.harvard.edu/subject/data-analysis), 课程分类很细致，提供了大量免费在线课程

- Washington State UNIVERSITY, [Data Analytics Course Syllabi](https://data-analytics.wsu.edu/data-analytics-course-syllabi/) (19 门课)
  - [Statistical Modeling for Data Analytics](https://data-analytics.wsu.edu/documents/2024/08/data-435-syllabus.pdf/)


## 教学模式

- 思路一：教方法和模型 &rarr; 学生自行选择案例分析对象
- 思路二：案例导向 &rarr; 学生根据自己的需要来学习

--- 

## 讨论 3：作业

### 个人作业：
- 环境配置
- 基础知识和概念
- &#x1F34E;：要让学生「卷起来」
- 量大，有一定难度

### 小组作业：

- 根据兴趣选择案例
- 展示和讨论 (2-3 个小组做同一个案例)
- 作业库？

--- 

## 讨论 4：教材和讲义

- 联合编写教材和讲义

- Github + Quarto (协作)


---

## 讨论 5：案例库 &#x1F34F;

- MBA 教学经验：[中欧案例库](https://www.chinacases.org/anon/casehelp/anon_casehelp_category/anonCasehelpCategory.do?method=view&fdId=17862da992a3f9f0d0322164cf0ae791&s_css=default&mainFdId=18e2bf77b4949fae1a9fd6f4132a5d2b&vido2=true&lang=zh-CN)
  - 岭院的师资培训：MIT Sloan 管理学院 (5 个月) + 中欧案例培训
  - MBA 教学经验：[MBA-CF](https://gitee.com/arlionn/MBA-CF/wikis/%E8%AF%BE%E7%A8%8B%E5%A4%A7%E7%BA%B2/0.%20%E4%BA%A4%E4%BD%9C%E4%B8%9A%E5%85%A5%E5%8F%A3)
- Kaggle 数据平台 (https://www.kaggle.com/datasets)
  - 深度不够、案例背景资料缺乏
- 学生的资源
  - 案例报告 / 小组作业
  - 毕业论文
  - 校企合作
- 年度案例大赛或案例征集

---

<center>

<https://lianxhcn.github.com/ds>

</center>