import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from matplotlib.ticker import MultipleLocator

# 创建保存结果的目录
os.makedirs("分析结果", exist_ok=True)

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

# 检查必要的列是否存在
required_columns = ['Year', 'Industry', 'Lev']
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    print(f"错误: 数据中缺少以下必要的列: {missing_columns}")
    exit(1)

# 处理年份列
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

# 筛选年份 (1998年至今)
min_year = 1998
max_year = data_filtered['year'].max()
data_years = data_filtered[(data_filtered['year'] >= min_year) & (data_filtered['year'] <= max_year)]

# 计算每个行业每年的平均负债率
avg_lev_by_industry_year = data_years.groupby(['industry_code', 'year'])['Lev'].mean().reset_index()

# 转换为透视表格式，便于绘图
lev_pivot = avg_lev_by_industry_year.pivot(index='year', columns='industry_code', values='Lev')

# 设置图表样式
plt.figure(figsize=(14, 8))
plt.style.use('ggplot')

# 设置不同行业的颜色和标记
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
markers = ['o', 's', '^', 'D', 'v', 'p', '*']

# 绘制每个行业的时序图
for i, (code, name) in enumerate(industry_mapping.items()):
    if code in lev_pivot.columns:
        plt.plot(lev_pivot.index, lev_pivot[code], 
                label=f"{name} ({code})", 
                marker=markers[i % len(markers)], 
                color=colors[i % len(colors)],
                linewidth=2,
                markersize=6)

# 添加重要时期标注
# 2007-2009年金融危机
plt.axvspan(2007, 2009, alpha=0.2, color='red', label='金融危机 (2007-2009)')
# 2020-2022年新冠疫情
plt.axvspan(2020, 2022, alpha=0.2, color='orange', label='新冠疫情 (2020-2022)')

# 设置图表标题和轴标签
plt.title('各行业年度平均负债率趋势 (1998-至今)', fontsize=16)
plt.xlabel('年份', fontsize=14)
plt.ylabel('平均负债率 (Lev)', fontsize=14)

# 设置坐标轴范围和刻度
plt.xlim(min_year-0.5, max_year+0.5)
plt.gca().xaxis.set_major_locator(MultipleLocator(2))  # 每隔2年显示一个刻度

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(loc='best', frameon=True, framealpha=0.8, fontsize=12)

# 保存图表
plt.tight_layout()
plt.savefig("分析结果/行业负债率趋势分析.png", dpi=300)
plt.savefig("分析结果/行业负债率趋势分析.pdf")  # 矢量格式，便于编辑
print("负债率趋势图已保存至: 分析结果/行业负债率趋势分析.png")

# 统计分析
print("\n各行业负债率统计分析:")
for code, name in industry_mapping.items():
    if code in lev_pivot.columns:
        industry_data = lev_pivot[code].dropna()
        
        if len(industry_data) > 0:
            avg_lev = industry_data.mean()
            max_lev = industry_data.max()
            max_year = industry_data.idxmax()
            min_lev = industry_data.min()
            min_year = industry_data.idxmin()
            
            # 计算变化率
            if len(industry_data) >= 2:
                first_year = industry_data.index[0]
                last_year = industry_data.index[-1]
                change_pct = (industry_data.iloc[-1] - industry_data.iloc[0]) / industry_data.iloc[0] * 100
                
                print(f"\n{name} ({code}):")
                print(f"  平均负债率: {avg_lev:.4f}")
                print(f"  最高负债率: {max_lev:.4f} ({max_year}年)")
                print(f"  最低负债率: {min_lev:.4f} ({min_year}年)")
                print(f"  从{first_year}年至{last_year}年变化率: {change_pct:.2f}%")
                
                # 趋势判断
                if change_pct > 5:
                    print(f"  趋势: 显著上升 (↑)")
                elif change_pct > 0:
                    print(f"  趋势: 小幅上升 (↗)")
                elif change_pct > -5:
                    print(f"  趋势: 小幅下降 (↘)")
                else:
                    print(f"  趋势: 显著下降 (↓)")

print("\n分析完成!") 