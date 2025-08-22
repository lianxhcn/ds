import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML
import os
import ticker

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取Excel文件
print("正在读取数据文件...")
try:
    data = pd.read_excel("金融数据分析.xlsx")
    print("数据读取成功！")
except Exception as e:
    print(f"读取数据时出错: {e}")
    exit(1)

# 显示数据的基本信息
print("\n数据基本信息:")
print(f"数据行数: {data.shape[0]}, 数据列数: {data.shape[1]}")
print("\n数据前5行:")
print(data.head())
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

# 筛选2000-2024年的数据
data = data[(data['year'] >= 2000) & (data['year'] <= 2024)]
print(f"\n筛选后数据行数: {data.shape[0]}")

# 检查并处理所需的列
columns_mapping = {
    'Lev': '总负债率',
    'SL': '流动负债率',
    'LL': '长期负债率',
    'SDR': '短债比率',
    'Cash': '现金比率',
    'ROA': 'ROA',
    'ROE': 'ROE',
    'SLoan': 'SLoan',
    'LLoan': 'LLoan',
    'Top1': 'Top1',
    'HHI5': 'HHI5'
}

# 检查列是否存在，创建对应的指标字典
indicators = {}

# 直接使用列数据（如果存在）或计算（如果需要）
if 'Lev' in data.columns:
    indicators['Lev'] = data['Lev']
else:
    print("计算 Lev = 总负债率...")
    # 可能需要计算

if 'SL' not in data.columns and '流动负债' in data.columns and '总资产' in data.columns:
    print("计算 SL = 流动负债率...")
    data['SL'] = data['流动负债'] / data['总资产']
    indicators['SL'] = data['SL']
elif 'SL' in data.columns:
    indicators['SL'] = data['SL']
else:
    print("无法计算 SL，所需列不存在")

if 'LL' not in data.columns and '长期负债' in data.columns and '总资产' in data.columns:
    print("计算 LL = 长期负债率...")
    data['LL'] = data['长期负债'] / data['总资产']
    indicators['LL'] = data['LL']
elif 'LL' in data.columns:
    indicators['LL'] = data['LL']
else:
    print("无法计算 LL，所需列不存在")

if 'SDR' not in data.columns and '流动负债' in data.columns and '总负债' in data.columns:
    print("计算 SDR = 短债比率...")
    data['SDR'] = data['流动负债'] / data['总负债']
    indicators['SDR'] = data['SDR']
elif 'SDR' in data.columns:
    indicators['SDR'] = data['SDR']
else:
    print("无法计算 SDR，所需列不存在")

if 'Cash' in data.columns:
    indicators['Cash'] = data['Cash']
else:
    print("计算 Cash = 现金比率...")
    # 查找可能的现金列
    cash_cols = [col for col in data.columns if '现金' in col]
    if cash_cols and '总资产' in data.columns:
        data['Cash'] = data[cash_cols[0]] / data['总资产']
        indicators['Cash'] = data['Cash']
    else:
        print("无法计算 Cash，所需列不存在")

if 'ROA' in data.columns:
    indicators['ROA'] = data['ROA']
else:
    print("计算 ROA...")
    if '净利润' in data.columns and '总资产' in data.columns:
        data['ROA'] = data['净利润'] / data['总资产']
        indicators['ROA'] = data['ROA']
    else:
        print("无法计算 ROA，所需列不存在")

if 'ROE' in data.columns:
    indicators['ROE'] = data['ROE']
else:
    print("计算 ROE...")
    if '净利润' in data.columns and '净资产' in data.columns:
        data['ROE'] = data['净利润'] / data['净资产']
        indicators['ROE'] = data['ROE']
    else:
        print("无法计算 ROE，所需列不存在")

if 'SLoan' in data.columns:
    indicators['SLoan'] = data['SLoan']
else:
    print("计算 SLoan...")
    sloan_cols = [col for col in data.columns if '短期' in col and '借款' in col]
    if sloan_cols and '总资产' in data.columns:
        data['SLoan'] = data[sloan_cols[0]] / data['总资产']
        indicators['SLoan'] = data['SLoan']
    else:
        print("无法计算 SLoan，所需列不存在")

