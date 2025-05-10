import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(url, names=column_names)

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Explore the structure
print("\nDataset information:")
print(iris_df.info())

# Check for missing values
print("\nMissing values:")
print(iris_df.isnull().sum())

# Clean the dataset (though iris dataset is already clean)
# For demonstration, if there were missing values we might do:
# iris_df = iris_df.dropna()  # or fillna() with appropriate values


# Basic statistics
print("\nBasic statistics:")
print(iris_df.describe())

# Group by species and compute means
print("\nMean measurements by species:")
print(iris_df.groupby('species').mean())

# Additional interesting findings
print("\nComparing petal length to width ratio by species:")
iris_df['petal_ratio'] = iris_df['petal_length'] / iris_df['petal_width']
print(iris_df.groupby('species')['petal_ratio'].mean().sort_values(ascending=False))



# Set style for better looking plots
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# 1. Line chart (though time series doesn't make sense for iris, we'll use index as x-axis)
plt.subplot(2, 2, 1)
plt.plot(iris_df.index[:50], iris_df['sepal_length'][:50], label='Setosa')
plt.plot(iris_df.index[50:100], iris_df['sepal_length'][50:100], label='Versicolor')
plt.plot(iris_df.index[100:], iris_df['sepal_length'][100:], label='Virginica')
plt.title('Sepal Length by Iris Species (Ordered by Index)')
plt.xlabel('Observation Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()

# 2. Bar chart - average petal length by species
plt.subplot(2, 2, 2)
iris_df.groupby('species')['petal_length'].mean().plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# 3. Histogram - distribution of sepal width
plt.subplot(2, 2, 3)
sns.histplot(data=iris_df, x='sepal_width', bins=15, kde=True, hue='species', multiple='stack')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')

# 4. Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(data=iris_df, x='sepal_length', y='petal_length', hue='species', style='species', s=100)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()