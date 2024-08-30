import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats



# Step 1. 1. Detecting Outliers
# Sample Data
data = {'Value': [10, 12, 12, 13,15, 120, 15, 12, 11, 12,120, 14, 15, 100]} # 100 is an outlier
df = pd.DataFrame(data)

# Box Plot
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Value'])
plt.title('Box Plot to Detect Outliers')
plt.show()

# Z-Score
df['Z-Score'] = np.abs(stats.zscore(df['Value']))
print(df)

# Identifying Outliers using Z-Score
threshold = 3
outliers = df[df['Z-Score'] > threshold]
print("\nOutliers using Z-Score:\n", outliers)

# Interquartile Range (IQR)
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_iqr = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
print("\nOutliers using IQR:\n", outliers_iqr)

# Step 2:  Handling Outliers
# 1. Removing Outliers
df_cleaned = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
print("\nData after Removing Outliers:\n", df_cleaned)

# 2. Capping Outliers
df_capped = df.copy()
df_capped.loc[df_capped['Value'] > upper_bound, 'Value'] = upper_bound
df_capped.loc[df_capped['Value'] < lower_bound, 'Value'] = lower_bound
print("\nData after Capping Outliers:\n", df_capped)

# 3. Imputing Outliers with Median
df_imputed = df.copy()
median_value = df['Value'].median()
df_imputed.loc[(df_imputed['Value'] < lower_bound) | (df_imputed['Value'] > upper_bound), 'Value'] = median_value
print("\nData after Imputing Outliers:\n", df_imputed)


# STep 3: Visualize outliers 
# Visualizing the Data
plt.figure(figsize=(15, 5))

# Original Data
plt.subplot(1, 4, 1)
sns.boxplot(x=df['Value'])
plt.title('Original Data')

# After Removing Outliers
plt.subplot(1, 4, 2)
sns.boxplot(x=df_cleaned['Value'])
plt.title('After Removing Outliers')

# After Capping Outliers
plt.subplot(1, 4, 3)
sns.boxplot(x=df_capped['Value'])
plt.title('After Capping Outliers')

# After Imputing Outliers
plt.subplot(1, 4, 4)
sns.boxplot(x=df_imputed['Value'])
plt.title('After Imputing Outliers')

plt.tight_layout()
plt.show()

# Visualizing the Data with Histograms
plt.figure(figsize=(15, 5))

# Original Data
plt.subplot(1, 4, 1)
plt.hist(df['Value'], bins=10, color='gray', edgecolor='black')
plt.title('Original Data')

# After Removing Outliers
plt.subplot(1, 4, 2)
plt.hist(df_cleaned['Value'], bins=10, color='blue', edgecolor='black')
plt.title('After Removing Outliers')

# After Capping Outliers
plt.subplot(1, 4, 3)
plt.hist(df_capped['Value'], bins=10, color='green', edgecolor='black')
plt.title('After Capping Outliers')

# After Imputing Outliers
plt.subplot(1, 4, 4)
plt.hist(df_imputed['Value'], bins=10, color='orange', edgecolor='black')
plt.title('After Imputing Outliers')

plt.tight_layout()
plt.show()