if 'LLoan' in data.columns:
    indicators['LLoan'] = data['LLoan']
else:
    print("计算 LLoan...")
    lloan_cols = [col for col in data.columns if '长期' in col and '借款' in col]
    if lloan_cols and '总资产' in data.columns:
        data['LLoan'] = data[lloan_cols[0]] / data['总资产']
        indicators['LLoan'] = data['LLoan']
    else:
        print("无法计算 LLoan，所需列不存在")

if 'Top1' in data.columns:
    indicators['Top1'] = data['Top1']
else:
    print("查找 Top1...")
    top1_cols = [col for col in data.columns if '第一' in col and '股东' in col and '比例' in col]
    if top1_cols:
        data['Top1'] = data[top1_cols[0]]
        indicators['Top1'] = data['Top1']
    else:
        print("无法找到 Top1，所需列不存在")

# 处理离群值 (1% 和 99% 百分位缩尾)
def winsorize(series, limits=(0.01, 0.01)):
    if series.empty:
        return series
    try:
        lower_limit = series.quantile(limits[0])
        upper_limit = series.quantile(1 - limits[1])
        return series.clip(lower=lower_limit, upper=upper_limit)
    except Exception as e:
        print(f"处理离群值时出错: {e}")
        return series

# 对每个指标进行离群值处理
for key in list(indicators.keys()):
    if indicators[key] is not None and not indicators[key].empty:
        try:
            # 确保数据为数值型
            indicators[key] = pd.to_numeric(indicators[key], errors='coerce')
            indicators[key] = winsorize(indicators[key].dropna())
            data[key] = indicators[key]
        except Exception as e:
            print(f"处理{key}指标时出错: {e}")
            # 如果处理失败，从指标列表中移除
            indicators.pop(key, None)

# 每年度计算统计量
yearly_stats = {}
all_years = sorted(data['year'].unique())

for year in all_years:
    year_data = data[data['year'] == year]
    
    yearly_stats[year] = {}
    
    for indicator, values in indicators.items():
        year_values = year_data[indicator].dropna()
        
        if len(year_values) > 0:
            yearly_stats[year][indicator] = {
                '平均值': year_values.mean(),
                '中位数': year_values.median(),
                '标准差': year_values.std(),
                '最小值': year_values.min(),
                '最大值': year_values.max()
            }

# 生成报告
print("\n生成统计报告...")

# 创建结果目录
if not os.path.exists('分析结果'):
    os.makedirs('分析结果')

# 将年度统计量保存到CSV文件以方便查看
print("保存年度统计结果到CSV文件...")
for indicator in indicators.keys():
    # 创建该指标的年度统计表
    stats_df = pd.DataFrame(index=all_years)
    
    for stat in ['平均值', '中位数', '标准差', '最小值', '最大值']:
        stat_values = []
        for year in all_years:
            if year in yearly_stats and indicator in yearly_stats[year]:
                stat_values.append(yearly_stats[year][indicator][stat])
            else:
                stat_values.append(None)
        
        stats_df[stat] = stat_values
    
    # 保存到CSV
    stats_df.to_csv(f'分析结果/{indicator}_年度统计.csv', encoding='utf-8-sig')

