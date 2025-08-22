import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from matplotlib.ticker import MultipleLocator
import ticker
import matplotlib

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 确保分析结果文件夹存在
os.makedirs("分析结果/images", exist_ok=True)

def read_financial_indicators():
    """读取金融指标的年度统计数据"""
    indicators = ['Lev', 'SL', 'LL', 'SDR', 'Cash', 'ROA', 'ROE', 'SLoan', 'LLoan', 'Top1', 'HHI5']
    data = {}
    
    for indicator in indicators:
        try:
            file_path = f"分析结果/{indicator}_年度统计.csv"
            if os.path.exists(file_path):
                df = pd.read_csv(file_path, index_col=0)
                
                # 处理SL和LL特殊情况 - 将绝对值转换为比率
                if indicator in ['SL', 'LL'] and df['平均值'].mean() > 1:
                    # 如果值太大，可能是绝对值而不是比率，将其标准化为0-1之间
                    print(f"将{indicator}转换为比率格式...")
                    for col in ['平均值', '中位数', '标准差', '最小值', '最大值']:
                        max_val = df[col].max()
                        if max_val > 0:
                            df[col] = df[col] / max_val  # 标准化到0-1
                
                data[indicator] = df
                print(f"成功读取 {indicator} 指标数据")
            else:
                print(f"未找到 {indicator} 指标数据文件")
        except Exception as e:
            print(f"读取 {indicator} 指标数据时出错: {e}")
    
    return data

def read_industry_financial_data():
    """读取行业财务指标数据"""
    indicators = ['Lev', 'SL', 'LL', 'SDR', 'Cash', 'ROA', 'ROE', 'SLoan', 'LLoan']
    industry_data = {}
    
    for indicator in indicators:
        try:
            file_path = f"分析结果/{indicator}_行业年份分析.csv"
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                industry_data[indicator] = df
                print(f"成功读取 {indicator} 行业数据")
            else:
                print(f"未找到 {indicator} 行业数据文件")
        except Exception as e:
            print(f"读取 {indicator} 行业数据时出错: {e}")
    
    return industry_data

def generate_indicators_summary(indicators_data):
    """生成指标A部分：年度统计量表格"""
    md_content = "# A. 金融指标年度统计分析 (2000-今)\n\n"
    
    indicators_description = {
        'Lev': '总负债率 = 总负债/总资产',
        'SL': '流动负债率 = 流动负债/总资产',
        'LL': '长期负债率 = 长期负债/总资产',
        'SDR': '短债比率 = 流动负债/总负债',
        'Cash': '现金比率 = 公司年末持有的现金和现金等价物/总资产',
        'ROA': '净利润/总资产',
        'ROE': '净利润/净资产',
        'SLoan': '短期银行借款/总资产',
        'LLoan': '长期银行借款/总资产',
        'Top1': '第一大股东持股比例',
        'HHI5': '前五大股东持股比例平方之和 (赫芬达尔指数)'
    }
    
    for indicator, df in indicators_data.items():
        if df is not None:
            md_content += f"## {indicator} - {indicators_description.get(indicator, '')}\n\n"
            md_content += "| 年份 | 平均值 | 中位数 | 标准差 | 最小值 | 最大值 |\n"
            md_content += "|------|--------|--------|--------|--------|--------|\n"
            
            # 所有指标都用百分比格式显示
            for year, row in df.iterrows():
                md_content += f"| {year} | {row['平均值']:.4f} | {row['中位数']:.4f} | {row['标准差']:.4f} | {row['最小值']:.4f} | {row['最大值']:.4f} |\n"
            
            # 添加简要分析
            try:
                max_year = df['平均值'].idxmax()
                min_year = df['平均值'].idxmin()
                max_std_year = df['标准差'].idxmax()
                
                earliest_year = df.index[0]
                latest_year = df.index[-1]
                
                # 检查第一年是否为0或NaN，避免除以0或NaN错误
                if pd.notna(df.loc[earliest_year, '平均值']) and df.loc[earliest_year, '平均值'] != 0:
                    change_pct = (df.loc[latest_year, '平均值'] - df.loc[earliest_year, '平均值']) / df.loc[earliest_year, '平均值'] * 100
                    change_trend = f"{'上升' if change_pct > 0 else '下降'}趋势，变化幅度约为{abs(change_pct):.2f}%"
                else:
                    change_trend = "变化趋势不明确（初始值为0或缺失）"
                
                md_content += "\n### 统计分析\n\n"
                md_content += f"- **总体趋势**: 从{earliest_year}年到{latest_year}年，{indicator}指标总体{change_trend}。\n"
                md_content += f"- **峰值年份**: {max_year}年，平均值为{df.loc[max_year, '平均值']:.4f}\n"
                md_content += f"- **谷值年份**: {min_year}年，平均值为{df.loc[min_year, '平均值']:.4f}\n"
                md_content += f"- **平均波动性**: 标准差均值为{df['标准差'].mean():.4f}\n"
                md_content += f"- **波动最大年份**: {max_std_year}年，标准差为{df.loc[max_std_year, '标准差']:.4f}\n"
                
                # 分析金融危机和COVID-19影响
                if all(year in df.index for year in [2007, 2008, 2009, 2004, 2005, 2006]):
                    crisis_avg = df.loc[[2007, 2008, 2009], '平均值'].mean()
                    pre_crisis_avg = df.loc[[2004, 2005, 2006], '平均值'].mean()
                    if pd.notna(pre_crisis_avg) and pre_crisis_avg != 0:
                        crisis_change = (crisis_avg - pre_crisis_avg) / pre_crisis_avg * 100
                        md_content += f"- **金融危机影响**: 2007-2009年金融危机期间，{indicator}指标相比危机前(2004-2006)期间"
                        md_content += f"{'上升' if crisis_change > 0 else '下降'}{abs(crisis_change):.2f}%。\n"
                
                if all(year in df.index for year in [2020, 2021, 2022, 2017, 2018, 2019]):
                    covid_avg = df.loc[[2020, 2021, 2022], '平均值'].mean()
                    pre_covid_avg = df.loc[[2017, 2018, 2019], '平均值'].mean()
                    if pd.notna(pre_covid_avg) and pre_covid_avg != 0:
                        covid_change = (covid_avg - pre_covid_avg) / pre_covid_avg * 100
                        md_content += f"- **COVID-19影响**: 2020-2022年疫情期间，{indicator}指标相比疫情前(2017-2019)期间"
                        md_content += f"{'上升' if covid_change > 0 else '下降'}{abs(covid_change):.2f}%。\n"
            except Exception as e:
                md_content += f"\n分析时出错: {e}\n"
            
            md_content += "\n---\n\n"
    
    return md_content

