import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Crop Production data.csv")
print(df.shape)

print(df.isnull().sum())
df2 = df.copy()

df2['Production'] = df2['Production'].fillna(df2['Production'].mean())

print(df2.isnull().sum())

print(df2.duplicated().sum())
df2 = df2.drop_duplicates()

df2['State_Name'] = df2['State_Name'].str.strip().str.title()
df2['District_Name'] = df2['District_Name'].str.strip().str.title()
df2['Season'] = df2['Season'].str.strip().str.title()
df2['Crop'] = df2['Crop'].str.strip().str.title()

df2['Area'] = df2['Area'].astype(int)
df2['Crop_Year'] = df2['Crop_Year'].astype(int)
df2['Production'] = df2['Production'].astype(int)
df2['Season'] = df2['Season'].astype('category')

x = (df2 == 0).any()
print(x)

df2 = df2[(df2['Area'] > 0) & (df2['Production'] > 0)]

Q1_area = df2['Area'].quantile(0.25)
Q3_area = df2['Area'].quantile(0.75)
IQR_area = Q3_area - Q1_area

# Calculate the IQR for Area and Production
Q1_area = df2['Area'].quantile(0.25)
Q3_area = df2['Area'].quantile(0.75)
IQR_area = Q3_area - Q1_area

Q1_production = df2['Production'].quantile(0.25)
Q3_production = df2['Production'].quantile(0.75)
IQR_production = Q3_production - Q1_production

# Define outlier boundaries for 'Area' and 'Production'
lower_bound_area = Q1_area - 1.5 * IQR_area
upper_bound_area = Q3_area + 1.5 * IQR_area

lower_bound_production = Q1_production - 1.5 * IQR_production
upper_bound_production = Q3_production + 1.5 * IQR_production

# Remove outliers
df2 = df2[(df2['Area'] >= lower_bound_area) & (df2['Area'] <= upper_bound_area) &
                    (df2['Production'] >= lower_bound_production) & (df2['Production'] <= upper_bound_production)]


df2.to_csv("Crop_Production_Data_Cleaned.csv", index = False)
