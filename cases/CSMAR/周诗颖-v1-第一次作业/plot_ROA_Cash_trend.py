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

# 读取ROA和Cash指标的统计数据
roa_path = '分析结果/ROA_年度统计.csv'
cash_path = '分析结果/Cash_年度统计.csv'

if not os.path.exists(roa_path) or not os.path.exists(cash_path):
    print(f"错误: 找不到必要的文件 {roa_path} 或 {cash_path}")
    exit(1)

roa_df = pd.read_csv(roa_path, index_col=0)
cash_df = pd.read_csv(cash_path, index_col=0)

# 确保两个数据框有相同的索引
common_years = sorted(set(roa_df.index).intersection(set(cash_df.index)))
roa_df = roa_df.loc[common_years]
cash_df = cash_df.loc[common_years]

# 创建双Y轴图表
fig, ax1 = plt.subplots(figsize=(14, 8))

# 第一个Y轴: ROA
color1 = 'tab:blue'
ax1.set_xlabel('年份', fontsize=14)
ax1.set_ylabel('总资产收益率 (ROA)', color=color1, fontsize=14)
line1 = ax1.plot(roa_df.index, roa_df['平均值'], 'o-', color=color1, linewidth=2.5, markersize=8, label='ROA均值')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle='--', alpha=0.3)

# 第二个Y轴: Cash
ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('现金比率 (Cash)', color=color2, fontsize=14)
line2 = ax2.plot(cash_df.index, cash_df['平均值'], 's--', color=color2, linewidth=2.5, markersize=8, label='Cash均值')
ax2.tick_params(axis='y', labelcolor=color2)

# 标记重要时期
important_periods = [
    (2007, 2009, 'lightcoral', '金融危机'),
    (2020, 2022, 'lightyellow', 'COVID-19疫情')
]

for start, end, color, label in important_periods:
    if start in common_years and end in common_years:
        start_idx = common_years.index(start)
        end_idx = common_years.index(end)
        ax1.axvspan(common_years[start_idx], common_years[end_idx], alpha=0.3, color=color, label=label)

# 添加图表标题和图例
plt.title('总资产收益率(ROA)与现金比率(Cash)年度变化趋势对比 (2000-2024)', fontsize=16)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', fontsize=12)

# 优化X轴显示
plt.xticks(rotation=45)

# 添加数据标签
for i, (roa_val, cash_val) in enumerate(zip(roa_df['平均值'], cash_df['平均值'])):
    if i % 3 == 0:  # 每隔3年显示一次标签，避免过度拥挤
        ax1.text(common_years[i], roa_val, f'{roa_val:.3f}', fontsize=9, 
                 ha='center', va='bottom', color=color1)
        ax2.text(common_years[i], cash_val, f'{cash_val:.3f}', fontsize=9, 
                 ha='center', va='bottom', color=color2)

# 计算和显示趋势
roa_first_year, roa_last_year = common_years[0], common_years[-1]
roa_first_mean, roa_last_mean = roa_df['平均值'].iloc[0], roa_df['平均值'].iloc[-1]
roa_change_pct = (roa_last_mean - roa_first_mean) / abs(roa_first_mean) * 100 if roa_first_mean != 0 else float('inf')
roa_trend = f"ROA变化趋势: {roa_first_year}年至{roa_last_year}年间从{roa_first_mean:.3f}{'增加' if roa_change_pct > 0 else '减少'}至{roa_last_mean:.3f}，变化率{abs(roa_change_pct):.2f}%"

cash_first_mean, cash_last_mean = cash_df['平均值'].iloc[0], cash_df['平均值'].iloc[-1]
cash_change_pct = (cash_last_mean - cash_first_mean) / abs(cash_first_mean) * 100 if cash_first_mean != 0 else float('inf')
cash_trend = f"Cash变化趋势: {roa_first_year}年至{roa_last_year}年间从{cash_first_mean:.3f}{'增加' if cash_change_pct > 0 else '减少'}至{cash_last_mean:.3f}，变化率{abs(cash_change_pct):.2f}%"

