
Python 数据处理：标签文件

- myFolder：D:\Github\dsfinance\case\CSMAR\data_raw
- Files:
  - myFile1: STK_LISTEDCOINFOANL.xlsx
  - myFile2：STK_LISTEDCOINFOANL[DES][xlsx].txt

- Files 的内容：

  - myFile1 的内容样式：
```
Symbol	ShortName	EndDate	ListedCoID
股票代码	股票简称	统计截止日期	上市公司ID
没有单位	没有单位	没有单位	没有单位
000001	深发展A	2000-12-31	101704
000001	深发展A	2001-12-31	101704
``` 
    - Note: 第一行为 变量名，第二行为变量中文名，第三行为单位（没有单位则为空）。
    - 第三行的处理建议：
      - 如果单位是“没有单位”，则忽略该信息。
      - 如果单位是“万元”，则将其附加到变量中文名后，写为「变量中文名（万元）」。

  - myFile2 的内容样式：'VarName' ['变量中文名'] - '变量描述'

```{myFile2 sample data}
Symbol [股票代码] - 上交所、深交所和北交所上市的证券代码。
ShortName [股票简称] - 上交所、深交所和北交所上市上市的股票简称。
EndDate [统计截止日期] - YYYY-MM-DD。
ListedCoID [上市公司ID] - 希施玛内部编制的上市公司ID。
SecurityID [证券ID] - 希施玛内部编制的证券ID。
```

## 任务

### 任务 1：
导入 myFile1, 并将其转换为 DataFrame 对象，并命名为 STK_basic_inf。


### 任务 2：
写一段 Python 代码，把 [myFile2] 中的信息整理成两个字典
   字典 1 (dic_var_Cname)：'VarName' - '变量中文名'
   字典 2 (dic_var_Cnotes)：'VarName' - '变量描述'




3

In addition to [Karl D.'s great answer](https://stackoverflow.com/questions/23576328/any-python-library-produces-publication-style-regression-tables/23576491#23576491) with the Statsmodels `as_latex` method, you can also check out the `pystout` [package](https://github.com/lucashusted/pystout).

```
!pip install pystout

```
```
import pandas as pd
from sklearn.datasets import load_iris
import statsmodels.api as sm
from pystout import pystout

```
```
data = load_iris()
df = pd.DataFrame(data = data.data, columns = data.feature_names)
df.columns = ['s_len', 's_w', 'p_len', 'p_w']

y = df['p_w']

X = df[['s_len', 's_w', 'p_len']]
m1 = sm.OLS(y, X).fit()

X = df[['s_len', 's_w']]
m2 =  sm.OLS(y, X).fit()

X = df[['s_len']]
m3 =  sm.OLS(y, X).fit()

pystout(models=[m1, m2, m3],
        file='test_table.tex',
        addnotes=['Note above','Note below'],
        digits=2,
        endog_names=['petal width', 'petal width', 'petal width'],
        varlabels={'const':'Constant',
                   'displacement':'Disp','mpg':'MPG'},
        mgroups={'First Group':[1,2],'Second Group':3},
        modstat={'nobs':'Obs','rsquared_adj':'Adj. R\sym{2}','fvalue':'F-stat'}
        )

```

Don't spend hours like me trying to print out `pystout`. The LaTeX output is directly written on the `.tex` document you pass for `file`.

When compiled, the output looks like this:

[![Some rendered LaTeX](https://i.sstatic.net/tpDUQ.png)](https://i.sstatic.net/tpDUQ.png)