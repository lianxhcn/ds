## 个人作业


## 提交

- 提交链接：[点击提交作业](https://gitee.com/link?target=https%3A%2F%2Fworkspace.jianguoyun.com%2Finbox%2Fcollect%2F8b71e5254a0f4f36ac95b582ffd7f2db%2Fsubmit) &#x1F34E; 

## 任务说明

1. Python 环境配置。请参照讲义 [6  Python：安装和环境配置](https://book.lianxh.cn/ds/body/01_1_install-Python-Anocanda.html) 中的说明，安装必要软件和插件，配置好 Python 运行环境。
2. 新建一个 `ex01_姓名.ipynb` 文件。
3. 添加一个 Markdown 单元格，写上你的姓名和学号，以及你对作业内容的简要介绍。
4. 添加一个 Python 代码单元格，根据如下提示词生成 Python 代码，产生模拟数据 (你可以使用 Copilot 或 ChatGPT 等工具)：

   ```raw
   生成模拟数据：N = 500，包含 2 个变量 (x1, x2)，x1 ~ N(0, 1)，x2 ~ N(3, 1.5)，corr(x1, x2) = 0.4。
   1. 存入一个名为 df 的数据框中。
   2. 种子值为：`你的学号后三位`。
   ```

5. 完成如下分析任务：每个任务对应三个单元格：
   - 先插入一个 Markdown 单元格：添加标题和说明文字，介绍你要分析什么
   - 再插入一个代码单元格，贴入你的代码并运行
   - 最后再插入一个 Markdown 单元格，解释结果。
   
   具体任务如下：

   ```Markdown 
   1. 呈现 df 数据框的前 5 行。
   2. 呈现 df 数据框的描述性统计，包括均值，标准差，中位数，最大值，最小值，偏度，峰度。
   3. 呈现 x1 的直方图。
   4. 在同一幅图中绘制 x1 和 x2 的密度函数图。
   5. 在同一幅图中绘制 x1 和 x2 的箱线图。
   6. 在同一幅图中绘制 x1 和 x2 的小提琴图。
   7. 计算 df 中 x1 和 x2 的相关系数，并输出结果。
   8. 绘制 x1 和 x2 的散点图，添加回归线和置信区间。
   ```
   
6. 提交：`ex01_姓名.ipynb` 文件。

