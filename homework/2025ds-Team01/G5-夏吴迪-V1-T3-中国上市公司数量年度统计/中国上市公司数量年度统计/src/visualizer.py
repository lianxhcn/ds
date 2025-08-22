"""
中国股票市场数据可视化模块
生成各种统计图表和可视化分析
"""

# 智能检测运行环境并配置matplotlib
import matplotlib
import os
import sys

def setup_matplotlib_backend():
    """智能设置matplotlib后端"""
    try:
        # 检测是否在Jupyter环境中
        if 'ipykernel' in sys.modules:
            # 在Jupyter环境中，不要设置后端，让Jupyter自己处理
            print("✅ 检测到Jupyter环境，使用默认后端")
        elif 'IPython' in sys.modules:
            try:
                get_ipython()
                print("✅ 检测到IPython环境，使用默认后端")
            except NameError:
                # 不在IPython中，使用Agg后端
                matplotlib.use('Agg')
                print("✅ 使用Agg后端（非GUI环境）")
        else:
            # 命令行环境，使用Agg后端避免GUI问题
            matplotlib.use('Agg')
            print("✅ 使用Agg后端（命令行环境）")
    except Exception as e:
        # 如果检测失败，默认使用Agg后端
        matplotlib.use('Agg')
        print(f"⚠️ 后端检测失败，使用默认Agg后端: {e}")

# 设置后端
setup_matplotlib_backend()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体 - 修复版本
def setup_chinese_fonts():
    """设置中文字体显示"""
    import matplotlib.font_manager as fm
    
    # 检测可用字体
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    # 中文字体优先级列表
    chinese_fonts = [
        'Microsoft YaHei',  # 微软雅黑
        'SimHei',           # 黑体
        'SimSun',           # 宋体
        'KaiTi',            # 楷体
        'FangSong',         # 仿宋
        'DejaVu Sans'       # 备用字体
    ]
    
    # 选择第一个可用的字体
    selected_font = 'DejaVu Sans'  # 默认备用字体
    for font in chinese_fonts:
        if font in available_fonts:
            selected_font = font
            break
    
    # 配置matplotlib
    plt.rcParams['font.sans-serif'] = [selected_font]
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.family'] = 'sans-serif'
    
    print(f"✅ 已配置中文字体: {selected_font}")
    return selected_font

# 检测Jupyter环境的函数
def is_jupyter_environment():
    """检测是否在Jupyter环境中"""
    try:
        get_ipython()
        return True
    except NameError:
        return False

def display_plot_in_jupyter():
    """在Jupyter中显示图表"""
    if is_jupyter_environment():
        plt.show()
        return True
    return False

# 调用字体设置
setup_chinese_fonts()

# 设置图表样式 - 兼容Python 3.7
sns.set_style("whitegrid")
try:
    plt.style.use('seaborn-v0_8')
except OSError:
    # 如果seaborn-v0_8不可用，使用默认样式
    try:
        plt.style.use('seaborn')
    except OSError:
        # 如果seaborn也不可用，使用默认样式
        pass


