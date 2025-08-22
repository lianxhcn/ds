import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

# 尝试设置中文字体
try:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
except:
    print("警告: 未能正确设置中文字体，图表中的中文可能无法正确显示")

# 读取Excel文件
print("正在读取数据文件...")
try:
    data = pd.read_excel("金融数据分析.xlsx")
    print("数据读取成功！")
except Exception as e:
    print(f"读取数据时出错: {e}")
    exit(1)

# 显示数据的基本信息
print(f"数据行数: {data.shape[0]}, 数据列数: {data.shape[1]}")
print("\n数据列名:")
print(data.columns.tolist())

# 处理年份列
if 'Year' in data.columns:
    # 第一行可能是中文标题，跳过
    if data['Year'].iloc[0] == '年份':
        data = data.iloc[1:].reset_index(drop=True)
    
    # 确保Year列是数值类型
    try:
        data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
        data = data.dropna(subset=['Year'])  # 删除年份为空的行
        data['year'] = data['Year'].astype(int)  # 创建一个年份的整数列
    except Exception as e:
        print(f"转换年份时出错: {e}")
        print("尝试手动检查年份数据...")
        print(data['Year'].head(10))  # 打印前10条年份数据进行检查

# 行业代码映射
industry_mapping = {
    'C': '制造业',
    'D': '电力、热力、燃气及水生产和供应业',
    'G': '交通运输业',
    'E': '建筑业',
    'K': '房地产业',
    'F': '批发和零售业',
    'J': '金融业'
}

# 处理行业代码列
if 'Industry' in data.columns:
    # 提取证监会行业分类主代码 (假设格式为字母+数字，如C39)
    def extract_industry_code(code):
        if pd.isna(code):
            return np.nan
        match = re.match(r'([A-Z])', str(code))
        if match:
            return match.group(1)
        return np.nan
    
    data['industry_code'] = data['Industry'].apply(extract_industry_code)
    print("\n行业代码分布:")
    print(data['industry_code'].value_counts())

# 筛选所需的行业
target_industries = list(industry_mapping.keys())
data_filtered = data[data['industry_code'].isin(target_industries)]

# 生成奇数年份列表 (从1999开始的奇数年)
selected_years = range(1999, data_filtered['year'].max() + 1, 2)
print(f"\n选定的年份: {list(selected_years)}")

# 选择要分析的指标
indicators = ['SLoan', 'LLoan', 'Lev', 'Cash', 'ROA', 'ROE']

# 检查指标是否在数据中存在
missing_indicators = [ind for ind in indicators if ind not in data_filtered.columns]
if missing_indicators:
    print(f"警告: 以下指标在数据中不存在: {missing_indicators}")
    indicators = [ind for ind in indicators if ind in data_filtered.columns]

# 筛选选定年份的数据
data_selected_years = data_filtered[data_filtered['year'].isin(selected_years)]

# 检查数据
print(f"\n筛选后数据行数: {data_selected_years.shape[0]}")
print(f"年份分布: \n{data_selected_years['year'].value_counts().sort_index()}")
print(f"行业分布: \n{data_selected_years['industry_code'].value_counts()}")

# 为每个指标创建数据表
tables = {}

for indicator in indicators:
    if indicator in data_selected_years.columns:
        # 计算每个行业在选定年份的指标平均值
        industry_year_avg = data_selected_years.groupby(['industry_code', 'year'])[indicator].mean().unstack()
        
        # 将行业代码转换为行业名称
        industry_year_avg.index = industry_year_avg.index.map(lambda x: f"{industry_mapping.get(x, '未知')} ({x})")
        
        # 存储结果
        tables[indicator] = industry_year_avg
        
        print(f"\n{indicator} 各行业年度平均值:")
        print(industry_year_avg)
        
        # 保存到CSV
        output_path = f"分析结果/{indicator}_行业年度平均值.csv"
        industry_year_avg.to_csv(output_path)
        print(f"{indicator}行业年度平均值已保存至: {output_path}")
    else:
        print(f"警告: {indicator}不在数据列中，跳过")

