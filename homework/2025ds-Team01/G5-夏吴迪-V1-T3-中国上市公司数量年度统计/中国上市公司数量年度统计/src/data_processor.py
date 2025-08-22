"""
中国股票市场数据处理模块
对收集的数据进行清洗、分类和统计分析
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import re
from collections import defaultdict


class StockDataProcessor:
    """股票数据处理器"""
    
    def __init__(self, raw_data_dir='../data/raw', processed_data_dir='../data/processed'):
        """
        初始化数据处理器
        
        Args:
            raw_data_dir (str): 原始数据目录
            processed_data_dir (str): 处理后数据目录
        """
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        self.ensure_dir_exists()
        
        # 板块分类映射
        self.board_mapping = {
            '主板': ['60', '000', '001'],  # 上海主板、深圳主板
            '科创板': ['688'],
            '创业板': ['300'],
            '中小板': ['002'],  # 注：中小板已并入主板，但历史数据仍需分类
            '北交所': ['8', '4']  # 北交所股票代码
        }
        
    def ensure_dir_exists(self):
        """确保处理后数据目录存在"""
        if not os.path.exists(self.processed_data_dir):
            os.makedirs(self.processed_data_dir)
    
    def classify_stock_by_code(self, stock_code):
        """
        根据股票代码分类股票所属板块
        
        Args:
            stock_code (str): 股票代码
            
        Returns:
            tuple: (交易所, 板块)
        """
        if pd.isna(stock_code):
            return '未知', '未知'
            
        code_str = str(stock_code).zfill(6)  # 确保6位数字
        
        # 上海交易所
        if code_str.startswith('60'):
            return '上海交易所', '主板'
        elif code_str.startswith('688') or code_str.startswith('689'):
            # 688xxx: 科创板主要代码
            # 689xxx: 科创板特殊代码（如689009九号公司等存托凭证）
            return '上海交易所', '科创板'
        
        # 深圳交易所
        elif code_str.startswith('000') or code_str.startswith('001'):
            return '深圳交易所', '主板'
        elif code_str.startswith('002'):
            return '深圳交易所', '中小板'
        elif (code_str.startswith('300') or code_str.startswith('003') or 
              code_str.startswith('301') or code_str.startswith('302')):
            # 300xxx: 创业板原有代码
            # 003xxx: 创业板注册制改革后的新代码（2020年起）
            # 301xxx: 创业板注册制改革后的新代码（2020年起）
            # 302xxx: 创业板注册制改革后的新代码（2020年起）
            return '深圳交易所', '创业板'
        
        # 北京交易所
        elif (code_str.startswith('8') or code_str.startswith('4') or 
              code_str.startswith('92')):
            # 8xxxxx: 北交所主要代码
            # 4xxxxx: 北交所代码
            # 92xxxx: 北交所特殊代码
            return '北京交易所', '北交所板块'
        
        else:
            return '其他', '其他'
    
    def analyze_by_exchange(self, stock_data):
        """
        按交易所分析股票分布
        
        Args:
            stock_data (pd.DataFrame): 股票数据
            
        Returns:
            dict: 各交易所股票数量统计
        """
        if stock_data.empty:
            return {}
        
        # 处理数据，添加分类信息
        processed_data = self.process_stock_list(stock_data)
        
        # 统计各交易所数量
        exchange_stats = processed_data['交易所'].value_counts().to_dict()
        
        # 移除未知项
        if '未知' in exchange_stats:
            del exchange_stats['未知']
        if '其他' in exchange_stats:
            del exchange_stats['其他']
            
        return exchange_stats
    
    def analyze_by_board(self, stock_data):
        """
        按板块分析股票分布
        
        Args:
            stock_data (pd.DataFrame): 股票数据
            
        Returns:
            dict: 各板块股票数量统计
        """
        if stock_data.empty:
            return {}
        
        # 处理数据，添加分类信息
        processed_data = self.process_stock_list(stock_data)
        
        # 统计各板块数量
        board_stats = processed_data['板块'].value_counts().to_dict()
        
        # 移除未知项
        if '未知' in board_stats:
            del board_stats['未知']
        if '其他' in board_stats:
            del board_stats['其他']
            
        return board_stats
    
    def analyze_by_industry(self, stock_data):
        """
        按行业分析股票分布
        
        Args:
            stock_data (pd.DataFrame): 股票数据
            
        Returns:
            dict: 各行业股票数量统计
        """
        if stock_data.empty:
            return {}
        
        # 处理数据，添加分类信息
        processed_data = self.process_stock_list(stock_data)
        
        # 查找行业列
        industry_column = None
        for col in ['行业', 'industry', '所属行业', '申万行业']:
            if col in processed_data.columns:
                industry_column = col
                break
        
        if industry_column is None:
            print("警告：未找到行业信息列，返回空统计")
            return {}
        
        # 统计各行业数量
        industry_stats = processed_data[industry_column].value_counts().to_dict()
        
        return industry_stats
    
    def generate_cross_statistics(self, stock_data):
        """
        生成交易所与板块的交叉统计
        
        Args:
            stock_data (pd.DataFrame): 股票数据
            
        Returns:
            pd.DataFrame: 交叉统计表
        """
        if stock_data.empty:
            return pd.DataFrame()
        
        # 处理数据，添加分类信息
        processed_data = self.process_stock_list(stock_data)
        
        # 过滤掉未知项
        processed_data = processed_data[
            (processed_data['交易所'] != '未知') & 
            (processed_data['交易所'] != '其他') &
            (processed_data['板块'] != '未知') & 
            (processed_data['板块'] != '其他')
        ]
        
        # 生成交叉统计表
        cross_stats = processed_data.groupby(['交易所', '板块']).size().unstack(fill_value=0)
        
        return cross_stats
    
    def process_stock_list(self, stock_data):
        """
        处理股票列表数据，添加分类信息
        
        Args:
            stock_data (pd.DataFrame): 原始股票数据
            
        Returns:
            pd.DataFrame: 处理后的股票数据
        """
        if stock_data.empty:
            return stock_data
        
        # 复制数据避免修改原始数据
        processed_data = stock_data.copy()
        
        # 确保有股票代码列
        code_column = None
        for col in ['code', '代码', 'symbol', '股票代码']:
            if col in processed_data.columns:
                code_column = col
                break
        
        if code_column is None:
            print("警告：未找到股票代码列")
            return processed_data
        
        # 添加分类信息
        classifications = processed_data[code_column].apply(self.classify_stock_by_code)
        processed_data['交易所'] = [cls[0] for cls in classifications]
        processed_data['板块'] = [cls[1] for cls in classifications]
        
        return processed_data
    
    def generate_annual_statistics(self, stock_data):
        """
        生成年度统计数据
        
        Args:
            stock_data (pd.DataFrame): 处理后的股票数据
            
        Returns:
            dict: 包含各种统计信息的字典
        """
        if stock_data.empty:
            return {}
        
        stats = {}
        
        # 总体统计
        stats['总计'] = {
            '上市公司总数': len(stock_data),
            '更新时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 按交易所统计
        exchange_stats = stock_data['交易所'].value_counts().to_dict()
        stats['按交易所统计'] = exchange_stats
        
        # 按板块统计
        board_stats = stock_data['板块'].value_counts().to_dict()
        stats['按板块统计'] = board_stats
        
        # 交叉统计：交易所 x 板块
        cross_stats = stock_data.groupby(['交易所', '板块']).size().unstack(fill_value=0)
        stats['交易所板块交叉统计'] = cross_stats.to_dict()
        
        return stats
    
    def analyze_industry_distribution(self, stock_data, industry_data=None):
        """
        分析行业分布
        
        Args:
            stock_data (pd.DataFrame): 股票数据
            industry_data (pd.DataFrame): 行业数据
            
        Returns:
            dict: 行业分布统计
        """
        industry_stats = {}
        
        # 如果有行业信息列，直接统计
        industry_columns = ['行业', 'industry', '所属行业', '申万行业']
        industry_column = None
        
        for col in industry_columns:
            if col in stock_data.columns:
                industry_column = col
                break
        
        if industry_column:
            # 总体行业分布
            industry_dist = stock_data[industry_column].value_counts()
            industry_stats['总体行业分布'] = industry_dist.to_dict()
            
            # 按交易所的行业分布
            for exchange in stock_data['交易所'].unique():
                if exchange != '未知':
                    exchange_data = stock_data[stock_data['交易所'] == exchange]
                    exchange_industry = exchange_data[industry_column].value_counts()
                    industry_stats[f'{exchange}行业分布'] = exchange_industry.to_dict()
        
        return industry_stats
    
    def create_summary_tables(self, stats_data):
        """
        创建汇总表格
        
        Args:
            stats_data (dict): 统计数据
            
        Returns:
            dict: 包含各种汇总表格的字典
        """
        tables = {}
        
        # 1. 交易所统计表
        if '按交易所统计' in stats_data:
            exchange_df = pd.DataFrame(list(stats_data['按交易所统计'].items()), 
                                     columns=['交易所', '上市公司数量'])
            exchange_df = exchange_df.sort_values('上市公司数量', ascending=False)
            tables['交易所统计'] = exchange_df
        
        # 2. 板块统计表
        if '按板块统计' in stats_data:
            board_df = pd.DataFrame(list(stats_data['按板块统计'].items()), 
                                  columns=['板块', '上市公司数量'])
            board_df = board_df.sort_values('上市公司数量', ascending=False)
            tables['板块统计'] = board_df
        
        # 3. 交易所板块详细统计表
        if '交易所板块交叉统计' in stats_data:
            cross_data = stats_data['交易所板块交叉统计']
            cross_df = pd.DataFrame(cross_data).fillna(0).astype(int)
            tables['交易所板块详细统计'] = cross_df
        
        return tables
    
    def save_processed_data(self, data, filename_prefix):
        """
        保存处理后的数据
        
        Args:
            data: 要保存的数据
            filename_prefix (str): 文件名前缀
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if isinstance(data, pd.DataFrame):
            filename = f"{filename_prefix}_{timestamp}.csv"
            filepath = os.path.join(self.processed_data_dir, filename)
            data.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"数据已保存到: {filepath}")
            
        elif isinstance(data, dict):
            # 如果是字典，保存为多个文件或JSON
            for key, value in data.items():
                if isinstance(value, pd.DataFrame):
                    filename = f"{filename_prefix}_{key}_{timestamp}.csv"
                    filepath = os.path.join(self.processed_data_dir, filename)
                    value.to_csv(filepath, index=False, encoding='utf-8-sig')
                    print(f"{key}数据已保存到: {filepath}")
    
    def process_all_data(self, raw_data):
        """
        处理所有原始数据
        
        Args:
            raw_data (dict): 原始数据字典
            
        Returns:
            dict: 处理后的数据和统计结果
        """
        print("开始处理股票数据...")
        print("=" * 50)
        
        processed_results = {}
        
        # 1. 处理所有股票数据
        if 'all_stocks' in raw_data and not raw_data['all_stocks'].empty:
            print("处理全部股票数据...")
            processed_stocks = self.process_stock_list(raw_data['all_stocks'])
            processed_results['processed_stocks'] = processed_stocks
            
            # 生成统计数据
            stats = self.generate_annual_statistics(processed_stocks)
            processed_results['statistics'] = stats
            
            # 生成汇总表格
            tables = self.create_summary_tables(stats)
            processed_results['summary_tables'] = tables
            
            # 分析行业分布
            industry_stats = self.analyze_industry_distribution(processed_stocks)
            processed_results['industry_analysis'] = industry_stats
            
            # 保存处理后的数据
            self.save_processed_data(processed_stocks, "processed_all_stocks")
            self.save_processed_data(tables, "summary_tables")
        
        # 2. 处理各交易所数据
        if 'exchanges' in raw_data:
            print("处理各交易所数据...")
            exchange_processed = {}
            for exchange, data in raw_data['exchanges'].items():
                if not data.empty:
                    processed_exchange_data = self.process_stock_list(data)
                    exchange_processed[exchange] = processed_exchange_data
                    
                    # 保存各交易所处理后的数据
                    self.save_processed_data(processed_exchange_data, f"processed_{exchange}")
            
            processed_results['exchanges_processed'] = exchange_processed
        
        print("=" * 50)
        print("数据处理完成！")
        
        return processed_results


def main():
    """主函数，用于测试数据处理功能"""
    # 这里可以加载一些测试数据进行处理
    processor = StockDataProcessor()
    
    # 创建测试数据
    test_data = {
        'all_stocks': pd.DataFrame({
            'code': ['600000', '000001', '300001', '688001', '830001'],
            'name': ['浦发银行', '平安银行', '特锐德', '华兴源创', '庆汇租赁'],
        })
    }
    
    # 处理测试数据
    results = processor.process_all_data(test_data)
    
    # 打印结果
    if 'statistics' in results:
        print("\n统计结果:")
        for key, value in results['statistics'].items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main() 