# Python：import 使用详解

## 引言

对于 Python 初学者来说，经常会在代码的前几行看到如下语句：

```python
import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
```

这时候，初学者往往会产生疑问：这些语句的作用是什么？为什么有时会看到很多类似的 `import` 语句？我如何知道自己需要导入哪些包？这些包到底是从哪里来的？它们如何帮助我实现特定的功能？

在本篇讲义中，我们将深入探讨 `import` 语句的使用，特别是如何通过导入模块和包，来扩展 Python 的功能，避免重复编写代码，提高开发效率。

通过实践，初学者可以逐渐掌握如何根据自己的需求，导入所需的库和模块，从而让自己的代码变得更加简洁且高效。

## 什么是模块、包和函数？

**函数 (Function)**

在 Python 中，函数是程序的基本组成部分。函数是一段执行特定任务的代码，可以接收输入并返回输出。函数是我们编写高效、简洁代码的重要工具。

例如，`math.sqrt()` 是 Python 标准库中的一个函数，用于计算平方根。它是一个模块中的一个功能。

**模块 (Module)**

模块是一个包含 Python 代码的文件，通常是一个 `.py` 文件。一个模块可以包含多个函数、类和变量，用来实现特定的功能。模块是对功能的封装，可以提高代码的可维护性和可复用性。

例如，`math` 是一个标准库模块，它包含了许多数学计算相关的函数，如 `sqrt()`、`sin()`、`cos()` 等。

**包 (Package)**

包是一个包含多个模块的目录。包可以将相关的模块组织在一起，方便管理和使用。每个包目录中都会包含一个特殊的 `__init__.py` 文件，它标识该目录是一个包。

例如，`numpy` 是一个非常常见的 Python 包，它包含多个子模块（如 `numpy.linalg` 用于线性代数运算，`numpy.fft` 用于傅里叶变换等）。

**函数、模块和包之间的关系**

为了更好地理解函数、模块和包之间的关系，下面是一个结构图：

```
Package (包)
    ├── Module (模块)
    │     ├── Function (函数)
    │     ├── Function (函数)
    │     └── Class (类)
    ├── Module (模块)
    └── __init__.py
```

在上图中，我们可以看到：
- **包（Package）** 是由多个 **模块（Module）** 组成的文件夹。
- 每个 **模块（Module）** 内部可以包含多个 **函数（Function）**，也可以包含 **类（Class）**。
- **函数** 是模块中的功能实现，它通常执行某一具体的任务。


## import 语句：基本用法

### 导入整个模块
最常见的方式是导入整个模块：

```python
import math
```

这样我们就可以使用 `math` 模块中的所有函数，如 `math.sqrt()`、`math.sin()` 等。

### 给模块起别名
为了提高代码的可读性和简洁性，我们通常给模块起一个别名，尤其是对于较长的模块名。例如，`numpy` 可以用 `np` 作为别名：

```python
import numpy as np
```

之后，我们可以通过 `np` 来引用 `numpy` 中的函数或类：

```python
arr = np.array([1, 2, 3])
print(arr)
```

### 从模块中导入特定函数
如果只需要模块中的特定功能，可以直接导入所需的函数：

```python
from math import sqrt
```

此时，我们可以直接使用 `sqrt()` 函数，而不需要再写 `math.sqrt()`。


## import 的机制

### 导入的背后：存储和内存

当你导入一个模块时，Python 会从其存储位置加载模块的代码到内存中，之后在内存中执行。对于标准库模块（如 `math`），它们已经随着 Python 安装包一起安装在你的电脑上，而第三方包（如 `numpy`、`yfinance` 等）需要通过 `pip` 或 `conda` 等工具安装，并通过 `import` 语句加载到内存中。

### 为什么需要 import？

很多初学者会问：“我已经安装了 `yfinance` 这个包，它已经在我的电脑上了，为什么每次使用时还要写 `import yfinance as yf`？”这是因为安装包并不会自动加载到 Python 的工作环境中。每次执行代码时，我们都需要明确告诉 Python 哪些功能是我们需要使用的，而 `import` 就是告诉 Python 去哪里找这些功能。`import` 将模块或包加载到内存中，以便在运行时使用。

### 如何查看已安装包的存储位置？

对于初学者来说，了解自己安装的包存储在哪里，有助于理解模块的导入机制。假设我们想查看 `numpy` 包的存储路径，可以使用以下 Python 命令：

```python
import numpy
print(numpy.__file__)
```

这将输出 `numpy` 包的文件路径，类似于：

```
C:\ProgramData\anaconda3\Lib\site-packages\numpy
```

在该路径下，你会看到 `numpy` 包的所有文件和子目录，包含了该包的源码、配置文件等。

### 目录结构
我们可以通过 `dir` 命令查看该路径下的所有文件。例如：

```python
import os
print(os.listdir(r'C:\ProgramData\anaconda3\Lib\site-packages\numpy'))
```

