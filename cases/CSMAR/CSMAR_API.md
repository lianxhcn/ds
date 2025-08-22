

> [CSMAR](https://data.csmar.com/) > **服务与支持** > 数据接口文档 > Python


# CSMAR-PYTHON 使用指南

## 1. 功能介绍

CSMAR-PYTHON 是基于 Python 语言的数据接口（目前仅支持 Windows 系统），以函数调用的形式实现 CSMAR 经济金融研究数据库数据查询、下载等功能，方便用户在进行数据分析、实证研究时高效获取 CSMAR 数据，仅限个人注册账号使用。

## 2. 初始配置

### 2.1 安装 Python3.6.X 工具

1. 下载并安装 [Python3.6.X 压缩包](https://data.csmar.com/static/python_3.6.0.rar)
2. 安装以下类库：

```bash
pip install urllib3
pip install websocket
pip install websocket_client
pip install pandas
pip install prettytable
```

说明：

- `websocket` 和 `websocket_client` 类库用于实现数据传输和实时数据更新。
- `urllib3` 类库用于处理 HTTP 请求和响应，支持数据下载和上传功能。
- `pandas` 类库用于数据处理和分析，支持数据的读取、清洗和转换等操作。
- `prettytable` 系统返回数据默认格式为 JSON，可通过 `prettytable` 类库格式化展示数据。

### 2.2 CSMAR-PYTHON 安装方式

- [下载 CSMAR-PYTHON 压缩包](https://data.csmar.com/static/packages/domestic/Python/csmarapi.rar)
- 解压至 Python 安装目录下的 `\Lib\site-packages`  
  示例路径：`\Programs\Python36\Lib\site-packages`


## 3. 使用 CSMAR-PYTHON

### 3.1 基础调用

```python
from csmarapi.CsmarService import CsmarService
csmar = CsmarService()

# 启用表格展示功能
from csmarapi.ReportUtil import ReportUtil
```

### 3.2 核心函数说明

#### 3.2.1 用户登录函数：login(account, pwd, lang)

```python
login(account, pwd, lang)
```

**参数说明：**
- `account`: 用户名/已验证电话/已验证邮箱
- `pwd`: 密码
- `lang`: 语言选项（0=中文，1=英文，默认0）

**示例：**
```python
account = '134******83'
pwd     = 'a*****c'

csmar.login(account, pwd)  # 中文登录
csmar.login(account, pwd, '1')  # 英文登录
```

#### 3.2.2 查看已购数据库：getListDbs()

**示例：**
```python
database = csmar.getListDbs()
ReportUtil(database)
```

#### 3.2.3 查看数据表：getListTables(databaseName)

**参数说明：**
- `databaseName`: 数据库名称（通过 `getListDbs()` 获取）

**示例：**
```python
tables = csmar.getListTables('股票市场交易')
ReportUtil(tables)
```

#### 3.2.4 查看表字段：getListFields(tableName)

**参数说明：**
- `tableName`: 数据表名称（通过 `getListTables()` 获取）

**示例：**
```python
fields = csmar.getListFields('Trd_Co')
ReportUtil(fields)
```

#### 3.2.5 数据预览：preview(tableName)

**示例：**
```python
data = csmar.preview('TRD_Co')
ReportUtil(data)
```

#### 3.2.6 记录数查询：queryCount()

```python
queryCount(columns, condition, tableName, startTime, endTime)
```

**参数说明：**
- `columns`: 字段列表（如 `['Cuntrycd','Stkcd']`）
- `condition`: 查询条件（类似 SQL WHERE 子句）
- `tableName`: 数据表名称
- `startTime/endTime`: 时间范围（格式：YYYY-MM-DD）

**示例：**
```python
csmar.queryCount(['Cuntrycd','Stkcd'], "Stkcd like'3%'", 'TRD_Co')
```

#### 3.2.7 数据查询

**JSON 格式返回：**
```python
query(columns, condition, tableName, startTime, endTime)
```

**DataFrame 格式返回：**
```python
query_df(columns, condition, tableName, startTime, endTime)
```

**注意事项：**
- 单次最多加载 200,000 条记录
- 分页查询需使用 `limit` 子句（如 `"Stkcd like'3%' limit 0,200000"`）
- 相同查询条件 30 分钟内仅允许执行一次

**示例：**
```python
# JSON 格式
data = csmar.query(['Cuntrycd','Stkcd'], "Stkcd like'3%'", 'TRD_Co')
ReportUtil(data)

# DataFrame 格式
data = csmar.query_df(['Cuntrycd','Stkcd'], "Stkcd like'3%'", 'TRD_Co')
print(data)
```

#### 3.2.8 数据下载：getPackResultExt()

```python
getPackResultExt(columns, 
                 condition, 
                 tableName, 
                 startTime, 
                 endTime)
```

**示例：**

```python
data = csmar.getPackResultExt(['Cuntrycd','Stkcd'], "Stkcd like'3%'", 'TRD_Co')
ReportUtil(data)
```

#### 3.2.9 数据解压：unzipSingle(filePath)

**参数说明：**
- `filePath`: 压缩包绝对路径（默认存储于 `C:\csmardata\zip\`）

**示例：**
```python
csmar.unzipSingle('c:\\csmardata\\zip\\778639194952077312.zip')
```

#### 3.2.10 数据加载：loadData(filePath, count)

**参数说明：**
- `filePath`: 解压文件路径（默认在 `C:\csmardata\` 下）
- `count`: 加载数据条数（可选）

**示例：**
```python
csmar.loadData('c:\\csmardata\\778639194952077312\\TRD_Co.csv')
```

## 4. 完整示例

### 4.1 基础查询流程

```python
from csmarapi.CsmarService import CsmarService
from csmarapi.ReportUtil import ReportUtil

csmar = CsmarService()
csmar.login('134******83', 'a*****c')
data = csmar.query(
    ['Cuntrycd','Stkcd','Stknme','Conme'],
    "Stkcd like'0%' or Stkcd like'6%'",
    'TRD_Co'
)
ReportUtil(data)
```

### 4.2 查询结果示例
![示例结果](https://data.csmar.com/static/document/image-python001.png)
