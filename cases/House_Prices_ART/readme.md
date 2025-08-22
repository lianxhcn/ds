参考代码：

- [Ensemble Stacking 示例](https://www.kaggle.com/code/chikonzeroselemani/ensemble-stacking)
- 前期数据分析：[Comprehensive data exploration with Python](https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python/input)

# 房价预测竞赛数据集简介

本项目数据源自 Kaggle 平台的 “房价预测：高级回归技术（House Prices: Advanced Regression Techniques）” 竞赛，广泛用于回归建模、特征工程和数据科学教学。

## 1. 项目背景

目标：根据爱荷华州埃姆斯市住宅特征，建立回归模型预测房屋售价。

## 2. 数据简介

- **训练集（train.csv）**：1460 条带房价样本
- **测试集（test.csv）**：1459 条无房价样本

每条记录包含 79 个特征变量，目标变量为 SalePrice（仅训练集）。

## 3. 主要变量说明

- **Id**：唯一标识
- **MSSubClass**：建筑类别
- **MSZoning**：区域类型
- **LotFrontage**：临街长度
- **LotArea**：土地面积
- **OverallQual**：整体质量评分
- **OverallCond**：整体状况评分
- **YearBuilt**：建造年份
- **GrLivArea**：地面以上居住面积
- **GarageCars**：车库容量
- **SalePrice**：房屋售价（目标变量，仅训练集）

完整变量说明见 `data_description.txt`。

## 4. 文件结构

- `train.csv`：训练数据
- `test.csv`：测试数据
- `data_description.txt`：变量说明
- `sample_submission.csv`：提交格式示例

## 5. 分析流程建议

1. **数据读取与初步查看**：使用 pandas 导入数据，查看结构与缺失值。
2. **数据清洗与特征工程**：处理缺失值、类别编码、归一化、新特征构建。
3. **建模与预测**：常用模型有线性回归、Lasso、随机森林、梯度提升树等。
4. **模型评估**：推荐 RMSE 等回归指标。
5. **结果提交**：按 `sample_submission.csv` 格式准备预测结果。

## 6. 参考资料

- [竞赛主页（Kaggle）](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
- [数据说明文档](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
- [Ames 房价原始数据论文](https://doi.org/10.1080/10691898.2011.11889627)

## 7. 版权声明

本数据集仅供教学与学术用途，禁止商业使用。原始数据由 Dean De Cock 教授整理。

## 推荐 Jupyter Notebook

- [House Prices Prediction using TFDF](https://www.kaggle.com/code/gusthema/house-prices-prediction-using-tfdf)
- [Comprehensive data exploration with Python](https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python)
- [Stacked Regressions: Top 4% on LeaderBoard](https://www.kaggle.com/code/serigne/stacked-regressions-top-4-on-leaderboard)
- [Regularized Linear Models](https://www.kaggle.com/code/apapiu/regularized-linear-models)
- [House prices: Lasso, XGBoost, and a detailed EDA](https://www.kaggle.com/code/erikbruin/house-prices-lasso-xgboost-and-a-detailed-eda)
- [Submitting From A Kernel](https://www.kaggle.com/code/dansbecker/submitting-from-a-kernel)
- [Handling Missing Values](https://www.kaggle.com/code/dansbecker/handling-missing-values)
- [Using Categorical Data with One Hot Encoding](https://www.kaggle.com/code/dansbecker/using-categorical-data-with-one-hot-encoding)
- [A study on Regression applied to the Ames dataset](https://www.kaggle.com/code/juliencs/a-study-on-regression-applied-to-the-ames-dataset)
- [A Detailed Regression Guide with House-pricing](https://www.kaggle.com/code/masumrumi/a-detailed-regression-guide-with-house-pricing)