# 添加趋势文本
plt.figtext(0.01, 0.01, roa_trend, ha='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.8), color=color1)
plt.figtext(0.01, 0.04, cash_trend, ha='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.8), color=color2)

# 添加相关性分析
corr = np.corrcoef(roa_df['平均值'], cash_df['平均值'])[0,1]
corr_text = f"ROA与Cash相关系数: {corr:.3f}"
plt.figtext(0.99, 0.01, corr_text, ha='right', fontsize=11, bbox=dict(facecolor='white', alpha=0.8))

# 调整布局并保存
plt.tight_layout(rect=[0, 0.07, 1, 0.97])
plt.savefig('分析结果/ROA_Cash_均值趋势对比.png', dpi=300, bbox_inches='tight')
print("ROA与Cash趋势对比图已保存至: 分析结果/ROA_Cash_均值趋势对比.png")

# 生成分析报告
print("\nROA与Cash趋势分析:")
print(f"1. ROA趋势: 从{roa_first_year}年至{roa_last_year}年，ROA均值从{roa_first_mean:.4f}{'增加' if roa_change_pct > 0 else '减少'}到{roa_last_mean:.4f}，变化率为{abs(roa_change_pct):.2f}%")
print(f"2. Cash趋势: 从{roa_first_year}年至{roa_last_year}年，Cash均值从{cash_first_mean:.4f}{'增加' if cash_change_pct > 0 else '减少'}到{cash_last_mean:.4f}，变化率为{abs(cash_change_pct):.2f}%")

# 计算峰谷值及其年份
roa_max_year = roa_df['平均值'].idxmax()
roa_min_year = roa_df['平均值'].idxmin()
roa_max = roa_df['平均值'].max()
roa_min = roa_df['平均值'].min()

cash_max_year = cash_df['平均值'].idxmax()
cash_min_year = cash_df['平均值'].idxmin()
cash_max = cash_df['平均值'].max()
cash_min = cash_df['平均值'].min()

print(f"3. ROA峰值出现在{roa_max_year}年，为{roa_max:.4f}；谷值出现在{roa_min_year}年，为{roa_min:.4f}")
print(f"4. Cash峰值出现在{cash_max_year}年，为{cash_max:.4f}；谷值出现在{cash_min_year}年，为{cash_min:.4f}")

# 分析特殊时期
crisis_years = [y for y in common_years if 2007 <= y <= 2009]
pre_crisis_years = [y for y in common_years if 2004 <= y <= 2006]
covid_years = [y for y in common_years if 2020 <= y <= 2022]
pre_covid_years = [y for y in common_years if 2017 <= y <= 2019]

if crisis_years and pre_crisis_years:
    roa_crisis_mean = roa_df.loc[crisis_years, '平均值'].mean()
    roa_pre_crisis_mean = roa_df.loc[pre_crisis_years, '平均值'].mean()
    roa_crisis_change = (roa_crisis_mean - roa_pre_crisis_mean) / abs(roa_pre_crisis_mean) * 100
    
    cash_crisis_mean = cash_df.loc[crisis_years, '平均值'].mean()
    cash_pre_crisis_mean = cash_df.loc[pre_crisis_years, '平均值'].mean()
    cash_crisis_change = (cash_crisis_mean - cash_pre_crisis_mean) / abs(cash_pre_crisis_mean) * 100
    
    print(f"5. 金融危机影响:")
    print(f"   - ROA: 金融危机期间(2007-2009)均值为{roa_crisis_mean:.4f}，比危机前(2004-2006)的{roa_pre_crisis_mean:.4f}{'增加' if roa_crisis_change > 0 else '减少'}{abs(roa_crisis_change):.2f}%")
    print(f"   - Cash: 金融危机期间(2007-2009)均值为{cash_crisis_mean:.4f}，比危机前(2004-2006)的{cash_pre_crisis_mean:.4f}{'增加' if cash_crisis_change > 0 else '减少'}{abs(cash_crisis_change):.2f}%")

if covid_years and pre_covid_years:
    roa_covid_mean = roa_df.loc[covid_years, '平均值'].mean()
    roa_pre_covid_mean = roa_df.loc[pre_covid_years, '平均值'].mean()
    roa_covid_change = (roa_covid_mean - roa_pre_covid_mean) / abs(roa_pre_covid_mean) * 100
    
    cash_covid_mean = cash_df.loc[covid_years, '平均值'].mean()
    cash_pre_covid_mean = cash_df.loc[pre_covid_years, '平均值'].mean()
    cash_covid_change = (cash_covid_mean - cash_pre_covid_mean) / abs(cash_pre_covid_mean) * 100
    
    print(f"6. 疫情影响:")
    print(f"   - ROA: 疫情期间(2020-2022)均值为{roa_covid_mean:.4f}，比疫情前(2017-2019)的{roa_pre_covid_mean:.4f}{'增加' if roa_covid_change > 0 else '减少'}{abs(roa_covid_change):.2f}%")
    print(f"   - Cash: 疫情期间(2020-2022)均值为{cash_covid_mean:.4f}，比疫情前(2017-2019)的{cash_pre_covid_mean:.4f}{'增加' if cash_covid_change > 0 else '减少'}{abs(cash_covid_change):.2f}%")

# 分析ROA与Cash的关系
print(f"7. ROA与Cash相关性:")
print(f"   - 相关系数: {corr:.4f}")
relationship_text = "正相关" if corr > 0 else "负相关" if corr < 0 else "几乎无相关"
strength_text = "强" if abs(corr) > 0.7 else "中等" if abs(corr) > 0.4 else "弱"
print(f"   - 两者呈{strength_text}{relationship_text}关系，表明" + 
      ("企业盈利能力与现金持有量变化趋势基本一致" if corr > 0.7 else
       "企业盈利能力与现金持有量存在一定关联" if corr > 0.4 and corr > 0 else
       "企业在盈利下降时倾向于增加现金持有以应对风险" if corr < -0.4 else
       "企业盈利能力与现金持有量之间关系不明显"))

# 讨论资产配置效率
if corr > 0:
    print("8. 资产配置效率分析: ROA与Cash呈正相关关系，表明企业整体现金管理与企业盈利能力相匹配，高盈利时保持更多现金储备，体现了较为稳健的财务策略")
else:
    print("8. 资产配置效率分析: ROA与Cash呈负相关或弱相关关系，可能表明企业在盈利下降时增加现金持有以应对风险，或在盈利良好时减少现金持有转而进行更多投资")

print("\n分析完成!") 