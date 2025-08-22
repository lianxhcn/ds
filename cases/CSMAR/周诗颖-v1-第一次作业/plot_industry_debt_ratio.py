import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import re
from matplotlib.font_manager import FontProperties

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

# 检查必要的列是否存在
required_columns = ['Year', 'Industry', 'Lev']
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    print(f"错误: 数据中缺少以下必要的列: {missing_columns}")
    exit(1)

# 处理年份列
# 第一行可能是中文标题，跳过
if isinstance(data['Year'].iloc[0], str) and data['Year'].iloc[0] == '年份':
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

# 筛选所需的行业
target_industries = list(industry_mapping.keys())
data_filtered = data[data['industry_code'].isin(target_industries)]

# 筛选1998年至今的数据
min_year = 1998
max_year = data_filtered['year'].max()
print(f"筛选{min_year}年至{max_year}年的数据")
data_filtered = data_filtered[(data_filtered['year'] >= min_year) & (data_filtered['year'] <= max_year)]

# 计算每个行业每年的平均杠杆率
avg_lev_by_industry = data_filtered.groupby(['industry_code', 'year'])['Lev'].mean().reset_index()

# 转换为数据透视表，用于绘图
lev_pivot = avg_lev_by_industry.pivot(index='year', columns='industry_code', values='Lev')

# 设置绘图样式
plt.figure(figsize=(14, 8))
plt.style.use('ggplot')

# 为每个行业设置不同的颜色和标记
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
markers = ['o', 's', '^', 'D', 'v', '<', '>']

# 绘制每个行业的杠杆率时序图
for i, (industry_code, industry_name) in enumerate(industry_mapping.items()):
    if industry_code in lev_pivot.columns:
        plt.plot(lev_pivot.index, lev_pivot[industry_code], 
                 label=f"{industry_name} ({industry_code})",
                 marker=markers[i % len(markers)],
                 markersize=6,
                 linewidth=2,
                 color=colors[i % len(colors)])

# 标记重要时间段
# 2007-2009金融危机
plt.axvspan(2007, 2009, alpha=0.2, color='gray')
plt.text(2008, lev_pivot.max().max() * 0.95, "金融危机\n(2007-2009)", 
         ha='center', va='top', fontsize=10, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))

# 2020-2022新冠疫情
plt.axvspan(2020, 2022, alpha=0.2, color='gray')
plt.text(2021, lev_pivot.max().max() * 0.85, "新冠疫情\n(2020-2022)", 
         ha='center', va='top', fontsize=10, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))

# 设置图表标题和轴标签
plt.title('中国各行业平均负债率时序变化(1998-至今)', fontsize=16)
plt.xlabel('年份', fontsize=12)
plt.ylabel('负债率(Lev)', fontsize=12)

# 设置x轴刻度为年份
years = sorted(lev_pivot.index.unique())
plt.xticks(years[::2])  # 每隔2年显示一次刻度，避免拥挤
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

# 添加图例，并将其放置在图表外部
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig("分析结果/行业负债率时序变化.png", dpi=300, bbox_inches='tight')
plt.savefig("分析结果/行业负债率时序变化.pdf", bbox_inches='tight')
print("已保存行业负债率时序图到文件夹: 分析结果")

# 关闭图表
plt.close()

# 统计分析
print("\n== 行业负债率统计分析 ==")

# 计算各行业平均杠杆率
industry_avg_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].mean().sort_values(ascending=False)
print("\n各行业平均负债率排名:")
for industry_code, avg_lev in industry_avg_lev.items():
    print(f"  {industry_mapping.get(industry_code, '未知')} ({industry_code}): {avg_lev:.4f}")

# 计算各行业最大和最小杠杆率
industry_max_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].max()
industry_min_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].min()

print("\n各行业负债率波动范围:")
for industry_code in industry_avg_lev.index:
    max_lev = industry_max_lev[industry_code]
    min_lev = industry_min_lev[industry_code]
    industry_name = industry_mapping.get(industry_code, '未知')
    print(f"  {industry_name} ({industry_code}): 最低 {min_lev:.4f}, 最高 {max_lev:.4f}, 波动幅度 {max_lev-min_lev:.4f}")

# 计算金融危机前后杠杆率变化
if 2006 in lev_pivot.index and 2010 in lev_pivot.index:
    print("\n金融危机前后(2006 vs 2010)负债率变化:")
    for industry_code in lev_pivot.columns:
        if pd.notna(lev_pivot.loc[2006, industry_code]) and pd.notna(lev_pivot.loc[2010, industry_code]):
            pre_crisis = lev_pivot.loc[2006, industry_code]
            post_crisis = lev_pivot.loc[2010, industry_code]
            pct_change = (post_crisis - pre_crisis) / pre_crisis * 100
            direction = "↑" if pct_change > 0 else "↓"
            industry_name = industry_mapping.get(industry_code, '未知')
            print(f"  {industry_name} ({industry_code}): {pct_change:.2f}% {direction}")

# 计算疫情前后杠杆率变化
if 2019 in lev_pivot.index and 2022 in lev_pivot.index:
    print("\n疫情前后(2019 vs 2022)负债率变化:")
    for industry_code in lev_pivot.columns:
        if pd.notna(lev_pivot.loc[2019, industry_code]) and pd.notna(lev_pivot.loc[2022, industry_code]):
            pre_covid = lev_pivot.loc[2019, industry_code]
            post_covid = lev_pivot.loc[2022, industry_code]
            pct_change = (post_covid - pre_covid) / pre_covid * 100
            direction = "↑" if pct_change > 0 else "↓"
            industry_name = industry_mapping.get(industry_code, '未知')
            print(f"  {industry_name} ({industry_code}): {pct_change:.2f}% {direction}")

# 计算负债率随时间的变化趋势 (线性回归斜率)
print("\n各行业负债率长期变化趋势:")
for industry_code in lev_pivot.columns:
    # 获取行业的时间序列数据
    series = lev_pivot[industry_code].dropna()
    if len(series) > 2:  # 确保有足够的数据点
        years = np.array(series.index, dtype=float)
        levs = np.array(series.values, dtype=float)
        
        # 简单线性回归
        slope, _ = np.polyfit(years, levs, 1)
        
        # 趋势判断
        if abs(slope) < 0.001:
            trend = "保持稳定"
        elif slope > 0:
            trend = "呈上升趋势"
        else:
            trend = "呈下降趋势"
        
        industry_name = industry_mapping.get(industry_code, '未知')
        print(f"  {industry_name} ({industry_code}): {trend} (斜率={slope:.4f})")

print("\n分析完成!") 