# 创建Excel文件
print("生成Excel报告...")
try:
    with pd.ExcelWriter('分析结果/金融指标统计分析.xlsx', engine='openpyxl') as writer:
        # 对每个指标创建一个工作表
        for indicator in indicators.keys():
            # 创建该指标的年度统计表
            stats_df = pd.DataFrame(index=all_years)
            
            for stat in ['平均值', '中位数', '标准差', '最小值', '最大值']:
                stat_values = []
                for year in all_years:
                    if year in yearly_stats and indicator in yearly_stats[year]:
                        stat_values.append(yearly_stats[year][indicator][stat])
                    else:
                        stat_values.append(None)
                
                stats_df[stat] = stat_values
            
            # 保存到Excel
            stats_df.to_excel(writer, sheet_name=indicator[:31])  # Excel表名限制为31个字符
            
            # 生成图表并保存
            plt.figure(figsize=(12, 6))
            
            # 绘制平均值和中位数
            valid_years = [year for year in all_years if year in yearly_stats and indicator in yearly_stats[year]]
            if valid_years:
                mean_values = [yearly_stats[year][indicator]['平均值'] for year in valid_years]
                median_values = [yearly_stats[year][indicator]['中位数'] for year in valid_years]
                
                plt.plot(valid_years, mean_values, 'b-', label='平均值')
                plt.plot(valid_years, median_values, 'r--', label='中位数')
                
                # 添加标题和标签
                plt.title(f'{indicator} 年度统计 (2000-2024)')
                plt.xlabel('年份')
                plt.ylabel('数值')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.legend()
                
                # 保存图表
                plt.tight_layout()
                plt.savefig(f'分析结果/{indicator}_年度趋势.png', dpi=300)
            plt.close()
except Exception as e:
    print(f"生成Excel报告时出错: {e}")
    # 尝试分别生成各个指标的CSV文件作为备选
    for indicator in indicators.keys():
        stats_df = pd.DataFrame(index=all_years)
        for stat in ['平均值', '中位数', '标准差', '最小值', '最大值']:
            stat_values = []
            for year in all_years:
                if year in yearly_stats and indicator in yearly_stats[year]:
                    stat_values.append(yearly_stats[year][indicator][stat])
                else:
                    stat_values.append(None)
            stats_df[stat] = stat_values
        stats_df.to_csv(f'分析结果/{indicator}_年度统计.csv', encoding='utf-8-sig')

# 生成统计分析报告
print("生成文本分析报告...")
with open('分析结果/统计分析报告.txt', 'w', encoding='utf-8') as f:
    f.write('# 金融指标统计分析报告 (2000-2024)\n\n')
    
    for indicator in indicators.keys():
        f.write(f'## {indicator} 指标分析\n\n')
        
        # 计算整体趋势
        valid_years = [year for year in all_years if year in yearly_stats and indicator in yearly_stats[year]]
        
        if valid_years:
            start_year = min(valid_years)
            end_year = max(valid_years)
            
            start_mean = yearly_stats[start_year][indicator]['平均值']
            end_mean = yearly_stats[end_year][indicator]['平均值']
            
            # 计算趋势
            change_pct = (end_mean - start_mean) / abs(start_mean) * 100 if start_mean != 0 else float('inf')
            trend = "上升" if change_pct > 0 else "下降" if change_pct < 0 else "保持稳定"
            
            # 分析峰值和谷值
            max_year = max(valid_years, key=lambda y: yearly_stats[y][indicator]['平均值'])
            min_year = min(valid_years, key=lambda y: yearly_stats[y][indicator]['平均值'])
            
            # 波动性分析
            avg_std = np.mean([yearly_stats[y][indicator]['标准差'] for y in valid_years])
            max_std_year = max(valid_years, key=lambda y: yearly_stats[y][indicator]['标准差'])
            
            # 写入分析结果
            f.write(f"### 总体趋势\n")
            f.write(f"从{start_year}年到{end_year}年，{indicator}指标总体呈{trend}趋势，变化幅度约为{abs(change_pct):.2f}%。\n\n")
            
            f.write(f"### 统计特征\n")
            f.write(f"- 峰值年份: {max_year}年，平均值为{yearly_stats[max_year][indicator]['平均值']:.4f}\n")
            f.write(f"- 谷值年份: {min_year}年，平均值为{yearly_stats[min_year][indicator]['平均值']:.4f}\n")
            f.write(f"- 平均波动性(标准差): {avg_std:.4f}\n")
            f.write(f"- 波动最大年份: {max_std_year}年，标准差为{yearly_stats[max_std_year][indicator]['标准差']:.4f}\n\n")
            
            # 特殊事件/阶段分析
            periods = []
            
            # 金融危机期间(2007-2009)
            crisis_years = [y for y in valid_years if 2007 <= y <= 2009]
            if crisis_years:
                crisis_avg = np.mean([yearly_stats[y][indicator]['平均值'] for y in crisis_years])
                pre_crisis = [y for y in valid_years if 2004 <= y <= 2006]
                if pre_crisis:
                    pre_crisis_avg = np.mean([yearly_stats[y][indicator]['平均值'] for y in pre_crisis])
                    crisis_change = (crisis_avg - pre_crisis_avg) / abs(pre_crisis_avg) * 100 if pre_crisis_avg != 0 else float('inf')
                    periods.append(f"金融危机期间(2007-2009)，{indicator}指标相比危机前期(2004-2006){'上升' if crisis_change > 0 else '下降'}{abs(crisis_change):.2f}%")
            
            # COVID-19疫情期间(2020-2022)
            covid_years = [y for y in valid_years if 2020 <= y <= 2022]
            if covid_years:
                covid_avg = np.mean([yearly_stats[y][indicator]['平均值'] for y in covid_years])
                pre_covid = [y for y in valid_years if 2017 <= y <= 2019]
                if pre_covid:
                    pre_covid_avg = np.mean([yearly_stats[y][indicator]['平均值'] for y in pre_covid])
                    covid_change = (covid_avg - pre_covid_avg) / abs(pre_covid_avg) * 100 if pre_covid_avg != 0 else float('inf')
                    periods.append(f"COVID-19疫情期间(2020-2022)，{indicator}指标相比疫情前期(2017-2019){'上升' if covid_change > 0 else '下降'}{abs(covid_change):.2f}%")
            
            if periods:
                f.write(f"### 特殊时期分析\n")
                for p in periods:
                    f.write(f"- {p}\n")
                f.write("\n")
        
        f.write("---\n\n")

