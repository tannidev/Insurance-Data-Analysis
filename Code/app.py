import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/insurance.csv")

# Title
st.title("Healthcare Insurance Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())


# Dataset Overview
st.header("1. Dataset Structure")

st.write("Shape of dataset (rows, columns):", df.shape)
st.write("Column Data Types:")
st.write(df.dtypes)

# Data Quality
st.header("2. Data Quality Check")

st.write("Missing Values:")
st.write(df.isnull().sum())

st.write("Duplicate Rows:", df.duplicated().sum())

# Handle Duplicates
if st.checkbox("Remove Duplicates"):
    df = df.drop_duplicates()
    st.success("Duplicates removed!")
    st.write("Updated shape:", df.shape)




# Basic Exploratory Analysis
st.header("3. Basic Exploratory Analysis (Numeric Distributions)")

numeric_cols = ['age', 'bmi', 'charges']

for col in numeric_cols:
    st.subheader(f"Distribution of {col.capitalize()}")
    fig, ax = plt.subplots()
    sns.histplot(df[col], bins=30, kde=True, ax=ax)
    st.pyplot(fig)






# Categorical Variables
st.header("4. Exploring Categorical Variables")

categorical_cols = ['sex', 'smoker', 'region', 'children']

for col in categorical_cols:
    st.subheader(f"Distribution of {col.capitalize()}")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=col, ax=ax)
    st.pyplot(fig)


# Bivariate Analysis
st.header("5. Bivariate Analysis (Features vs Charges)")

# Charges by smoker
st.subheader("Charges by Smoker Status")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="smoker", y="charges", ax=ax)
st.pyplot(fig)

# Charges by sex
st.subheader("Charges by Sex")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="sex", y="charges", ax=ax)
st.pyplot(fig)

# Charges by region
st.subheader("Charges by Region")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="region", y="charges", ax=ax)
st.pyplot(fig)

# Charges by number of children
st.subheader("Charges by Number of Children")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="children", y="charges", ax=ax)
st.pyplot(fig)





# Correlation Analysis
st.header("6. Correlation Analysis")

# Heatmap
st.subheader("Correlation Heatmap (Numeric Features)")
corr = df[['age', 'bmi', 'children', 'charges']].corr()

fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Scatter: Age vs Charges
st.subheader("Age vs Charges (Smoker Highlighted)")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="age", y="charges", hue="smoker", ax=ax)
st.pyplot(fig)

# Scatter: BMI vs Charges
st.subheader("BMI vs Charges (Smoker Highlighted)")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="bmi", y="charges", hue="smoker", ax=ax)
st.pyplot(fig)
