# 当当网Python书籍爬虫项目

本项目旨在爬取当当网上Python相关书籍的销售信息，并进行数据分析。

## 项目结构

```
DangDang_Crawler/
├── data_raw/          # 存放原始爬取数据
├── data_clean/        # 存放清洗后的数据
├── README.md          # 项目说明文档
├── 01_data_clean.ipynb    # 数据清洗程序
└── 02_data_analysis.ipynb # 数据分析程序
```

## 使用说明

1. 运行顺序：
   - 然后运行 `01_data_clean.ipynb` 清洗数据（已运行，如果要重复运行，可以先把data_clean中的文件夹清空）
   - 最后运行 `02_data_analysis.ipynb` 进行分析（可以单独运行，如果想分模块运行，务必先运行第一模块校验数据以及安装中文适配）

## 数据来源

- 数据来源：当当网 (https://search.dangdang.com/)
- 爬取内容：Python相关书籍信息
  - 没有使用python程序来进行爬取，最后使用了扣子空间的AI视觉爬取方案进行网站信息的提取
  - 提示词：
      网站：https://search.dangdang.com/
      关键词：'python'
      排序关键词：'销量'
      排序方式：从高到低
      信息条数：前 50 条
      目前搜索结果页面URL：https://search.dangdang.com/?key=python&act=input&sort_type=sort_sale_amt_desc#J_tab
      需要收集的信息：
      书名，作者，年份，出版社，评论数，原价、折后价
      帮我从当当网收集一下信息，数据结果用excel文件存储
- 爬取字段：
  - 书名
  - 作者
  - 出版年份
  - 出版社
  - 评论数
  - 原价
  - 折后价

## 注意事项
1. 所有数据仅用于学习研究，请勿用于商业用途 