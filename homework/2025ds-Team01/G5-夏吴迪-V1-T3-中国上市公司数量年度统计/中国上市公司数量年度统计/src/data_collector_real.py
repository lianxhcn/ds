"""
中国股票市场真实数据收集模块
使用akshare库获取真实的各交易所上市公司数据
适用于Python 3.10+
"""

import akshare as ak
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import os
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')


class RealStockDataCollector:
    """真实股票数据收集器"""
    
    def __init__(self, data_dir='../data/raw'):
        """
        初始化数据收集器
        
        Args:
            data_dir (str): 数据存储目录
        """
        self.data_dir = data_dir
        self.ensure_dir_exists()
        
    def ensure_dir_exists(self):
        """确保数据目录存在"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def get_stock_list_all(self):
        """
        获取所有上市公司基本信息（真实数据）
        
        Returns:
            pd.DataFrame: 包含所有上市公司信息的DataFrame
        """
        print("正在获取所有上市公司基本信息...")
        try:
            # 获取所有A股上市公司信息
            stock_info = ak.stock_info_a_code_name()
            
            # 保存原始数据
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stock_list_all_real_{timestamp}.csv"
            filepath = os.path.join(self.data_dir, filename)
            stock_info.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"真实数据已保存到: {filepath}")
            
            return stock_info
            
        except Exception as e:
            print(f"获取股票列表失败: {e}")
            return pd.DataFrame()
    
    def get_stock_list_by_exchange(self):
        """
        分别获取各交易所的股票列表（真实数据）
        
        Returns:
            dict: 包含各交易所股票列表的字典
        """
        exchanges_data = {}
        
        # 上海交易所
        print("正在获取上海交易所股票列表...")
        try:
            sh_stocks = ak.stock_sh_a_spot_em()
            exchanges_data['上海交易所'] = sh_stocks
            
            # 保存数据
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stock_list_sh_real_{timestamp}.csv"
            filepath = os.path.join(self.data_dir, filename)
            sh_stocks.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"上海交易所真实数据已保存: {len(sh_stocks)} 只股票")
            
        except Exception as e:
            print(f"获取上海交易所数据失败: {e}")
            exchanges_data['上海交易所'] = pd.DataFrame()
        
        # 深圳交易所
        print("正在获取深圳交易所股票列表...")
        try:
            sz_stocks = ak.stock_sz_a_spot_em()
            exchanges_data['深圳交易所'] = sz_stocks
            
            # 保存数据
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stock_list_sz_real_{timestamp}.csv"
            filepath = os.path.join(self.data_dir, filename)
            sz_stocks.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"深圳交易所真实数据已保存: {len(sz_stocks)} 只股票")
            
        except Exception as e:
            print(f"获取深圳交易所数据失败: {e}")
            exchanges_data['深圳交易所'] = pd.DataFrame()
        
        # 北京交易所
        print("正在获取北京交易所股票列表...")
        try:
            bj_stocks = ak.stock_bj_a_spot_em()
            exchanges_data['北京交易所'] = bj_stocks
            
            # 保存数据
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stock_list_bj_real_{timestamp}.csv"
            filepath = os.path.join(self.data_dir, filename)
            bj_stocks.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"北京交易所真实数据已保存: {len(bj_stocks)} 只股票")
            
        except Exception as e:
            print(f"获取北京交易所数据失败: {e}")
            exchanges_data['北京交易所'] = pd.DataFrame()
        
        return exchanges_data
    
    def get_stock_board_concept(self):
        """
        获取股票板块和概念信息（真实数据）
        
        Returns:
            dict: 包含各种板块信息的字典
        """
        board_data = {}
        
        # 获取行业板块信息
        print("正在获取行业板块信息...")
        try:
            industry_data = ak.stock_board_industry_name_em()
            board_data['行业板块'] = industry_data
            
            # 保存数据
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"industry_board_real_{timestamp}.csv"
            filepath = os.path.join(self.data_dir, filename)
            industry_data.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"行业板块真实数据已保存: {len(industry_data)} 个行业")
            
        except Exception as e:
            print(f"获取行业板块信息失败: {e}")
            board_data['行业板块'] = pd.DataFrame()
        
        return board_data
    
    def get_stock_industry_detail(self, industry_name):
        """
        获取特定行业的股票详细信息（真实数据）
        
        Args:
            industry_name (str): 行业名称
            
        Returns:
            pd.DataFrame: 该行业的股票信息
        """
        try:
            industry_stocks = ak.stock_board_industry_cons_em(symbol=industry_name)
            return industry_stocks
        except Exception as e:
            print(f"获取行业 {industry_name} 详细信息失败: {e}")
            return pd.DataFrame()
    
    def get_additional_stock_info(self):
        """
        获取额外的股票信息（IPO信息、财务数据等）
        
        Returns:
            dict: 包含额外信息的字典
        """
        additional_data = {}
        
        # 获取IPO信息
        print("正在获取IPO信息...")
        try:
            ipo_data = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="20240101", end_date="20241231", period="daily", adjust="")
            additional_data['ipo_info'] = ipo_data
            print(f"IPO信息获取成功")
        except Exception as e:
            print(f"获取IPO信息失败: {e}")
            additional_data['ipo_info'] = pd.DataFrame()
        
        return additional_data
    
    def collect_all_data(self):
        """
        收集所有需要的真实数据
        
        Returns:
            dict: 包含所有收集数据的字典
        """
        print("开始收集中国股票市场真实数据...")
        print("=" * 50)
        print("📈 使用akshare获取最新真实市场数据")
        print("=" * 50)
        
        all_data = {}
        
        # 1. 获取所有股票列表
        print("\n🔍 步骤1: 获取所有股票基本信息")
        all_data['all_stocks'] = self.get_stock_list_all()
        time.sleep(2)  # 避免请求过于频繁
        
        # 2. 获取各交易所股票列表
        print("\n🔍 步骤2: 获取各交易所股票列表")
        all_data['exchanges'] = self.get_stock_list_by_exchange()
        time.sleep(2)
        
        # 3. 获取板块信息
        print("\n🔍 步骤3: 获取板块信息")
        all_data['boards'] = self.get_stock_board_concept()
        time.sleep(2)
        
        # 4. 获取额外信息
        print("\n🔍 步骤4: 获取额外信息")
        # all_data['additional'] = self.get_additional_stock_info()  # 暂时注释，避免过多请求
        
        print("=" * 50)
        print("✅ 真实数据收集完成！")
        
        return all_data


def main():
    """主函数，用于测试真实数据收集功能"""
    print("🚀 启动真实股票数据收集器")
    print("=" * 60)
    
    collector = RealStockDataCollector(data_dir='./data/raw')
    data = collector.collect_all_data()
    
    # 打印数据概览
    print("\n📊 真实数据收集结果概览:")
    print("-" * 40)
    
    if not data['all_stocks'].empty:
        print(f"✅ 全部上市公司数量: {len(data['all_stocks'])}")
        print(f"📋 数据列: {list(data['all_stocks'].columns)}")
    
    for exchange, df in data['exchanges'].items():
        if not df.empty:
            print(f"✅ {exchange}上市公司数量: {len(df)}")
    
    if 'boards' in data and '行业板块' in data['boards'] and not data['boards']['行业板块'].empty:
        print(f"✅ 行业板块数量: {len(data['boards']['行业板块'])}")
    
    print("\n🎉 真实数据收集完成！")
    print("📁 数据文件已保存到 ./data/raw/ 目录")


if __name__ == "__main__":
    main() 