class StockDataVisualizer:
    """股票数据可视化器"""
    
    def __init__(self, output_dir='./results/charts'):
        """
        初始化可视化器
        
        Args:
            output_dir (str): 图表输出目录
        """
        self.output_dir = output_dir
        self.ensure_dir_exists()
        
        # 检测是否在Jupyter环境中
        self.in_jupyter = is_jupyter_environment()
        if self.in_jupyter:
            print("📱 检测到Jupyter环境，图表将直接显示")
        
        # 定义颜色方案
        self.colors = {
            '上海交易所': '#FF6B6B',
            '深圳交易所': '#4ECDC4', 
            '北京交易所': '#45B7D1',
            '主板': '#96CEB4',
            '科创板': '#FFEAA7',
            '创业板': '#DDA0DD',
            '中小板': '#98D8C8'
        }
        
    def ensure_dir_exists(self):
        """确保输出目录存在"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _save_and_show(self, save_path, chart_name):
        """保存图表并在Jupyter中显示"""
        # 先在Jupyter中显示图表
        if self.in_jupyter:
            plt.show()
        
        # 然后保存图表
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"{chart_name}已保存到: {save_path}")
        
        # 保存完成后立即关闭图形以释放内存，避免重复显示
        plt.close()
    
    def plot_exchange_distribution(self, exchange_data, save_path=None):
        """
        绘制交易所分布图
        
        Args:
            exchange_data (dict): 交易所统计数据字典，格式如 {'上海交易所': 1000, '深圳交易所': 800}
            save_path (str): 保存路径
        """
        if not exchange_data:
            print("缺少交易所统计数据")
            return
        
        # 清除之前的图形
        plt.clf()
        plt.close('all')
        
        # 创建子图
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 1. 柱状图
        exchanges = list(exchange_data.keys())
        counts = list(exchange_data.values())
        colors = [self.colors.get(ex, '#95A5A6') for ex in exchanges]
        
        bars = ax1.bar(exchanges, counts, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
        ax1.set_title('各交易所上市公司数量', fontsize=16, fontweight='bold', pad=20)
        ax1.set_ylabel('上市公司数量', fontsize=12)
        ax1.set_xlabel('交易所', fontsize=12)
        
        # 在柱状图上添加数值标签
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + max(counts)*0.01,
                    f'{count}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # 2. 饼图
        wedges, texts, autotexts = ax2.pie(counts, labels=exchanges, colors=colors, 
                                          autopct='%1.1f%%', startangle=90,
                                          textprops={'fontsize': 10})
        ax2.set_title('各交易所上市公司占比', fontsize=16, fontweight='bold', pad=20)
        
        # 美化饼图文本
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        plt.tight_layout()
        
        # 设置保存路径
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.output_dir, f"exchange_distribution_{timestamp}.png")
        
        # 保存并显示
        self._save_and_show(save_path, "交易所分布图")
        
        return fig
    
    def plot_board_distribution(self, board_data, save_path=None):
        """
        绘制板块分布图
        
        Args:
            board_data (dict): 板块统计数据字典，格式如 {'主板': 2000, '科创板': 500}
            save_path (str): 保存路径
        """
        if not board_data:
            print("缺少板块统计数据")
            return
        
        # 清除之前的图形
        plt.clf()
        plt.close('all')
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(12, 8))
        
        boards = list(board_data.keys())
        counts = list(board_data.values())
        colors = [self.colors.get(board, '#95A5A6') for board in boards]
        
        # 水平柱状图
        bars = ax.barh(boards, counts, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
        
        ax.set_title('各板块上市公司数量分布', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('上市公司数量', fontsize=12)
        ax.set_ylabel('板块', fontsize=12)
        
        # 添加数值标签
        for bar, count in zip(bars, counts):
            width = bar.get_width()
            ax.text(width + max(counts)*0.01, bar.get_y() + bar.get_height()/2.,
                   f'{count}', ha='left', va='center', fontsize=11, fontweight='bold')
        
        plt.tight_layout()
        
        # 设置保存路径
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.output_dir, f"board_distribution_{timestamp}.png")
        
        # 保存并显示
        self._save_and_show(save_path, "板块分布图")
        
        return fig
    
    def plot_cross_analysis(self, stats_data, save_path=None):
        """
        绘制交易所与板块交叉分析图
        
        Args:
            stats_data (dict): 统计数据
            save_path (str): 保存路径
        """
        if '交易所板块交叉统计' not in stats_data:
            print("缺少交叉统计数据")
            return
        
        cross_data = stats_data['交易所板块交叉统计']
        cross_df = pd.DataFrame(cross_data).fillna(0)
        
        # 创建热力图
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # 绘制热力图
        sns.heatmap(cross_df, annot=True, fmt='g', cmap='YlOrRd', 
                   cbar_kws={'label': '上市公司数量'}, ax=ax,
                   linewidths=0.5, linecolor='white')
        
        ax.set_title('交易所与板块交叉分析热力图', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('板块', fontsize=12)
        ax.set_ylabel('交易所', fontsize=12)
        
        # 旋转x轴标签
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        
        plt.tight_layout()
        
        # 设置保存路径
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.output_dir, f"cross_analysis_{timestamp}.png")
        
        # 保存并显示
        self._save_and_show(save_path, "交叉分析图")
        
        return fig
    
    def plot_cross_analysis_heatmap(self, cross_df, save_path=None):
        """
        绘制交易所与板块交叉分析热力图
        
        Args:
            cross_df (pd.DataFrame): 交叉统计DataFrame
            save_path (str): 保存路径
        """
        if cross_df.empty:
            print("缺少交叉统计数据")
            return
        
        # 创建热力图
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # 绘制热力图
        sns.heatmap(cross_df, annot=True, fmt='g', cmap='YlOrRd', 
                   cbar_kws={'label': '上市公司数量'}, ax=ax,
                   linewidths=0.5, linecolor='white')
        
        ax.set_title('交易所与板块交叉分析热力图', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('板块', fontsize=12)
        ax.set_ylabel('交易所', fontsize=12)
        
        # 旋转x轴标签
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        
        plt.tight_layout()
        
        # 设置保存路径
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.output_dir, f"cross_analysis_heatmap_{timestamp}.png")
        
        # 保存并显示
        self._save_and_show(save_path, "交叉分析热力图")
        
        return fig
    
    def plot_industry_distribution(self, industry_data, top_n=15, save_path=None):
        """
        绘制行业分布图
        
        Args:
            industry_data (dict): 行业统计数据字典，格式如 {'制造业': 1000, '金融业': 500}
            top_n (int): 显示前N个行业
            save_path (str): 保存路径
        """
        if not industry_data:
            print("缺少行业分布数据")
            return
        
        # 获取前N个行业
        sorted_industries = sorted(industry_data.items(), key=lambda x: x[1], reverse=True)[:top_n]
        industries = [item[0] for item in sorted_industries]
        counts = [item[1] for item in sorted_industries]
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # 使用渐变色
        colors = plt.cm.Set3(np.linspace(0, 1, len(industries)))
        
        bars = ax.bar(range(len(industries)), counts, color=colors, alpha=0.8, 
                     edgecolor='black', linewidth=1)
        
        ax.set_title(f'前{top_n}个行业上市公司数量分布', fontsize=16, fontweight='bold', pad=20)
        ax.set_ylabel('上市公司数量', fontsize=12)
        ax.set_xlabel('行业', fontsize=12)
        ax.set_xticks(range(len(industries)))
        ax.set_xticklabels(industries, rotation=45, ha='right')
        
        # 添加数值标签
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(counts)*0.01,
                   f'{count}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        
        # 设置保存路径
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.output_dir, f"industry_distribution_{timestamp}.png")
        
        # 保存并显示
        self._save_and_show(save_path, "行业分布图")
        
        return fig
    
    def create_interactive_dashboard(self, stats_data, industry_stats=None):
        """
        创建交互式仪表板
        
        Args:
            stats_data (dict): 统计数据
            industry_stats (dict): 行业统计数据
        """
        # 创建子图
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('交易所分布', '板块分布', '交易所板块交叉分析', '行业分布'),
            specs=[[{"type": "pie"}, {"type": "bar"}],
                   [{"type": "heatmap"}, {"type": "bar"}]]
        )
        
        # 1. 交易所饼图
        if '按交易所统计' in stats_data:
            exchange_data = stats_data['按交易所统计']
            fig.add_trace(
                go.Pie(labels=list(exchange_data.keys()), 
                      values=list(exchange_data.values()),
                      name="交易所分布"),
                row=1, col=1
            )
        
        # 2. 板块柱状图
        if '按板块统计' in stats_data:
            board_data = stats_data['按板块统计']
            fig.add_trace(
                go.Bar(x=list(board_data.keys()), 
                      y=list(board_data.values()),
                      name="板块分布"),
                row=1, col=2
            )
        
        # 更新布局
        fig.update_layout(
            title_text="中国股票市场数据分析仪表板",
            title_x=0.5,
            height=800,
            showlegend=False
        )
        
        # 保存交互式图表
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        html_path = os.path.join(self.output_dir, f"interactive_dashboard_{timestamp}.html")
        fig.write_html(html_path)
        print(f"交互式仪表板已保存到: {html_path}")
        
        return fig
    
    def generate_all_charts(self, processed_data):
        """
        生成所有图表
        
        Args:
            processed_data (dict): 处理后的数据
        """
        print("开始生成可视化图表...")
        print("=" * 50)
        
        if 'statistics' in processed_data:
            stats = processed_data['statistics']
            
            # 1. 交易所分布图
            self.plot_exchange_distribution(stats['按交易所统计'])
            
            # 2. 板块分布图
            self.plot_board_distribution(stats['按板块统计'])
            
            # 3. 交叉分析图
            self.plot_cross_analysis(stats)
        
        # 4. 行业分布图
        if 'industry_analysis' in processed_data:
            industry_stats = processed_data['industry_analysis']
            if industry_stats:
                self.plot_industry_distribution(industry_stats)
        
        # 5. 交互式仪表板
        if 'statistics' in processed_data:
            self.create_interactive_dashboard(
                processed_data['statistics'],
                processed_data.get('industry_analysis')
            )
        
        print("=" * 50)
        print("所有图表生成完成！")


def main():
    """主函数，用于测试可视化功能"""
    # 创建测试数据
    test_stats = {
        '按交易所统计': {
            '上海交易所': 1800,
            '深圳交易所': 2500,
            '北京交易所': 120
        },
        '按板块统计': {
            '主板': 3000,
            '创业板': 1000,
            '科创板': 400,
            '中小板': 20
        },
        '交易所板块交叉统计': {
            '主板': {'上海交易所': 1800, '深圳交易所': 1200, '北京交易所': 0},
            '科创板': {'上海交易所': 400, '深圳交易所': 0, '北京交易所': 0},
            '创业板': {'上海交易所': 0, '深圳交易所': 1000, '北京交易所': 0},
            '中小板': {'上海交易所': 0, '深圳交易所': 20, '北京交易所': 0}
        }
    }
    
    test_industry = {
        '总体行业分布': {
            '制造业': 800,
            '信息技术': 600,
            '金融业': 400,
            '房地产': 300,
            '医药生物': 250
        }
    }
    
    # 创建可视化器并生成图表
    visualizer = StockDataVisualizer()
    
    test_data = {
        'statistics': test_stats,
        'industry_analysis': test_industry
    }
    
    visualizer.generate_all_charts(test_data)


if __name__ == "__main__":
    main() 