"""
sales_forecast.py — Predict future sales using Linear Regression
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Paths
DATA_PATH = os.path.join("data", "sales_data.xlsx")
OUTPUT_DIR = os.path.join("output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_excel(DATA_PATH)

# Sort by date
df = df.sort_values("Date")

# Create a numeric index for regression (1, 2, 3, ...)
df["MonthIndex"] = np.arange(1, len(df) + 1)

# Prepare X (feature) and y (target)
X = df[["MonthIndex"]]
y = df["Sales"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict next 6 months
future_months = np.arange(len(df) + 1, len(df) + 7).reshape(-1, 1)
future_sales = model.predict(future_months)

# Prepare future dataframe
future_dates = pd.date_range(start=df["Date"].iloc[-1] + pd.offsets.MonthEnd(1), periods=6, freq="M")
future_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Sales": future_sales
})

# Save to output folder
future_df.to_csv(os.path.join(OUTPUT_DIR, "future_sales_forecast.csv"), index=False)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Sales"], marker="o", label="Actual Sales")
plt.plot(future_df["Date"], future_df["Predicted_Sales"], marker="x", linestyle="--", color="orange", label="Predicted Sales")
plt.title("Sales Forecast (Linear Regression)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sales_forecast.png"))
plt.show()

print("✅ Forecast completed!")
print("Predictions saved in: output/future_sales_forecast.csv")