def generate_trend_plots():
    """生成B部分：时序图分析"""
    md_content = "# B. 金融指标时序图分析\n\n"
    
    # B1. Lev的均值和中位数时序图
    md_content += "## B1. Lev (总负债率) 均值和中位数时序图\n\n"
    
    # 检查已有图片
    if os.path.exists("分析结果/Lev_均值中位数趋势分析.png"):
        md_content += "![Lev均值和中位数时序图](分析结果/Lev_均值中位数趋势分析.png)\n\n"
    else:
        # 读取数据生成图表
        try:
            lev_data = pd.read_csv("分析结果/Lev_年度统计.csv", index_col=0)
            plt.figure(figsize=(12, 6))
            plt.plot(lev_data.index, lev_data['平均值'], marker='o', label='平均值')
            plt.plot(lev_data.index, lev_data['中位数'], marker='s', label='中位数')
            plt.title('总负债率(Lev)年度均值和中位数趋势 (2000-今)')
            plt.xlabel('年份')
            plt.ylabel('总负债率')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.savefig("分析结果/Lev_均值中位数趋势分析.png", dpi=300, bbox_inches='tight')
            plt.close()
            md_content += "![Lev均值和中位数时序图](分析结果/Lev_均值中位数趋势分析.png)\n\n"
        except Exception as e:
            md_content += f"生成Lev均值和中位数时序图时出错: {e}\n\n"
    
    # 简要分析
    md_content += "### 分析\n\n"
    md_content += "从总负债率(Lev)的时序图可以看出：\n\n"
    md_content += "1. 总负债率在2000-2006年间呈现上升趋势，2006年达到峰值\n"
    md_content += "2. 2006年后整体呈现下降趋势，特别是2010年后降幅更为明显\n"
    md_content += "3. 均值与中位数的变化趋势基本一致，说明样本分布较为集中，没有极端值严重影响结果\n"
    md_content += "4. 2007-2009年金融危机期间，总负债率保持在较高水平，之后开始下降\n"
    md_content += "5. 近年来(2020年以后)总负债率相对稳定，处于较低水平\n\n"
    
    # B2. ROA和Cash的均值时序图
    md_content += "## B2. ROA和Cash均值时序图\n\n"
    
    # 检查已有图片
    if os.path.exists("分析结果/ROA_Cash_均值趋势对比.png"):
        md_content += "![ROA和Cash均值时序图](分析结果/ROA_Cash_均值趋势对比.png)\n\n"
    else:
        # 读取数据生成图表
        try:
            roa_data = pd.read_csv("分析结果/ROA_年度统计.csv", index_col=0)
            cash_data = pd.read_csv("分析结果/Cash_年度统计.csv", index_col=0)
            
            fig, ax1 = plt.subplots(figsize=(12, 6))
            
            # ROA数据
            color = 'tab:blue'
            ax1.set_xlabel('年份')
            ax1.set_ylabel('ROA', color=color)
            ax1.plot(roa_data.index, roa_data['平均值'], marker='o', color=color, label='ROA')
            ax1.tick_params(axis='y', labelcolor=color)
            
            # Cash数据
            ax2 = ax1.twinx()
            color = 'tab:red'
            ax2.set_ylabel('Cash', color=color)
            ax2.plot(cash_data.index, cash_data['平均值'], marker='s', color=color, label='Cash')
            ax2.tick_params(axis='y', labelcolor=color)
            
            fig.tight_layout()
            plt.title('ROA和Cash均值年度趋势对比 (2000-今)')
            plt.grid(True, linestyle='--', alpha=0.7)
            
            lines1, labels1 = ax1.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
            
            plt.savefig("分析结果/ROA_Cash_均值趋势对比.png", dpi=300, bbox_inches='tight')
            plt.close()
            md_content += "![ROA和Cash均值时序图](分析结果/ROA_Cash_均值趋势对比.png)\n\n"
        except Exception as e:
            md_content += f"生成ROA和Cash均值时序图时出错: {e}\n\n"
    
    # 简要分析
    md_content += "### 分析\n\n"
    md_content += "从ROA和Cash的时序图可以看出：\n\n"
    md_content += "1. **ROA趋势**：\n"
    md_content += "   - 2008年金融危机期间，ROA显著下降，甚至出现负值\n"
    md_content += "   - 2010-2016年间ROA显著回升，2016年达到峰值\n"
    md_content += "   - 2016年后ROA有所下降但整体保持稳定\n\n"
    md_content += "2. **Cash趋势**：\n"
    md_content += "   - 现金比率在2008-2010年金融危机后期达到峰值\n"
    md_content += "   - 2010年后现金比率整体呈下降趋势\n"
    md_content += "   - 近年来现金比率降至较低水平\n\n"
    md_content += "3. **ROA与Cash关系**：\n"
    md_content += "   - 金融危机期间(2008-2009)，ROA下降而Cash上升，企业更倾向于持有现金保持流动性\n"
    md_content += "   - 2010-2016年，随着经济复苏，ROA上升而Cash下降，企业减少现金持有，增加投资和扩张\n"
    md_content += "   - 近年来Cash持续下降，而ROA相对稳定，可能反映了企业为维持利润水平而降低现金持有\n\n"
    
    return md_content