你还可以使用 `tree` 命令（如果安装了 `tree` 工具）以树形结构显示目录内容：

```
C:\ProgramData\anaconda3\Lib\site-packages\numpy
├── core
│   ├── arrayobject.py       <- 用于数组操作的模块
│   ├── umath.py             <- 数学运算模块
│   └── ...
├── linalg
│   ├── linalg.py            <- 线性代数运算模块
│   └── ...
└── __init__.py              <- 初始化文件
```

### 从模块中导入特定函数的好处

通过 `from module import function` 语句，我们可以只导入模块中的某个函数或类，而不是整个模块。这带来了几个好处：
- **减少内存消耗**：只加载需要的部分，避免不必要的内存开销。
- **简化代码**：导入函数后，我们可以直接使用函数名称，避免在代码中重复书写模块名。

例如，从 `math` 模块中只导入 `sqrt` 函数：

```python
from math import sqrt
print(sqrt(25))  # 直接使用 sqrt 函数
```

## import 语句：高级用法

### 动态导入
在某些情况下，我们可能需要在运行时根据条件来导入模块，这时可以使用 `importlib`：

```python
import importlib

numpy = importlib.import_module('numpy')
print(numpy.array([1, 2, 3]))
```

### 按需加载
虽然通常情况下我们会在代码开始时导入所有需要的库，但在某些特殊情况下，按需加载可以提高代码的性能。例如：

```python
def some_function():
    import numpy as np
    # 使用 numpy 库进行操作
```

这种方式可以避免在程序启动时加载不必要的库，但对于大多数用户来说，在文件开始部分就加载所有需要的包更直观。

## 总结与建议

在 Python 中，`import` 语句是非常重要的，它帮助我们将模块化的代码引入到程序中，提升代码的可重用性和模块化程度。我们可以通过导入整个模块、给模块起别名、从模块中导入特定功能等方式灵活地使用模块。

在使用 `import` 时，我们需要根据实际需求选择合适的导入方式，避免命名冲突，并理解 `import` 是如何将模块加载到内存中的。继续实践并探索更多 Python 内置和第三方模块的使用，将会帮助你写出更简洁、可维护的代码。

## 参考资料

以下是与本讲义直接相关的一些链接，供读者扩展阅读：

1. [Python 官方文档 - 模块](https://docs.python.org/3/tutorial/modules.html)
2. [numpy 官方文档](https://numpy.org/doc/stable/)
3. [Python 中的包和模块概念](https://realpython.com/python-modules-packages/)


## 附录：提示词

::: {.callout-tip}
## 提示词

### Prompt 1

- 写一篇讲义，主题：Python 中的 import 使用详解。
- 读者：初学者，对 Python 几乎一无所知
- 语言风格：朴实，严谨。一个从事多年 Python 教学的教授所写

你先帮我介绍一个提纲和思路，我修改确认后再开始写

### Prompt 2

补充：

1. 为了让初学者有个直观的感受，能否以 numpy 包为例，介绍其存储位置，以及文件夹中的内>容。我的路径为「C:\ProgramData\anaconda3\Lib\site-packages\numpy」，你可以在讲义中>介绍一些 Python 命令，以便读者能够获取它的电脑中的路径。总之，要提供一些指引，让读者能>够看到这个文件夹下的内容。也可以用 dir tree 结构图来呈现。似乎可以用 `sys.path` 命>令。
2. 「引言」部分，可以采用更有趣的导入方式，比如：对于 Python 初学者而言，经常看到代码>的前几行会出现如下语句：

```python
import numpy as np
import yfinance as yf
……
```

不免产生如下疑问：这些语句的作用是什么？我如何知道我该 import 哪些 packages？……

1. 「2. 什么是模块和包？」部分：可以先介绍一下 function 的概念，这是 Python 的基本元>素，然后再介绍更高阶的内容，这样读者更容易理解诸如 np.arry,  os.getcwd () 这样的表达>式
2. 有一个重要的问题是：很多人认为，我已经 install 了 yfinance package，它已经存储在了>我的电脑上；另外， 诸如 math 这样的标准库模块，在我安装 Python 后 Anocanda 的时候就自>动安装在我的电脑中了，为何我用的时候还需要 import yfinance？你要在讲义的合适位置讲一下>这个问题。可能需要讲一下，import numpy 把【什么文件】导入到了【什么位置】（内存？），>这种做法的好处是什么？
3. 「4.3 从模块中导入特定函数」部分，这种做法的好处是什么？
4. 「6.2 按需加载」最好补充一个例子。不过，我猜测对于多数用户而言，这个问题并不重要。反>而是在文件开头部分就载入所有 packages 可以让代码更直观？
  
### Prompt 3

修改：
在「2. 什么是模块、包和函数？」部分，能否增加一个 结构图，更直观地展示 函数，模块和 package 之间的关系
  
### Prompt 4

很好，整合成一个完整的文档。
在结尾处提供 2-3 个与本讲义直接相关的链接，以便读者扩展阅读
:::