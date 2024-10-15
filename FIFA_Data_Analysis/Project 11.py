import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv("WorldCupMatches.csv")
# Excel had 4350 rows with only data in 852 so dropped all the data after 852 rows
df = df.drop(df.index[852:])

# Dropping duplicates
df = df.drop_duplicates()

# Checking shape of the df
print(df.shape)

# To check if there is any null values
print(df.isnull().sum())
# found one missing value in attendance

# To find the index of the value that is missing in attendance
empty_indices = df[df['Attendance'].isnull()].index
print(empty_indices)

# Calculate the mean of the 'Attendance' column, ignoring NaN values, and round it to an integer
mean_attendance = int(round(df['Attendance'].mean()))
df['Attendance'].fillna(mean_attendance, inplace=True)

# Sliced Datetime till date
df['Datetime'] = df['Datetime'].str[:11]

# Rename the column Datetime to Date
df.rename(columns={'Datetime': 'Date'}, inplace=True)

# To sum all goals
df['Goals'] = df['Home Team Goals'] + df['Away Team Goals']

# To replace spaces with underscores in column names
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('-', '_')

# To sum half time goals
df['Half_Time_Goals'] = df['Half_time_Home_Goals'] + df['Half_time_Away_Goals']

# To rename column names
df['Country'] = df['Home_Team_Name']
df['Win_Conditions'] = df['Win_conditions']
df['Half_Time_Home_Goals'] = df['Half_time_Home_Goals']
df['Half_Time_Away_Goals'] = df['Half_time_Away_Goals']

# Creating column Outcome_Of_The_Match with conditional function
def outcome(df):
    if df['Home_Team_Goals'] > df['Away_Team_Goals']:
        return 'Home_Team_Win'
    elif df['Home_Team_Goals'] < df['Away_Team_Goals']:
        return 'Away_Team_Win'
    else:
        return 'DRAW'

# df.apply is used to apply functions along an axis on df that is on rows or columns axis = 1 for rows.
df['Outcome_Of_The_Match'] = df.apply(outcome, axis=1)

# To reorder columns
new_order = ['Year','Date', 'RoundID', 'Stage', 'MatchID', 'Country', 'City', 'Stadium', 'Home_Team_Name', 'Home_Team_Initials', 'Half_Time_Home_Goals', 'Home_Team_Goals','Away_Team_Name', 'Away_Team_Initials', 'Half_Time_Away_Goals', 'Away_Team_Goals', 'Half_Time_Goals', 'Goals','Outcome_Of_The_Match', 'Win_Conditions', 'Attendance', 'Referee', 'Assistant_1', 'Assistant_2']
df = df.reindex(columns=new_order)

# df.to_csv('WC_MATCHES_BY_PY.csv')





