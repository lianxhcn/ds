## 简介

看官方说明文档 [Python 教程](https://docs.python.org/zh-cn/3.13/tutorial/index.html) 即可快速入门。 

## 基本要求

- [A Quick Tour of Python Language Syntax](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/02-Basic-Python-Syntax.ipynb)
  - 空格，缩进等要求




## 命令语法规则

Python 的命令可以分为如下几大类：
- `import`：导入模块
- `df = pd.read_csv(./data/gpd.csv)`：读取数据
    - `df`：数据框对象
    - `pd`：pandas 模块
    - `read_csv()`：读取 CSV 文件的函数

通用结构：
- `对象名 = 模块名.函数名(参数)`，例如 `df = pd.read_csv(./data/gpd.csv)`
  - `对象名`：变量名，通常是数据框、列表、字典等数据结构
  - `模块名`：导入的模块名称，如 `pandas`、`numpy` 等
  - `函数名`：模块中的函数名称，如 `read_csv()`、`mean()` 等
- `对象名 = 模块名.子模块名.函数名()`，例如 `statsmodels.api.OLS(y, X).fit()`
    - 这种写法表示通过模块和子模块调用某个函数或类，并将结果赋值给一个变量。例如，`statsmodels.api.OLS(y, X)` 创建一个线性回归模型对象，`.fit()` 是该对象的方法，用于拟合模型。整个表达式 `statsmodels.api.OLS(y, X).fit()` 返回一个拟合后的模型对象，通常赋值给 `result` 或 `modelfit` 变量。这里 `OLS` 实际上是一个类名，`fit()` 是该类的实例方法。通过链式调用，可以一步完成模型的创建和拟合过程。
    - 我们可以把 `statsmodels.api.OLS(y, X).fit()` 拆解成如下几条语句，以便理解哪些是「函数」，哪些是「方法」：
        ```python
        import statsmodels.api as sm
        model = sm.OLS(y, X)  # 创建 OLS 模型对象
        result = model.fit()  # 拟合模型
        ```
    其中，`statasmodel.api` 是一个模块，我们使用 `import xxx as sm` 的方式导入它。`OLS` 是 `statsmodels.api` 模块中的一个类，用于创建线性回归模型对象。`fit()` 是 `OLS` 类的一个方法，用于拟合模型。

一些更复杂的例子：

- `result = statsmodels.api.OLS(y, X).fit()`
  - 结构：`对象名 = 模块名.子模块名.类名(参数).方法名()`
    - `statsmodels.api`：statsmodels 的 api 子模块
    - `OLS`：线性回归类
    - `fit()`：拟合模型的方法

- `plt.subplots(figsize=(8, 6))`
  - 结构：`模块名.函数名(参数=值)`
    - `plt`：matplotlib.pyplot 模块
    - `subplots()`：创建图表和坐标轴的函数
    - `figsize=(8, 6)`：指定图像大小的参数

- `df['new_col'] = df['col1'] + df['col2']`
  - 结构：`对象名['新列'] = 对象名['列1'] + 对象名['列2']`
    - 通过运算创建新列

- `df.groupby('地区')['收入'].mean()`
  - 结构：`对象名.groupby('列名')['列名'].方法名()`
    - `groupby()`：分组函数
    - `mean()`：计算均值的方法

这些例子展示了 Python 常见的链式调用、属性访问和函数调用的语法结构。
- `df.head()`：查看数据框的前几行
  - 结构：`对象名.函数名()`
    - `df`：数据框对象
    - `head()`：查看数据框的前几行的函数
- `df['column']`：查看数据框的某一列
  - 结构：`对象名['列名']`
    - `df`：数据框对象
    - `column`：数据框的列名 (索引，切片)
- `modelfit.residuals`：查看模型的残差
  - 结构：`对象名.属性名`
    - `modelfit`：模型对象
    - `residuals`：模型的残差属性

## 断行

