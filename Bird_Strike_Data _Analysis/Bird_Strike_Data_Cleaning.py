import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the shape of data before cleaning
df = pd.read_excel('data/Bird Strikes data.xlsx')
# print(df.shape)
# Result: (25558, 26)

# To check the number of records and the data type of the columns
# print(df.info())

# Checking the number of duplicate records
duplicate_records = df.duplicated().sum()
# print(duplicate_records)
# Result: 0

# Checking the missing values in records
missing_values = df.isnull().sum()
# print(missing_values)

# Handling missing values
# Replace None with other value because pandas as read none precipication as NaN
df['Conditions: Precipitation'] = df['Conditions: Precipitation'].fillna('No precipitation')

# Replace None with other value in Effect: Impact to flight column
df['Effect: Impact to flight'] = df['Effect: Impact to flight'].fillna("No imapct")

# Replacing N/A(Not avaiable) in origin state to unknown
df['Origin State'] = df['Origin State'].fillna("unknown")

# Drpping Remarks column
df.drop('Remarks', axis=1, inplace=True)

# Replace missing values in Aircraft: Number of engines? to unknown due to confidentiality.
df['Aircraft: Number of engines?'] = df['Aircraft: Number of engines?'].fillna("Unknown")

# Dropping the rest of the records with missing values as it is only 129 records
df.dropna(axis=0, how = 'any', inplace= True)

# Checking missing values after handling it
missing_valuess = df.isnull().sum()
# print(missing_valuess)
# Result: 0

# Data type correction
df['Record ID'] = df['Record ID'].astype(int)
df['Altitude bin'] = df['Altitude bin'].astype('category')
df['Wildlife: Number struck'] = df['Wildlife: Number struck'].astype('category')
df['Is Aircraft Large?'] = df['Is Aircraft Large?'].astype(bool)
# To convert to int we must remove commas which is str operation so first convert datatype to str
df['Feet above ground'] = df['Feet above ground'].astype(str)
df['Feet above ground'] = df['Feet above ground'].str.replace(',', '')
df['Feet above ground'] = df['Feet above ground'].astype(float)
# To convert to int we must remove commas which is str operation so first convert datatype to str
df['Cost: Total $'] = df['Cost: Total $'].astype(str)
df['Cost: Total $'] = df['Cost: Total $'].str.replace(',', '')
df['Cost: Total $'] = df['Cost: Total $'].astype(float)

# Records correction
df['Airport: Name'] = df['Airport: Name'].str.title()
df['Aircraft: Airline/Operator'] = df['Aircraft: Airline/Operator'].str.title()

# Creating Columns
# Creating 3 new columns out of FlightDate column
df['FlightDate'] = pd.to_datetime(df['FlightDate'])
df['Year'] = df['FlightDate'].dt.year
df['Month'] = df['FlightDate'].dt.month
df['Day'] = df['FlightDate'].dt.day
# Creating season column for efficient data analysis
season_mapping = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}
df['Season'] = df['Month'].map(season_mapping)
# Creating regions column
# Dictionary to map states to regions
state_region_dict = {
    'Connecticut': 'Northeast',
    'Maine': 'Northeast',
    'Massachusetts': 'Northeast',
    'New Hampshire': 'Northeast',
    'Rhode Island': 'Northeast',
    'Vermont': 'Northeast',
    'New Jersey': 'Northeast',
    'New York': 'Northeast',
    'Pennsylvania': 'Northeast',
    'Florida': 'Southeast',
    'Georgia': 'Southeast',
    'South Carolina': 'Southeast',
    'North Carolina': 'Southeast',
    'Virginia': 'Southeast',
    'West Virginia': 'Southeast',
    'Maryland': 'Southeast',
    'Delaware': 'Southeast',
    'Kentucky': 'Southeast',
    'Tennessee': 'Southeast',
    'Alabama': 'Southeast',
    'Mississippi': 'Southeast',
    'Arkansas': 'Southeast',
    'Louisiana': 'Southeast',
    'District of Columbia': 'Southeast',
    'Illinois': 'Midwest',
    'Indiana': 'Midwest',
    'Michigan': 'Midwest',
    'Ohio': 'Midwest',
    'Wisconsin': 'Midwest',
    'Iowa': 'Midwest',
    'Kansas': 'Midwest',
    'Minnesota': 'Midwest',
    'Missouri': 'Midwest',
    'Nebraska': 'Midwest',
    'North Dakota': 'Midwest',
    'South Dakota': 'Midwest',
    'Texas': 'Southwest',
    'Oklahoma': 'Southwest',
    'New Mexico': 'Southwest',
    'Arizona': 'Southwest',
    'Alaska': 'West',
    'California': 'West',
    'Hawaii': 'West',
    'Oregon': 'West',
    'Washington': 'West',
    'DC' : 'West',
    'Colorado': 'West',
    'Idaho': 'West',
    'Montana': 'West',
    'Nevada': 'West',
    'Utah': 'West',
    'Wyoming': 'West',
    'Virgin Islands': 'Virgin Islands',
    'Puerto Rico': 'Puerto Rico',
    'Prince Edward Island' : 'Canada',
    'Quebec' : 'Canada',
    'Ontario' : 'Canada',
    'British Columbia' : 'Canada',
    'Saskatchewan' : 'Canada',
    'Alberta' : 'Canada',
    'Newfoundland and Labrador' : 'Canada',
    'unknown' : 'Canada'
}
df['Region'] = df['Origin State'].map(state_region_dict)

# Visualizing outliers in 'Feet above ground'
sns.boxplot(x=df['Feet above ground'])
# plt.show()

Q1 = df['Feet above ground'].quantile(0.25)
Q3 = df['Feet above ground'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Feet above ground'] < lower_bound) | (df['Feet above ground'] > upper_bound)]
# print(outliers[['Feet above ground']].count())
# Result 3803 records

# Visualizing outliers in 'Cost: Total $'
sns.boxplot(x=df['Cost: Total $'])
# plt.show()

Q1 = df['Cost: Total $'].quantile(0.25)
Q3 = df['Cost: Total $'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlierss = df[(df['Cost: Total $'] < lower_bound) | (df['Cost: Total $'] > upper_bound)]
# print(outlierss[['Cost: Total $']].count())
# Result: 1214 rows

# Outliers found reasonable so kept intact

# print(df.describe()) # Insights generated


# df.to_excel("Bird_Strike_Data_Cleaned.xlsx", index = False)

