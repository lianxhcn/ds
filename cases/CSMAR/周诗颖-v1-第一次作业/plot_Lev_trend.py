import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 尝试设置中文字体
try:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 尝试多种中文字体
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
except:
    print("警告: 未能正确设置中文字体，图表中的中文可能无法正确显示")

# 读取Lev指标的统计数据
data_path = '分析结果/Lev_年度统计.csv'
if os.path.exists(data_path):
    df = pd.read_csv(data_path, index_col=0)
else:
    print(f"错误: 找不到文件 {data_path}")
    exit(1)

# 绘制Lev的均值和中位数时序图
plt.figure(figsize=(12, 8))

# 绘制均值曲线
plt.plot(df.index, df['平均值'], 'b-o', linewidth=2, markersize=6, label='平均值')

# 绘制中位数曲线
plt.plot(df.index, df['中位数'], 'r--s', linewidth=2, markersize=6, label='中位数')

# 添加图表元素
plt.title('总负债率(Lev)年度变化趋势 (2000-2024)', fontsize=16)
plt.xlabel('年份', fontsize=14)
plt.ylabel('总负债率 (Lev)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 优化X轴显示
plt.xticks(rotation=45)

# 添加数据标签
for i, (mean_val, median_val) in enumerate(zip(df['平均值'], df['中位数'])):
    if i % 3 == 0:  # 每隔3年显示一次标签，避免过度拥挤
        plt.text(df.index[i], mean_val, f'{mean_val:.3f}', fontsize=9, 
                 ha='center', va='bottom')

# 标记重要时期
important_periods = [
    (2007, 2009, 'r', '金融危机'),
    (2020, 2022, 'y', 'COVID-19疫情')
]

for start, end, color, label in important_periods:
    if start in df.index and end in df.index:
        start_idx = df.index.get_loc(start)
        end_idx = df.index.get_loc(end)
        plt.axvspan(df.index[start_idx], df.index[end_idx], alpha=0.2, color=color, label=label)

# 计算和显示趋势
first_year, last_year = df.index[0], df.index[-1]
first_mean, last_mean = df['平均值'].iloc[0], df['平均值'].iloc[-1]
change_pct = (last_mean - first_mean) / first_mean * 100
trend_text = f"整体趋势: {first_year}年至{last_year}年期间，总负债率均值从{first_mean:.3f}变化到{last_mean:.3f}，变化率为{change_pct:.2f}%"

# 添加趋势文本
plt.figtext(0.5, 0.01, trend_text, ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# 调整布局并保存
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.savefig('分析结果/Lev_均值中位数趋势分析.png', dpi=300, bbox_inches='tight')
print("Lev趋势图已保存至: 分析结果/Lev_均值中位数趋势分析.png")

# 简要分析
print("\n总负债率(Lev)趋势分析:")
print(f"1. 整体趋势: 从{first_year}年至{last_year}年，总负债率均值从{first_mean:.4f}变化到{last_mean:.4f}，变化率为{change_pct:.2f}%")

# 计算峰谷值及其年份
max_mean_year = df['平均值'].idxmax()
min_mean_year = df['平均值'].idxmin()
max_mean = df['平均值'].max()
min_mean = df['平均值'].min()

print(f"2. 峰值出现在{max_mean_year}年，为{max_mean:.4f}；谷值出现在{min_mean_year}年，为{min_mean:.4f}")

# 分析特殊时期
crisis_years = [y for y in df.index if 2007 <= y <= 2009]
pre_crisis_years = [y for y in df.index if 2004 <= y <= 2006]
covid_years = [y for y in df.index if 2020 <= y <= 2022]
pre_covid_years = [y for y in df.index if 2017 <= y <= 2019]

if crisis_years and pre_crisis_years:
    crisis_mean = df.loc[crisis_years, '平均值'].mean()
    pre_crisis_mean = df.loc[pre_crisis_years, '平均值'].mean()
    crisis_change = (crisis_mean - pre_crisis_mean) / pre_crisis_mean * 100
    print(f"3. 金融危机影响: 金融危机期间(2007-2009)总负债率均值为{crisis_mean:.4f}，比危机前(2004-2006)的{pre_crisis_mean:.4f}变化了{crisis_change:.2f}%")

if covid_years and pre_covid_years:
    covid_mean = df.loc[covid_years, '平均值'].mean()
    pre_covid_mean = df.loc[pre_covid_years, '平均值'].mean()
    covid_change = (covid_mean - pre_covid_mean) / pre_covid_mean * 100
    print(f"4. 疫情影响: 疫情期间(2020-2022)总负债率均值为{covid_mean:.4f}，比疫情前(2017-2019)的{pre_covid_mean:.4f}变化了{covid_change:.2f}%")

# 分析均值与中位数的差异
mean_median_diff = df['平均值'] - df['中位数']
max_diff_year = mean_median_diff.abs().idxmax()
max_diff = mean_median_diff[max_diff_year]
print(f"5. 均值与中位数差异: 差异最大的年份是{max_diff_year}年，均值比中位数{'高' if max_diff > 0 else '低'}{abs(max_diff):.4f}")
print("   均值高于中位数表明负债率分布右偏，部分企业的高负债率拉高了整体均值")

print("\n分析完成!") 