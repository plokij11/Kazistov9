import pandas as pd
import numpy as np
from datetime import datetime

print('2.')
data = {
    'Прізвище': ['Шевченко', 'Франко', 'Лесенко', 'Котляревська', 'Забужко'],
    'Ім\'я': ['Тарас', 'Іван', 'Леся', 'Олена', 'Оксана'],
    'Дата народження': ['1985-02-13', '1988-07-07', '1993-06-25', '1980-11-01', '1995-01-14'],
    'Маса тіла (кг)': [80, 90, 70, None, 60],
    'Медичне страхування': [False, True, True, False, True]
}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print('\n')

# Припускаємо, що у нас є інший файл CSV з іншими даними
print('3.')
df = pd.read_csv("health_data.csv")
print(df)
print('\n')

print('4.')
print(df.head(10))
print('\n')

print('5.')
print(df.shape)
print('\n')

print('6.')
print(df.info())
print('\n')

print('7.')
print(df.describe())
print('\n')

print('8.')
print(df.nunique())
print('\n')

print('9.')
min_unique_column = df.nunique().idxmin()
value_counts = df[min_unique_column].value_counts()
print(value_counts)
print('\n')

print('10.')
print("\n\t1. Some columns may have incorrect data types, especially dates that could be converted to datetime type if stored as strings.\n\t2. It's essential to examine rows with missing data and decide how to fill or remove them.\n\t3. If the dataset contains numerical data with different scales, it might be beneficial to standardize them.\n\t")
print('\n')

print('11.')
print(df['timestamp'].head(5))
df = df.dropna(subset=['timestamp'])
df = df[~df['timestamp'].isin([np.nan, np.inf, -np.inf])]

# Convert the 'timestamp' column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'])
print('_________________')
print(df['timestamp'].head(5))
print('\n')

print('12.')
# Creating a copy of DataFrame
df_copy = df.copy()

print('Before deletion:', df_copy.shape)

# Calculate the percentage of non-null values for each column
non_null_percentages = df_copy.count() / len(df_copy)

# Select columns where the percentage of non-null values is less than 30%
columns_to_drop = non_null_percentages[non_null_percentages < 0.3].index

# Delete the corresponding columns
df_copy = df_copy.drop(columns=columns_to_drop)

print('After deletion:', df_copy.shape)
print('\n')

print('14.')
rows_with_missing_values = df[df.isnull().any(axis=1)]
print(rows_with_missing_values)
print('\n')

print('15.')
# Select rows corresponding to models of missiles from a list
selected_models = ['X-31', 'Kalibr', 'Iskander-M', 'X-59', 'X-101/X-555', 'X-101', 'X-555', 'X-31P', 'X-22', 'X-47', 'X-59 and X-35', 'X-47 Kinzhal', 'Iskander-M/KN-23/X-47', 'KN-23']
selected_rows = df[df['model'].isin(selected_models)]

# Calculate the total number of launched and destroyed missiles
total_launched = selected_rows['launched'].sum()
total_destroyed = selected_rows['destroyed'].sum()

# Calculate the destruction percentage
if total_launched != 0:
    average_percentage_destroyed = (total_destroyed / total_launched) * 100
else:
    average_percentage_destroyed = 0

print("Average missile destruction percentage over the entire period: {:.2f}%".format(average_percentage_destroyed))
print('\n')

print('16.')
# Group data by model and count the total number of launched devices
model_counts = df.groupby('model')['launched'].sum().reset_index()

# Sort data in descending order by the number of launched devices
top_10_models = model_counts.sort_values(by='launched', ascending=False).head(10)

# Convert data to JSON format and save to a file
top_10_models.to_json('top_10_models.json', orient='records')

# Display the top 10 most popular launched device models
print(top_10_models)
print('\n')


print('17.')
data = {
    'timestamp': ['2022-01-01 12:00', '2022-01-02 12:00', '2022-01-03 12:00', '2022-01-04 12:00', '2022-01-05 12:00'],
    'model': ['X-31', 'Kalibr', 'Iskander-M', 'X-59', 'X-101'],
    'launched': [5, 10, 2, 8, 4],
    'destroyed': [1, 3, 1, 2, 0],
}

df = pd.DataFrame(data)

# Rename 'timestamp' to 'time_start' to match the analysis code
df.rename(columns={'timestamp': 'time_start'}, inplace=True)

# Create a new column that will contain the difference between the number of launched and destroyed devices
df['hits'] = df['launched'] - df['destroyed']

# Group data by the start date of attacks and count the total number of hits (difference between launched and destroyed) for each day
hits_by_day = df.groupby('time_start')['hits'].sum()

# Find the day with the most hits
max_hits_day = hits_by_day.idxmax()

# Get the number of hits on that day
max_hits_count = hits_by_day[max_hits_day]

# Display the start time of the attack and the number of hits (difference between launched and destroyed) for the day with the most hits
print("The most hits occurred on the day:", max_hits_day)
print("Number of hits (difference between launched and destroyed):", max_hits_count)
print('\n')