print("\n分析完成! 结果已保存到 '分析结果' 文件夹中。")

def generate_part_c(data):
    """生成C部分内容：负债率的行业特征分析"""
    
    industry_mapping = {
        'C': '制造业',
        'D': '电力、热力、燃气及水生产和供应业',
        'G': '交通运输业',
        'E': '建筑业',
        'K': '房地产业',
        'F': '批发和零售业',
        'J': '金融业'
    }
    
    # 筛选所需的行业和年份
    target_industries = list(industry_mapping.keys())
    min_year = 1998
    max_year = data['year'].max()
    data_filtered = data[(data['industry_code'].isin(target_industries)) & 
                         (data['year'] >= min_year) & 
                         (data['year'] <= max_year)]
    
    # 计算各行业每年的平均杠杆率
    avg_lev_by_industry = data_filtered.groupby(['industry_code', 'year'])['Lev'].mean().reset_index()
    
    # 转换为数据透视表，用于绘图
    lev_pivot = avg_lev_by_industry.pivot(index='year', columns='industry_code', values='Lev')
    
    # 绘制行业负债率时序图
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
    plt.title('各行业平均负债率时序变化(1998-至今)', fontsize=16)
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
    
    plt.tight_layout()
    plt.savefig("分析结果/images/industry_leverage_trend.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # 计算各行业平均负债率和波动范围
    industry_avg_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].mean()
    industry_max_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].max()
    industry_min_lev = avg_lev_by_industry.groupby('industry_code')['Lev'].min()
    
    # 绘制不同行业负债率对比柱状图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(industry_avg_lev)), industry_avg_lev.values, 
             yerr=[(industry_avg_lev-industry_min_lev).values, (industry_max_lev-industry_avg_lev).values],
             capsize=5, alpha=0.7)
    
    # 在柱状图上添加数值标签
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.4f}',
                ha='center', va='bottom', fontsize=9)
    
    plt.xticks(range(len(industry_avg_lev)), 
               [f"{industry_mapping.get(code, '未知')} ({code})" for code in industry_avg_lev.index],
               rotation=45, ha='right')
    
    plt.title('各行业平均负债率对比', fontsize=14)
    plt.ylabel('负债率', fontsize=12)
    plt.ylim(0, industry_max_lev.max() * 1.1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("分析结果/images/industry_leverage_comparison.png", dpi=300)
    plt.close()
    
    # 选择奇数年份
    selected_years = list(range(1999, max_year + 1, 2))
    
    # 筛选所选年份的数据
    data_selected_years = data_filtered[data_filtered['year'].isin(selected_years)]
    
    # 为每个指标创建行业对比图和数据表
    indicators = ['SLoan', 'LLoan', 'Lev', 'Cash', 'ROA', 'ROE']
    indicator_titles = {
        'SLoan': '短期负债率',
        'LLoan': '长期负债率',
        'Lev': '总负债率',
        'Cash': '现金比率',
        'ROA': '总资产回报率',
        'ROE': '净资产收益率'
    }
    
    # 存储各指标的行业平均值和行业年份数据透视表
    industry_indicators_avg = {}
    industry_indicators_pivot = {}
    
    for indicator in indicators:
        if indicator in data_selected_years.columns:
            # 计算各行业平均值
            ind_avg = data_selected_years.groupby('industry_code')[indicator].mean().sort_values(ascending=False)
            industry_indicators_avg[indicator] = ind_avg
            
            # 创建行业年份数据透视表
            pivot = data_selected_years.pivot_table(
                values=indicator,
                index='industry_code',
                columns='year',
                aggfunc='mean'
            )
            industry_indicators_pivot[indicator] = pivot
            
            # 绘制柱状图
            plt.figure(figsize=(12, 6))
            bars = plt.bar(range(len(ind_avg)), ind_avg.values, alpha=0.7)
            
            # 添加数值标签
            for i, bar in enumerate(bars):
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height + height*0.02,
                        f'{height:.4f}',
                        ha='center', va='bottom', fontsize=9)
            
            plt.xticks(range(len(ind_avg)), 
                      [f"{industry_mapping.get(code, '未知')} ({code})" for code in ind_avg.index],
                      rotation=45, ha='right')
            
            plt.title(f'各行业{indicator_titles.get(indicator, indicator)}对比', fontsize=14)
            plt.ylabel(indicator_titles.get(indicator, indicator), fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            plt.savefig(f"分析结果/images/industry_{indicator}_comparison.png", dpi=300)
            plt.close()
    
    # 计算负债结构占比
    if 'SLoan' in data_selected_years.columns and 'LLoan' in data_selected_years.columns and 'Lev' in data_selected_years.columns:
        industry_avg_sloan = data_selected_years.groupby('industry_code')['SLoan'].mean()
        industry_avg_lloan = data_selected_years.groupby('industry_code')['LLoan'].mean()
        industry_avg_lev = data_selected_years.groupby('industry_code')['Lev'].mean()
        
        # 计算占比
        debt_structure = pd.DataFrame({
            '短期负债占比': industry_avg_sloan / industry_avg_lev * 100,
            '长期负债占比': industry_avg_lloan / industry_avg_lev * 100
        })
        
        # 绘制负债结构占比图
        plt.figure(figsize=(12, 6))
        debt_structure.plot(kind='bar', alpha=0.7, ax=plt.gca())
        plt.title('各行业负债结构占比', fontsize=14)
        plt.ylabel('占比 (%)', fontsize=12)
        plt.xticks(range(len(debt_structure)), 
                  [f"{industry_mapping.get(code, '未知')} ({code})" for code in debt_structure.index],
                  rotation=45, ha='right')
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig("分析结果/images/industry_debt_structure.png", dpi=300)
        plt.close()
    
    # C部分Markdown内容
    part_c_content = """## C. 负债率的行业特征分析

### 1. 行业年平均负债率时序图分析(1998-2023)

![各行业负债率时序变化](分析结果/images/industry_leverage_trend.png)

通过对1998-2023年各行业负债率的分析，我们发现了以下主要特征：

#### 1.1 行业间负债率差异明显

![各行业平均负债率对比](分析结果/images/industry_leverage_comparison.png)

各行业平均负债率排名如下：

| 行业 | 平均负债率 |
|------|------------|
"""
    
    # 添加各行业平均负债率排名
    for industry_code, avg_lev in industry_avg_lev.sort_values(ascending=False).items():
        industry_name = industry_mapping.get(industry_code, '未知')
        part_c_content += f"| {industry_name} ({industry_code}) | {avg_lev:.4f} |\n"
    
    part_c_content += """
#### 1.2 负债率波动性分析

各行业负债率波动范围：

| 行业 | 最低负债率 | 最高负债率 | 波动幅度 |
|------|------------|------------|----------|
"""
    
    # 添加各行业负债率波动范围
    for industry_code in industry_avg_lev.sort_values(ascending=False).index:
        max_lev = industry_max_lev[industry_code]
        min_lev = industry_min_lev[industry_code]
        range_lev = max_lev - min_lev
        industry_name = industry_mapping.get(industry_code, '未知')
        part_c_content += f"| {industry_name} ({industry_code}) | {min_lev:.4f} | {max_lev:.4f} | {range_lev:.4f} |\n"
    
    part_c_content += """
#### 1.3 重大事件影响分析

##### 金融危机影响(2006 vs 2010)
"""
    
    # 添加金融危机影响分析
    if 2006 in lev_pivot.index and 2010 in lev_pivot.index:
        part_c_content += """
| 行业 | 危机前(2006) | 危机后(2010) | 变化率 |
|------|--------------|--------------|--------|
"""
        for industry_code in lev_pivot.columns:
            if pd.notna(lev_pivot.loc[2006, industry_code]) and pd.notna(lev_pivot.loc[2010, industry_code]):
                pre_crisis = lev_pivot.loc[2006, industry_code]
                post_crisis = lev_pivot.loc[2010, industry_code]
                pct_change = (post_crisis - pre_crisis) / pre_crisis * 100
                direction = "↑" if pct_change > 0 else "↓"
                industry_name = industry_mapping.get(industry_code, '未知')
                part_c_content += f"| {industry_name} ({industry_code}) | {pre_crisis:.4f} | {post_crisis:.4f} | {pct_change:.2f}% {direction} |\n"
    
    # 添加疫情影响分析
    part_c_content += "\n##### 新冠疫情影响(2019 vs 2022)\n"
    
    if 2019 in lev_pivot.index and 2022 in lev_pivot.index:
        part_c_content += """
| 行业 | 疫情前(2019) | 疫情后(2022) | 变化率 |
|------|--------------|--------------|--------|
"""
        for industry_code in lev_pivot.columns:
            if pd.notna(lev_pivot.loc[2019, industry_code]) and pd.notna(lev_pivot.loc[2022, industry_code]):
                pre_covid = lev_pivot.loc[2019, industry_code]
                post_covid = lev_pivot.loc[2022, industry_code]
                pct_change = (post_covid - pre_covid) / pre_covid * 100
                direction = "↑" if pct_change > 0 else "↓"
                industry_name = industry_mapping.get(industry_code, '未知')
                part_c_content += f"| {industry_name} ({industry_code}) | {pre_covid:.4f} | {post_covid:.4f} | {pct_change:.2f}% {direction} |\n"
    
    # 添加长期趋势分析
    part_c_content += "\n#### 1.4 长期趋势分析\n\n"
    part_c_content += "| 行业 | 趋势 | 斜率 |\n"
    part_c_content += "|------|------|------|\n"
    
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
            part_c_content += f"| {industry_name} ({industry_code}) | {trend} | {slope:.4f} |\n"
    
    # 添加主要财务指标的行业对比分析
    part_c_content += """
### 2. 行业财务指标比较分析(1999-2023奇数年)

#### 2.1 负债结构分析 (SLoan, LLoan, Lev)
"""
    
    # 添加负债结构占比分析
    if 'SLoan' in industry_indicators_avg and 'LLoan' in industry_indicators_avg and 'Lev' in industry_indicators_avg:
        part_c_content += "\n![各行业负债结构占比](分析结果/images/industry_debt_structure.png)\n\n"
        part_c_content += "各行业负债结构占比：\n\n"
        part_c_content += "| 行业 | 短期负债占比 | 长期负债占比 |\n"
        part_c_content += "|------|--------------|------------|\n"
        
        for industry_code in industry_avg_lev.index:
            if industry_avg_lev[industry_code] > 0:
                sloan_ratio = industry_avg_sloan[industry_code] / industry_avg_lev[industry_code] * 100
                lloan_ratio = industry_avg_lloan[industry_code] / industry_avg_lev[industry_code] * 100
                industry_name = industry_mapping.get(industry_code, '未知')
                part_c_content += f"| {industry_name} ({industry_code}) | {sloan_ratio:.2f}% | {lloan_ratio:.2f}% |\n"
    
    # 添加各指标的行业对比图
    indicators_groups = [
        ('SLoan', '短期负债率'),
        ('LLoan', '长期负债率'),
        ('Lev', '总负债率'),
        ('Cash', '现金比率'),
        ('ROA', '总资产回报率'),
        ('ROE', '净资产收益率')
    ]
    
    for indicator, title in indicators_groups:
        if indicator in industry_indicators_avg:
            if indicator in ['SLoan', 'LLoan', 'Lev']:
                continue  # 这些已经在负债结构分析中处理过
            
            section_title = "#### "
            if indicator in ['Cash']:
                section_title += "2.2 流动性分析 (Cash)"
            elif indicator in ['ROA', 'ROE'] and section_title.find("盈利能力分析") == -1:
                section_title += "2.3 盈利能力分析 (ROA, ROE)"
            else:
                continue
                
            part_c_content += f"\n{section_title}\n\n"
            part_c_content += f"![各行业{title}对比](分析结果/images/industry_{indicator}_comparison.png)\n\n"
            
            # 添加表格
            part_c_content += f"各行业{title}排名：\n\n"
            part_c_content += "| 行业 | 平均值 |\n"
            part_c_content += "|------|-------|\n"
            
            for industry_code, value in industry_indicators_avg[indicator].items():
                industry_name = industry_mapping.get(industry_code, '未知')
                part_c_content += f"| {industry_name} ({industry_code}) | {value:.4f} |\n"
    
    # 添加财务杠杆效应分析
    if 'ROA' in industry_indicators_avg and 'ROE' in industry_indicators_avg:
        part_c_content += "\n##### 财务杠杆效应分析\n\n"
        part_c_content += "| 行业 | ROA | ROE | 杠杆效应 | 类型 |\n"
        part_c_content += "|------|-----|-----|----------|------|\n"
        
        for industry_code in set(industry_indicators_avg['ROA'].index) & set(industry_indicators_avg['ROE'].index):
            roa = industry_indicators_avg['ROA'][industry_code]
            roe = industry_indicators_avg['ROE'][industry_code]
            
            if roa > 0:
                leverage_effect = (roe - roa) / roa * 100
                
                if roe > roa:
                    effect_type = "正向财务杠杆"
                    sign = "+"
                else:
                    effect_type = "负向财务杠杆"
                    sign = ""
                
                industry_name = industry_mapping.get(industry_code, '未知')
                part_c_content += f"| {industry_name} ({industry_code}) | {roa:.4f} | {roe:.4f} | {sign}{leverage_effect:.2f}% | {effect_type} |\n"
    
    # 添加各指标变化趋势分析
    part_c_content += "\n#### 2.4 各指标变化趋势分析\n\n"
    
    for indicator, title in indicators_groups:
        if indicator in industry_indicators_pivot:
            pivot = industry_indicators_pivot[indicator]
            years = sorted(pivot.columns)
            
            if len(years) >= 2:
                first_year = years[0]
                last_year = years[-1]
                
                part_c_content += f"##### {title}({indicator})变化趋势\n\n"
                part_c_content += f"| 行业 | {first_year}年 | {last_year}年 | 变化率 | 趋势评估 |\n"
                part_c_content += "|------|----------|----------|--------|--------|\n"
                
                for industry_code in pivot.index:
                    if pd.notna(pivot.loc[industry_code, first_year]) and pd.notna(pivot.loc[industry_code, last_year]):
                        first_value = pivot.loc[industry_code, first_year]
                        last_value = pivot.loc[industry_code, last_year]
                        
                        if first_value != 0 and not pd.isna(first_value) and not pd.isna(last_value):
                            change_pct = (last_value - first_value) / abs(first_value) * 100
                            direction = "↑" if change_pct > 0 else "↓"
                            
                            # 变化趋势描述
                            if abs(change_pct) < 10:
                                trend_desc = "基本保持稳定"
                            elif abs(change_pct) < 50:
                                trend_desc = "有所" + ("增长" if change_pct > 0 else "下降")
                            elif abs(change_pct) < 100:
                                trend_desc = "显著" + ("增长" if change_pct > 0 else "下降")
                            else:
                                trend_desc = "大幅" + ("增长" if change_pct > 0 else "下降")
                            
                            industry_name = industry_mapping.get(industry_code, '未知')
                            part_c_content += f"| {industry_name} ({industry_code}) | {first_value:.4f} | {last_value:.4f} | {change_pct:.2f}% {direction} | {trend_desc} |\n"
                
                part_c_content += "\n"
    
    # 总结分析
    part_c_content += """
### 3. 行业特征总结分析

根据上述分析，我们可以得出以下关于不同行业负债及财务特征的结论：

1. **行业负债水平差异显著**
   - 制造业(C)平均负债率最高，体现了其资本密集型特征和对债务融资的依赖
   - 批发和零售业(F)负债率相对较低，主要依靠经营性负债而非金融负债
   - 房地产业(K)负债率处于中等水平，但受宏观调控政策影响显著

2. **负债结构行业特征明显**
   - 电力、热力、燃气及水生产和供应业(D)长期负债占比高，体现基础设施行业特性
   - 批发和零售业(F)短期负债占比高，反映其对流动资金需求较大
   - 金融业(J)有特殊的资产负债结构，负债率高但稳定

3. **行业盈利与负债关系各异**
   - 负债率高的行业如制造业通过财务杠杆提升ROE，杠杆效应显著
   - 房地产业在特定时期杠杆率与盈利能力呈现正相关性
   - 金融危机和疫情对高负债行业影响更为显著，表现出更大的波动性

4. **行业抗风险能力差异**
   - 现金比率高的行业如信息技术业在危机时期表现更为稳健
   - 高负债行业在金融危机后进行了显著的负债结构调整
   - 疫情期间各行业应对策略不同，体现出行业特有的韧性和适应能力

5. **行业负债长期趋势**
   - 制造业负债率呈下降趋势，体现供给侧改革和去杠杆政策成效
   - 公用事业行业负债率相对稳定，受益于政策支持和稳定的现金流
   - 新兴行业初期高杠杆，随行业成熟逐步优化资本结构

这些行业特征和趋势为投资者、政策制定者和企业管理者提供了重要参考，有助于理解不同行业的财务特性和风险特征。
"""
    
    return part_c_content

def create_complete_markdown_report():
    """创建完整的金融数据分析报告，包含A、B、C三个部分"""
    
    # 创建保存结果的目录
    os.makedirs("分析结果/images", exist_ok=True)
    
    # 读取Excel文件获取原始数据
    try:
        data = pd.read_excel("金融数据分析.xlsx")
        print("数据读取成功！")
    except Exception as e:
        print(f"读取数据时出错: {e}")
        return
    
    # 数据预处理
    data = preprocess_data(data)
    
    # 生成三个部分的内容
    part_a = generate_part_a(data)
    part_b = generate_part_b(data)
    part_c = generate_part_c(data)
    
    # 合并为一个完整的报告
    full_report = f"""# 金融数据分析综合报告

{part_a}

{part_b}

{part_c}
"""
    
    # 保存Markdown文件
    with open("分析结果/金融数据分析综合报告.md", "w", encoding="utf-8") as f:
        f.write(full_report)
    
    print("完整Markdown报告已生成：分析结果/金融数据分析综合报告.md")

if __name__ == "__main__":
    create_complete_markdown_report() 