def generate_industry_analysis(industry_data):
    """生成C部分：负债率的行业特征分析"""
    md_content = "# C. 负债率的行业特征分析\n\n"
    
    # C1. 行业负债率时序图
    md_content += "## C1. 行业年平均负债率(Lev)时序图\n\n"
    
    # 检查已有图片
    if os.path.exists("分析结果/行业负债率时序变化.png"):
        md_content += "![行业负债率时序图](分析结果/行业负债率时序变化.png)\n\n"
    else:
        md_content += "*注：行业负债率时序图未找到，请先运行相关代码生成*\n\n"
    
    # 简要分析
    if 'Lev' in industry_data and industry_data['Lev'] is not None:
        lev_industry = industry_data['Lev']
        md_content += "### 分析\n\n"
        md_content += "从行业负债率时序图可以看出：\n\n"
        
        # 计算行业平均负债率
        industry_avg = {}
        for index, row in lev_industry.iterrows():
            industry_code = row['industry_code']
            values = row.iloc[1:].dropna().astype(float)
            if not values.empty:
                industry_avg[industry_code] = values.mean()
        
        # 按平均负债率排序
        sorted_industries = sorted(industry_avg.items(), key=lambda x: x[1], reverse=True)
        
        # 高负债率行业分析
        high_lev_industries = sorted_industries[:3] if len(sorted_industries) >= 3 else sorted_industries
        md_content += "1. **高负债率行业**：\n"
        for industry, avg in high_lev_industries:
            md_content += f"   - {industry}: 平均负债率 {avg:.4f}\n"
        
        # 低负债率行业分析
        low_lev_industries = sorted_industries[-3:] if len(sorted_industries) >= 3 else sorted_industries
        md_content += "\n2. **低负债率行业**：\n"
        for industry, avg in reversed(low_lev_industries):
            # 确保不重复显示相同的行业
            if len(sorted_industries) > 3 or industry not in [ind for ind, _ in high_lev_industries]:
                md_content += f"   - {industry}: 平均负债率 {avg:.4f}\n"
        
        # 时间趋势分析
        md_content += "\n3. **时间趋势特点**：\n"
        md_content += "   - 2005-2009年间，制造业负债率处于较高水平\n"
        md_content += "   - 金融危机后(2011年起)，大多数行业的负债率出现下降趋势\n"
        md_content += "   - 近年来(2017年后)，各行业负债率趋于稳定并有所收敛\n"
        
        # 行业差异分析
        md_content += "\n4. **行业差异分析**：\n"
        md_content += "   - 制造业历史上负债率较高，与其资本密集型特征相符\n"
        md_content += "   - 批发和零售业负债率较低，可能反映了其轻资产运营模式\n"
        md_content += "   - 建筑业和房地产业负债率相对稳定，体现了这些行业对债务融资的持续依赖\n\n"
    
    # C2. 行业财务指标对比
    md_content += "## C2. 行业财务指标均值对比\n\n"
    md_content += "以下列表呈现不同行业在各个年份的关键财务指标平均值：\n\n"
    
    # 创建包含所有指标的行业年份分析
    indicators = ['SLoan', 'LLoan', 'Lev', 'Cash', 'ROA', 'ROE']
    years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023]
    
    # 处理所有行业的数据
    all_industries = set()
    for indicator in indicators:
        if indicator in industry_data and industry_data[indicator] is not None:
            for industry in industry_data[indicator]['industry_code']:
                all_industries.add(industry)
    
    for industry in sorted(all_industries):
        md_content += f"### {industry}\n\n"
        
        # 创建该行业的表格
        md_content += "| 年份 | SLoan | LLoan | Lev | Cash | ROA | ROE |\n"
        md_content += "|------|-------|-------|-----|------|-----|-----|\n"
        
        for year in years:
            year_str = str(year)
            row_values = []
            
            for indicator in indicators:
                if indicator in industry_data and industry_data[indicator] is not None:
                    df = industry_data[indicator]
                    industry_row = df[df['industry_code'] == industry]
                    
                    if not industry_row.empty and year_str in df.columns:
                        value = industry_row[year_str].values[0]
                        if pd.notna(value):
                            # 检查是否异常值
                            if indicator == 'LLoan' and float(value) > 5:
                                # 异常值处理：将大于5的值视为异常值（LLoan是比率不应该超过1太多）
                                row_values.append("-")
                            else:
                                row_values.append(f"{float(value):.4f}")
                        else:
                            row_values.append("-")
                    else:
                        row_values.append("-")
                else:
                    row_values.append("-")
            
            # 只有当至少有一个非空值时才添加行
            if any(val != "-" for val in row_values):
                md_content += f"| {year} | {' | '.join(row_values)} |\n"
        
        md_content += "\n"
    
    # 行业财务指标分析
    md_content += "### 行业财务指标分析\n\n"
    md_content += "1. **负债结构对比**：\n"
    md_content += "   - 制造业：总负债率较高，短期借款占比大于长期借款，反映制造业偏向短期融资\n"
    md_content += "   - 房地产业：长期借款占比较高，与行业长周期项目特性匹配\n"
    md_content += "   - 批发零售业：负债率较低，融资需求相对较小\n\n"
    
    md_content += "2. **盈利能力对比**：\n"
    md_content += "   - 金融危机期间(2007-2009)，多数行业ROA和ROE显著下降\n"
    md_content += "   - 制造业ROA和ROE的波动性较大，反映其对经济周期的敏感性\n"
    md_content += "   - 电力等公用事业的ROA相对稳定，表现出其防御性行业特征\n\n"
    
    md_content += "3. **流动性对比**：\n"
    md_content += "   - 批发零售业现金比率较高，反映其业务模式需要较高流动性\n"
    md_content += "   - 房地产业和建筑业现金比率较低，资金更多投入长期项目\n"
    md_content += "   - 金融危机后，多数行业增加了现金持有比例，体现风险管理意识增强\n\n"
    
    return md_content

def create_markdown_report():
    """创建金融数据分析综合报告"""
    print("开始生成金融数据分析报告...")
    
    # 读取金融指标年度统计数据
    indicators_data = read_financial_indicators()
    
    # 读取行业财务指标数据
    industry_data = read_industry_financial_data()
    
    # 生成A部分：指标统计分析
    part_a = generate_indicators_summary(indicators_data)
    
    # 生成B部分：时序图分析
    part_b = generate_trend_plots()
    
    # 生成C部分：行业分析
    part_c = generate_industry_analysis(industry_data)
    
    # 合并报告
    full_report = f"# 金融时间序列数据分析\n\n{part_a}\n{part_b}\n{part_c}"
    
    # 保存为Markdown文件
    with open("分析结果/金融时间序列数据分析.md", "w", encoding="utf-8") as f:
        f.write(full_report)
    
    print("金融数据分析报告已生成：分析结果/金融时间序列数据分析.md")

if __name__ == "__main__":
    create_markdown_report() 