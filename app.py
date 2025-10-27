import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

# App title and description
st.set_page_config(page_title="📊 Excel Auto EDA & Sales Forecast", layout="wide")
st.title("📈 Excel Auto-EDA & Sales Forecast App")
st.markdown("""
Upload any Excel file to explore the data automatically.  
If your file has `Date` and `Sales` columns, the app will also **forecast future sales** using Linear Regression.
---
""")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success(f"✅ File uploaded: {uploaded_file.name}")
    st.write("### 👀 Preview of your data")
    st.dataframe(df.head())

    # Basic summary
    st.markdown("### 📊 Basic Summary")
    st.write(df.describe())

    # Visualizations
    st.markdown("### 📈 Distribution of Numeric Columns")
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    # Correlation heatmap
    if len(numeric_cols) > 1:
        st.markdown("### 🔥 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(6,4))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Forecast section
    if "Date" in df.columns and "Sales" in df.columns:
        st.markdown("---")
        st.markdown("### 🤖 Sales Forecast (Linear Regression)")
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")
        df["Days"] = (df["Date"] - df["Date"].min()).dt.days

        X = df[["Days"]]
        y = df["Sales"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        st.write(f"Model RMSE: **{mean_squared_error(y_test, preds, squared=False):.2f}**")

        # Predict 30 days ahead
        future_days = pd.DataFrame({"Days": range(df["Days"].max()+1, df["Days"].max()+31)})
        future_sales = model.predict(future_days)

        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Sales"], label="Actual Sales", marker="o")
        ax.plot(pd.date_range(df["Date"].max(), periods=30, freq="D"), future_sales, 
                label="Forecast (Next 30 Days)", linestyle="--")
        ax.legend()
        ax.set_title("Sales Forecast")
        st.pyplot(fig)
else:
    st.info("👆 Upload an Excel file to get started.")
