import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\sagar\OneDrive\Desktop\Chethan\Unified Mentor\Project 5\Data.xlsx")

df2 = df.drop(['Sector'], axis = 1)
data_sum = df2.copy()
data_sum['Sum_in_million_USD'] = df2.sum(axis = 1)

df_year = df.iloc[:,1:]
width_y = df_year.shape[1]

def cal_avg(n):
    avg = np.round(df_year.iloc[:,width_y-n:width_y].mean(axis=1),2)
    return(avg)

df_year["avg_last_17yrs"] = cal_avg(17)
df_year["avg_last_15yrs"] = cal_avg(15)
df_year["avg_last_12yrs"] = cal_avg(12)
df_year["avg_last_10yrs"] = cal_avg(10)
df_year["avg_last_8yrs"] = cal_avg(8)
df_year["avg_last_5yrs"] = cal_avg(5)
df_year["avg_last_3yrs"] = cal_avg(3)
df_year["avg_last_2yrs"] = cal_avg(2)

df_year.insert(0,'Sector', df['Sector'])
df_year['Sum_in_million_USD'] = data_sum['Sum_in_million_USD']


df_year.to_excel('FDI_DT.xlsx')

df = pd.read_excel(r"C:\Users\sagar\OneDrive\Desktop\Chethan\Unified Mentor\Project 5\FDI_DT_By_Excel.xlsx")

newdf = df.copy()
z = newdf.drop([df.index[17], df.index[18]])

df_melted = pd.melt(z, id_vars=['Sector'], var_name='sector', value_name='FDI Amount')
print(df_melted.to_string())

df_melted.to_excel("Year_Sector_FDIamt.xlsx")

