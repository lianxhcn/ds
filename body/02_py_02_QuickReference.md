# Python 常用命令速查表

> [ChatGPT 对话](https://chatgpt.com/share/681e06b0-3d44-8005-91d6-003124a2ee71)



> **入门资料**

- [Python 官方文档（中文）](https://docs.python.org/zh-cn/3/)：权威资料
- [菜鸟教程：Python 教程](https://www.runoob.com/python3/python3-tutorial.html)：适合新手
- [pandas 官方文档](https://pandas.pydata.org/docs/)：数据处理
- [NumPy 用户指南](https://numpy.org/doc/)：数值计算
- [matplotlib 使用指南](https://matplotlib.org/stable/users/index.html)：数据可视化



## 环境配置

- [Anaconda](https://www.anaconda.com/)：推荐使用 Anaconda 进行 Python 环境管理和包安装
  - [Getting started with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [VS Code](https://code.visualstudio.com/)：推荐使用 VS Code 作为 Python 开发环境
- VS Code 常用插件（推荐安装）
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)（基础语法支持）
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)（运行 .ipynb 文件）
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)（智能补全与类型检查）
  - [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) / [ChatGPT 插件](https://marketplace.visualstudio.com/items?itemName=Gencraft.chatgpt-vscode)（AI 辅助编程）
  - [Data wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.data-wrangler)（呈现表格）


## 基础语法与变量操作

```python
print("Hello, world!")       # 输出字符串
name = input("请输入姓名：")  # 获取用户输入
x = 5                        # 赋值
type(x)                      # 查看变量类型
int("123"), str(123)         # 类型转换
len("abc")                   # 求长度（字符串、列表等通用）

num = 3.14                   # 浮点数
is_active = True             # 布尔值
x, y, z = 1, 2, "three"      # 多变量赋值
10 // 3                      # 整除 → 3
2 ** 3                       # 幂运算 → 8
abs(-5)                      # 绝对值
round(3.1415, 2)             # 四舍五入
```

## 控制流程

```python
# 条件判断
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("负数")

# for 循环
for i in range(5):
    print(i)

# while 循环
while x < 10:
    x += 1

# 跳出、跳过、占位
break, continue, pass
```


## 常用数据结构命令

### 字符串 `str`

```python
s = "hello"
s.upper(), s.lower()        # 转大写、小写
s.replace("l", "L")         # 替换字符
s.split(",")                # 分割字符串
",".join(["a", "b"])        # 合并为字符串
```

### 列表 `list`

```python
lst = [1, 2, 3]
lst.append(4)               # 添加元素
lst.pop()                   # 删除最后一个
lst[0], lst[-1]             # 索引访问第一个、最后一个元素
lst[1:3]                    # 切片

lst.insert(1, 1.5)          # 指定位置插入
lst.remove(1.5)             # 删除指定元素
lst.extend([4,5])           # 合并列表
lst.index(2)                # 查找元素索引
[ x**2 for x in lst ]       # 列表推导式
```

### 字典 `dict`

```python
d = {"a": 1, "b": 2}        # 创建字典
d["a"]                      # 通过键取值
d.get("a", 0)               # 安全取值，键不存在返回默认值
d.keys(), d.values(), d.items()  # 获取所有键、值、键-值对
```

### 集合 `set`

```python
s = set([1, 2, 3])
s.add(4)
s.union({2, 5})          # 求并集
s.intersection({2, 3})   # 求交集
```


## 文件、路径、项目设置

```python
import os
os.getcwd()                 # 当前工作目录
os.chdir("路径")            # 切换目录
os.listdir()                # 查看目录内容
os.path.exists("data.txt")  # 检查文件存在
os.mkdir("new_folder")      # 创建目录    

# 文件读写
with open("data.txt", "r") as f:
    content = f.read()       # 读取文件内容

with open("out.txt", "w") as f:
    f.write("Hello, file!")  # 写入文件内容

with open("data.txt") as f:  # 逐行读取
    for line in f:
        print(line.strip())

# JSON处理
import json
data = {"name": "Alice"}
json.dump(data, open("data.json", "w"))
loaded = json.load(open("data.json"))
```


## 包安装与环境管理（使用 pip）

```bash
pip install pandas          # 安装
pip install -U numpy        # 升级
pip uninstall matplotlib    # 卸载

pip list                    # 查看所有包
pip show seaborn            # 查看包信息

pip freeze > req.txt        # 导出依赖
pip install -r req.txt      # 安装依赖
```


## Jupyter & VS Code 使用技巧

### 常用 Jupyter 魔法命令（只适用于 .ipynb）

```python
%pwd                       # 显示当前路径
%cd 路径                   # 切换目录
%whos                      # 查看变量
%reset -f                  # 清空变量
%timeit sum(range(10000)) # 测试代码运行时间
```


## 基础绘图与数据分析模块（速查）

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas
df = pd.read_csv("data.csv")
df.head(), df.describe()
df["col"].mean(), df.dropna()

# numpy
a = np.array([1, 2, 3])
a.mean(), a.std(), a.shape

# matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("简单图形")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()
```


## 代码风格与注释规范

### 注释与文档字符串

```python
# 单行注释用 #
"""
多行注释可用于函数文档
"""

def add(x, y):
    """返回两个数的和"""
    return x + y
```

### 格式建议（PEP 8 简要）

* 变量名用小写加下划线：`my_variable`
* 函数名应有描述性：`def calculate_mean()`
* 运算符左右加空格：`a = b + c`
* 每行不超过 79 个字符


## 分组计算

```python
df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe()
```
