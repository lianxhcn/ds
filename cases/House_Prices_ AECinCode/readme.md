
## 简介

> Stanislava Fedorova. [House Prices | AECinCode](https://kaggle.com/competitions/aecincode_houseprices), 2025. Kaggle.

- Source: [Kaggle - House Prices | AECinCode](https://www.kaggle.com/competitions/aecincode_houseprices/overview)
- Data: 1.96M, 1460 samples, 79 features, [详情](https://www.kaggle.com/competitions/aecincode_houseprices/data)

这是 Kaggle 上的一个房价预测比赛，数据集包含了 1460 个样本和 79 个特征。目标是预测房屋的销售价格。数据集中的特征包括房屋的面积、卧室数量、卫生间数量、车库数量等。数据集中的目标变量是房屋的销售价格。

> Note: 建议在开始这个项目之前，先看看更早的一个明星项目：
> Anna Montoya and DataCanary. [House Prices - Advanced Regression Techniques](https://kaggle.com/competitions/house-prices-advanced-regression-techniques), 2016. Kaggle. 该项目主页提供了数据分析、机器学习等相关教程。同时，自该项目设立以来，已有超过 4700 支队伍参与过这个项目，累计参与人数超过 25000 人。该项目的主页上有大量的讨论和代码示例，供大家参考。
> - [Hot-notebook: House Prices Prediction using TFDF](https://www.kaggle.com/code/gusthema/house-prices-prediction-using-tfdf/notebook)

What's the secret sauce behind a home's price? It's not just about fancy kitchens or a backyard---sometimes, the quirkiest details make all the difference. In this competition, you'll dive into a real-world dataset from Ames, Iowa, packed with 79 features that shape housing prices in unexpected ways. Your mission: uncover hidden patterns, engineer clever features, and build a sharp regression model to predict prices like a pro. Whether you're team random forest or all-in on gradient boosting, it's time to put your skills to the test. Ready to crack the code? Let's get started!

**Goal:**

The goal is simple: build a predictive model that accurately estimates home sale prices in Ames, Iowa by uncovering hidden patterns in the dataset. You'll need to analyze all 79 features---from obvious factors like square footage to subtle influences like neighborhood zoning---and engineer the best approach to beat the competition. The most accurate predictions win.

## Recommendations for the educators

-   This competition can be used to teach data cleaning, EDA and regression techiniques. I used it for teaching model evaluation, metrics and hyperparameter tuning
-   Go through the sample [notebook](https://github.com/STASYA00/AECinCode_tutorials/blob/main/notebooks/model_evaluation.ipynb) together with the students, making sure they understand how to download the data and upload the submission:)
-   Give this task to the students already more or less comfortable with programming. Teaching programming on a kaggle competition proved to be a bad idea.
-   Keep it short and sweet - max. 2 weeks

## Recommendations for the students

-   Use the framework we have seen during the course to solve the homework (pandas, sklearn).
-   Use Colab to write and run the code.
-   [Notebook](https://github.com/STASYA00/AECinCode_tutorials/blob/main/notebooks/model_evaluation.ipynb) to get you started
-   Save all the code you write on Github, then you will most certainly avoid the risk of losing your precious work.
-   Organize your code following the approach shown during the lab sessions (e.g., dataset splitting, data loader, model creation, model fitting, etc) to ensure reproducibility of the solution.
-   Use your domain knowledge to understand the data and the algorithms applied to them. Feel free to engineer more features that you feel can be relevant to the solution, even from the external sources.
-   Feel free to write notebooks and tutorials in this competition explaining your approaches or writing utility code if you feel it might be useful for other participants. It will be considered during the course evaluation.
-   Check what other people did with the [target dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/)

You don't have any constraint on the algorithm to be used, but try to explore different solutions. it will be appreciated during the final evaluation :)

### Evaluation

link

keyboard\_arrow\_up

[RMSLE](https://www.datascienceland.com/blog/difference-between-rmse-and-rmsle-656/) metric is used for the evaluation. Taking logs (the **L** in the metric abbreviature) means that errors in predicting expensive houses and cheap houses will affect the result equally.

```Python
def rmsle(y_true, y_pred):
    return np.sqrt(mean_squared_error(np.log1p(y_true), np.log1p(y_pred)))
```

### Submission File

For each ID in the test set, you must predict a probability for the TARGET variable. The file should contain a header and have the following format:

```Python
id,meter_reading
1,0
2,0
3,0
etc.
```

To create a submission file use the following function:

```Python
def generate_submission(predictions, output_file):
    if len(predictions) != len(sample_submission):
        raise ValueError("The length of predictions must match the sample_submission DataFrame.")
    sample_submission['SalePrice'] = predictions
    sample_submission.to_csv(output_file, index=False)
```   


## Dataset Description

### Files

- **train.csv** - Training dataset
- **test.csv** - Test dataset
- **sample_submission.csv** - Sample submission file in the required format

### Columns

A detailed description of all columns/features is provided in the table above.

The dataset contains the following features:

| **Feature Name** | **Description** |
| --- |  --- |
| `Order` | Row identifier. |
| --- |  --- |
| `PID` | Parcel Identification Number. |
| `MS SubClass` | Identifies the type of dwelling involved in the sale. |
| `MS Zoning` | General zoning classification of the sale. |
| `Lot Frontage` | Linear feet of street connected to the property. |
| `Lot Area` | Lot size in square feet. |
| `Street` | Type of road access to the property (e.g., Pave, Grvl). |
| `Alley` | Type of alley access (e.g., Grvl, Pave, NA if no alley). |
| `Lot Shape` | General shape of the property (e.g., Reg, IR1, IR2, IR3). |
| `Land Contour` | Flatness of the property (e.g., Lvl, Bnk, HLS, Low). |
| `Utilities` | Type of utilities available (e.g., AllPub, NoSewr, NoSeWa, ELO). |
| `Lot Config` | Lot configuration (e.g., Inside, Corner, CulDSac, FR2, FR3). |
| `Land Slope` | Slope of the property (e.g., Gtl, Mod, Sev). |
| `Neighborhood` | Physical locations within the city. |
| `Condition 1` | Proximity to main road or railroad. |
| `Condition 2` | Proximity to main road or railroad (if a second is present). |
| `Bldg Type` | Type of dwelling (e.g., 1Fam, 2FmCon, Duplex, TwnhsE, Twnhs). |
| `House Style` | Style of dwelling (e.g., 1Story, 2Story, 1.5Fin, SLvl). |
| `Overall Qual` | Rates the overall material and finish of the house (1-10). |
| `Overall Cond` | Rates the overall condition of the house (1-10). |
| `Year Built` | Original construction date. |
| `Year Remod/Add` | Remodel date (same as `Year Built` if no remodeling). |
| `Roof Style` | Type of roof (e.g., Gable, Hip, Mansard). |
| `Roof Matl` | Roof material (e.g., CompShg, Metal, Membran). |
| `Exterior 1st` | Exterior covering on house (e.g., VinylSd, Wd Sdng, HdBoard). |
| `Exterior 2nd` | Exterior covering on house (if multiple materials). |
| `Mas Vnr Type` | Masonry veneer type (e.g., BrkFace, None, Stone). |
| `Mas Vnr Area` | Masonry veneer area in square feet. |
| `Exter Qual` | Evaluates the quality of the material on the exterior (e.g., Ex, Gd, TA). |
| `Exter Cond` | Evaluates the condition of the material on the exterior (e.g., Ex, Gd, TA). |
| `Foundation` | Type of foundation (e.g., PConc, CBlock, BrkTil). |
| `Bsmt Qual` | Evaluates the height of the basement (e.g., Ex, Gd, TA, NA). |
| `Bsmt Cond` | Evaluates the general condition of the basement (e.g., Ex, Gd, TA, NA). |
| `Bsmt Exposure` | Refers to walkout or garden level basement walls (e.g., Gd, Av, Mn, NA). |
| `BsmtFin Type 1` | Rating of basement finished area (e.g., GLQ, ALQ, Unf). |
| `BsmtFin SF 1` | Type 1 finished square feet. |
| `BsmtFin Type 2` | Rating of basement finished area (if multiple types). |
| `BsmtFin SF 2` | Type 2 finished square feet. |
| `Bsmt Unf SF` | Unfinished basement square feet. |
| `Total Bsmt SF` | Total basement square feet. |
| `Heating` | Type of heating (e.g., GasA, GasW, Wall). |
| `Heating QC` | Heating quality and condition (e.g., Ex, Gd, TA). |
| `Central Air` | Whether the house has central air conditioning (Y/N). |
| `Electrical` | Electrical system (e.g., SBrkr, FuseA, FuseF). |
| `1st Flr SF` | First-floor square feet. |
| `2nd Flr SF` | Second-floor square feet. |
| `Low Qual Fin SF` | Low-quality finished square feet (all floors). |
| `Gr Liv Area` | Above-grade (ground level) living area square feet. |
| `Bsmt Full Bath` | Number of full bathrooms in the basement. |
| `Bsmt Half Bath` | Number of half bathrooms in the basement. |
| `Full Bath` | Number of full bathrooms above grade. |
| `Half Bath` | Number of half bathrooms above grade. |
| `Bedroom AbvGr` | Number of bedrooms above grade. |
| `Kitchen AbvGr` | Number of kitchens above grade. |
| `Kitchen Qual` | Kitchen quality (e.g., Ex, Gd, TA). |
| `TotRms AbvGrd` | Total number of rooms above grade (excluding bathrooms). |
| `Functional` | Home functionality rating (e.g., Typ, Min1, Maj1). |
| `Fireplaces` | Number of fireplaces. |
| `Fireplace Qu` | Fireplace quality (e.g., Ex, Gd, TA, NA). |
| `Garage Type` | Garage location (e.g., Attchd, Detchd, NA). |
| `Garage Yr Blt` | Year garage was built. |
| `Garage Finish` | Interior finish of the garage (e.g., Fin, RFn, Unf). |
| `Garage Cars` | Size of garage in car capacity. |
| `Garage Area` | Size of garage in square feet. |
| `Garage Qual` | Garage quality (e.g., Ex, Gd, TA, NA). |
| `Garage Cond` | Garage condition (e.g., Ex, Gd, TA, NA). |
| `Paved Drive` | Whether the driveway is paved (e.g., Y, P, N). |
| `Wood Deck SF` | Wood deck area in square feet. |
| `Open Porch SF` | Open porch area in square feet. |
| `Enclosed Porch` | Enclosed porch area in square feet. |
| `3Ssn Porch` | Three-season porch area in square feet. |
| `Screen Porch` | Screen porch area in square feet. |
| `Pool Area` | Pool area in square feet. |
| `Pool QC` | Pool quality (e.g., Ex, Gd, TA, NA). |
| `Fence` | Fence quality (e.g., GdPrv, MnPrv, NA). |
| `Misc Feature` | Miscellaneous feature not covered in other categories. |
| `Misc Val` | Value of miscellaneous feature. |
| `Mo Sold` | Month sold (1-12). |
| `Yr Sold` | Year sold. |
| `Sale Type` | Type of sale (e.g., WD, New, COD). |
| `Sale Condition` | Condition of sale (e.g., Normal, Abnorml, Partial). |
| `SalePrice` | Sale price of the property (target variable). |