# 创建一个包含所有指标的Excel文件
print("\n创建总表...")
with pd.ExcelWriter("分析结果/行业财务指标分析.xlsx") as writer:
    for indicator, table in tables.items():
        table.to_excel(writer, sheet_name=indicator)
    
    # 创建一个概览表
    overview = pd.DataFrame(index=[f"{industry_mapping.get(ind, '未知')} ({ind})" for ind in target_industries if ind in data_selected_years['industry_code'].unique()])
    
    # 计算各指标的总平均值
    for indicator in indicators:
        if indicator in tables:
            indicator_avg = data_selected_years.groupby('industry_code')[indicator].mean()
            indicator_avg.index = indicator_avg.index.map(lambda x: f"{industry_mapping.get(x, '未知')} ({x})")
            overview[f"{indicator}_平均值"] = indicator_avg
    
    overview.to_excel(writer, sheet_name="概览")

print("行业财务指标分析总表已保存至: 分析结果/行业财务指标分析.xlsx")

# 行业指标比较分析
print("\n行业指标比较分析:")

# 1. 负债结构分析 (SLoan, LLoan, Lev)
print("\n1. 负债结构分析:")
debt_indicators = ['SLoan', 'LLoan', 'Lev']
debt_avail = [ind for ind in debt_indicators if ind in tables]

if debt_avail:
    # 计算各行业的整体平均值
    industry_debt_avg = {ind: data_selected_years.groupby('industry_code')[ind].mean() for ind in debt_avail}
    
    # 将结果合并为一个表格
    debt_df = pd.DataFrame({f"{ind}_平均值": avg for ind, avg in industry_debt_avg.items()})
    debt_df.index = debt_df.index.map(lambda x: f"{industry_mapping.get(x, '未知')} ({x})")
    
    # 排序并打印结果
    for ind in debt_avail:
        sorted_ind = debt_df[f"{ind}_平均值"].sort_values(ascending=False)
        print(f"\n{ind} 行业排名:")
        for industry, value in sorted_ind.items():
            print(f"{industry}: {value:.4f}")

# 2. 盈利能力分析 (ROA, ROE)
print("\n2. 盈利能力分析:")
profit_indicators = ['ROA', 'ROE']
profit_avail = [ind for ind in profit_indicators if ind in tables]

if profit_avail:
    # 计算各行业的整体平均值
    industry_profit_avg = {ind: data_selected_years.groupby('industry_code')[ind].mean() for ind in profit_avail}
    
    # 将结果合并为一个表格
    profit_df = pd.DataFrame({f"{ind}_平均值": avg for ind, avg in industry_profit_avg.items()})
    profit_df.index = profit_df.index.map(lambda x: f"{industry_mapping.get(x, '未知')} ({x})")
    
    # 排序并打印结果
    for ind in profit_avail:
        sorted_ind = profit_df[f"{ind}_平均值"].sort_values(ascending=False)
        print(f"\n{ind} 行业排名:")
        for industry, value in sorted_ind.items():
            print(f"{industry}: {value:.4f}")

# 3. 流动性分析 (Cash)
print("\n3. 流动性分析:")
if 'Cash' in tables:
    cash_avg = data_selected_years.groupby('industry_code')['Cash'].mean()
    cash_avg.index = cash_avg.index.map(lambda x: f"{industry_mapping.get(x, '未知')} ({x})")
    
    sorted_cash = cash_avg.sort_values(ascending=False)
    print("\nCash 行业排名:")
    for industry, value in sorted_cash.items():
        print(f"{industry}: {value:.4f}")

# 4. 趋势分析
print("\n4. 各指标趋势分析:")
for indicator in indicators:
    if indicator in tables:
        print(f"\n{indicator} 趋势变化:")
        for industry in tables[indicator].index:
            ind_data = tables[indicator].loc[industry].dropna()
            if len(ind_data) >= 2:
                first_year = ind_data.index[0]
                last_year = ind_data.index[-1]
                first_val = ind_data.iloc[0]
                last_val = ind_data.iloc[-1]
                change_pct = (last_val - first_val) / abs(first_val) * 100 if first_val != 0 else float('inf')
                
                print(f"{industry}: {first_year}年({first_val:.4f}) 至 {last_year}年({last_val:.4f}), 变化率: {change_pct:.2f}%")

print("\n分析完成!") 