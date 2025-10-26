import pandas as pd
import os

# Create folders if they don't exist
os.makedirs("data", exist_ok=True)

# Sample data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "Sales": [200, 220, 250, 270, 300, 280, 320, 330, 310, 340],
    "Customers": [20, 22, 25, 24, 30, 28, 32, 31, 30, 33],
    "Region": ["North", "East", "West", "South", "North", "East", "West", "South", "North", "East"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as Excel
output_path = os.path.join("data", "sales_data.xlsx")
df.to_excel(output_path, index=False)

print(f"✅ Sample Excel file created at: {output_path}")
