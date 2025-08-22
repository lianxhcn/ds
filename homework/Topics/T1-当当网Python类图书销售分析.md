## 当当网 Python 类图书销售信息分析

### 任务基本信息
- 目的：从当当网获取 Python 相关书籍的销售量信息，最终输出一份市场调研报告。
- 语言：Python
- 网站：[https://search.dangdang.com/](https://search.dangdang.com/)
- 关键词：'python'
- 排序关键词：'销量'
- 排序方式：从高到低
- 信息条数：前 50 条
- 目前搜索结果页面URL：[https://search.dangdang.com/?key=python\&act=input\&sort\_type=sort\_sale\_amt\_desc#J\_tab](https://search.dangdang.com/?key=python&act=input&sort_type=sort_sale_amt_desc#J_tab)
- 需要收集的信息： 
  - 书名，作者，年份，出版社，评论数，原价、折后价

### 分析目标

假设你是一个教师，准备写一本有关 Python 的书籍。在开始之前，你想先了解一下相关情况。目前主要关注在当当网销量排名前 50 的 Python 类户籍。

你想通过数据分析，了解如下信息：

1. 销量排名前 10 的 Python 类图书清单？
2. 销量前 50 的 Python 类图书主要涵盖了哪些领域？比如，编程技巧、数据分析、机器学习和深度学习、青少年编程等 (可以自行定义)
3. 销量前 50 的 Python 类图书中，哪些出版社的书籍比较多？
4. 销量前 50 的 Python 类图书中，原价和折后价的分布，折扣率的分布特征。

如果有兴趣，也可以进一步分析如下问题 (选做)：

1. 词频分析。去除无用词汇后，分析销量前 50 的 Python 类图书的书名中，哪些词汇出现频率较高？
2. 不同类型的 Python 书籍的售价情况。
3. “书名” 中的关键词与售价和销量之间是否存在关联？
