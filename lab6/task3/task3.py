import pandas as pd
data=pd.read_csv("train.csv")
missing_values=data.isnull().sum()
print(missing_values.to_string())
# Drop columns with excessive missing values
data.drop(["Alley", "PoolQC", "Fence", "MiscFeature"], axis=1, inplace=True)
# Fill missing numerical values with median
num_cols = ["LotFrontage", "MasVnrArea", "GarageYrBlt"]
data.fillna({col: data[col].median() for col in num_cols}, inplace=True)
# Fill missing categorical values with mode
cat_cols = ["MasVnrType", "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2",
            "GarageType", "GarageFinish", "GarageQual", "GarageCond", "Electrical"]
data.fillna({col: data[col].mode()[0] for col in cat_cols}, inplace=True)
data.fillna({"FireplaceQu": "None"}, inplace=True)
# Verify missing values after cleaning
print("Missing values after cleaning:\n", data.isnull().sum().sum())
num_cols = ["LotFrontage", "LotArea", "GarageYrBlt"]  # List numeric columns stored as text
data[num_cols] = data[num_cols].apply(pd.to_numeric, errors="coerce")
print(data.dtypes.to_string())



