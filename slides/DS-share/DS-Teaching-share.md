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
  font-size: 22px;      /* 正文字号 */
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


<br>

<!--封面图片-->
![bg right:60% w:700 brightness:. sepia:50%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250610225636.png) 



<!--幻灯片标题-->

### 数据分析与经济决策

<br>

# 课程建设经验分享



<br>
<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>

<!-- backgroundColor: #FFFFF9 -->


--- - --

# 课程内容
# 如何教？
# 教什么？
# 学生的特点


---

# 课前摸底

1. 你会用哪些软件？（多选题）
2. 你了解以下哪些方法?（多选题）
3. 你期望学习哪方面的内容？（多选）
4. 你经常使用哪些 AI 工具？
5. 你更喜欢哪种授课方式？

--- - --

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

  - 90% 以上的时间由老师讲授，学生课后完成作业

### 6-4 模式

  - 老师讲授最重要的概念和原理，以及一些数据分析的流程。
  - 布置小组作业：一个小型的数据处理和分析项目
  - 课堂上留出大概 2/5 的时间，由学生报告，并与同学和老师做详细的讨论。

![bg right:45% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250820171611.png)

---

## 学生背景 (1)

![bg right:55% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250821183906.png)

**制造与实业**: 21 人
- 中国联合网络通信集团广东省分公司
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

# 教什么？

- 思路一：教方法和模型 &rarr; 学生自行选择案例分析对象
- 思路二：案例导向 &rarr; 学生根据自己的需要来学习

--- 

## 覆盖的主要内容

- 数据分析的目的
  - 数据清理和可视化 
  - 预测 v.s. 因果推断
- 数据分析的流程
- 数据分析的工具

### 主要模块

- 数据的获取
  - CSMAR
  - API
  - `akshare` package
  - 爬虫
- 数据清洗和格式化
  - 项目文档结构
  - 数据字典
  - 格式化数据与非格式化数据
  - 数据变换、二次编码、离群值
- 数据可视化 
  - 常用图表 (直方图、密度函数图、散点图、分仓散点图、类别变量)
  - 可视化的一些基本原则
- EDA
- 常用统计和计量模型
  - 入手：数据类型和分布特征
  - 假设检验
  - 线性模型
  - GLM
  - 离散选择和受限因变量
  - 机器学习方法
    - 分类、回归、聚类、降维
- 数据分析案例

---

# 一些典型的大纲

- Harvard University, [Data Analysis Courses](https://pll.harvard.edu/subject/data-analysis), 课程分类很细致，提供了大量免费在线课程

- Washington State UNIVERSITY, [Data Analytics Course Syllabi](https://data-analytics.wsu.edu/data-analytics-course-syllabi/) (19 门课)
  - [Statistical Modeling for Data Analytics](https://data-analytics.wsu.edu/documents/2024/08/data-435-syllabus.pdf/)


---

## 如何教？

- AI 辅助教学
- 原理 + 流程 + 规范
- 统计软件和工具的选择
  - Python + Jupyter Notebook
  - Github + GitHub Copilot + Github Desktop
  - 好处：提高编程效率，便于协作和版本控制
    - 版本控制：记录代码变更，便于回溯和协作
    - 代码补全：提高编码效率，减少错误
    - 小组协作：便于团队成员之间的协作
    - Fork 和 Pull Request：利用全球最优质的代码和项目资源
- Markdown
  - 写讲义
  - 使用 Marp 制作幻灯片


---

## 如何教？作业

- 个人作业
- 小组作业

---

## 如何教？收作业



---

# 教材和讲义


## Python 

- [Problem Solving with Python](https://problemsolvingwithpython.com/) by Kazarinoff
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Sweigart
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by VanderPlas
- [Think Python: How to Think Like a Computer Scientist](https://greenteapress.com/thinkpython2/html/) by Downey
- [A Bite of Python](https://python.swaroopch.com/)
- [Dive Into Python 3](https://diveintopython3.net/) by Pilgrim


---

Computational tools for reproducible data analysis and version control (Git/GitHub, Emacs/RStudio/Spyder), reproducible data (Data repositories/Dataverse) and reproducible dynamic report generation (Rmarkdown/R Notebook/Jupyter/Pandoc), and workflows.