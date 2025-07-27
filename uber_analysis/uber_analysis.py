import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("uber.csv")
print("Original Data Preview:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df_clean = df.dropna()


df_clean['pickup_datetime'] = pd.to_datetime(df_clean['pickup_datetime'])
df_clean['hour'] = df_clean['pickup_datetime'].dt.hour
df_clean['day'] = df_clean['pickup_datetime'].dt.day
df_clean['month'] = df_clean['pickup_datetime'].dt.month
df_clean['weekday'] = df_clean['pickup_datetime'].dt.day_name()

df_clean = df_clean[df_clean['fare_amount'] > 0]

df_clean.to_csv("cleaned_uber_data.csv", index=False)



print("\n--- Descriptive Statistics ---")
print(df_clean.describe())

print("\nMedian Fare Amount:", df_clean['fare_amount'].median())
print("Mode Fare Amount:", df_clean['fare_amount'].mode()[0])


plt.figure(figsize=(10, 5))
sns.histplot(df_clean['fare_amount'], bins=50, kde=True)
plt.title("Fare Amount Distribution")
plt.xlabel("Fare ($)")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10, 2))
sns.boxplot(x=df_clean['fare_amount'])
plt.title("Boxplot of Fare Amount")
plt.show()

if 'distance' in df_clean.columns:
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df_clean, x='distance', y='fare_amount')
    plt.title("Fare vs Distance")
    plt.xlabel("Distance")
    plt.ylabel("Fare Amount")
    plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(x='hour', y='fare_amount', data=df_clean)
plt.title("Fare Amount by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Fare Amount")
plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(x='weekday', y='fare_amount', data=df_clean)
plt.title("Fare Amount by Weekday")
plt.xticks(rotation=45)
plt.show()
