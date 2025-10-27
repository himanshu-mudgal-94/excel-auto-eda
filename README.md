# 📊 Excel Auto EDA & Sales Forecasting App

A simple end-to-end ML project that performs automatic **Exploratory Data Analysis (EDA)** on any uploaded Excel file and optionally predicts **future sales trends** using Linear Regression.

---

## 🚀 Features
- Upload any Excel file (`.xlsx`)
- Automatically clean, summarize, and visualize data
- Generate histograms, correlation heatmaps, and descriptive stats
- Forecast future sales with ML (Linear Regression)
- Download results as CSV and visualizations as PNGs

---

## 🧠 Tech Stack
- **Python 3.10+**
- **Pandas, Matplotlib, Seaborn, Scikit-learn**
- **Streamlit** for the web app interface

---

## 🏗️ Run Locally
```bash
# 1. Create and activate virtual environment
python3 -m venv source
source source/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

excel-auto-eda/
│
├── data/                 # Excel input files
├── output/               # Generated plots & CSVs
├── app.py                # Streamlit web interface
├── main.py               # Core EDA script
├── sales_forecast.py     # Linear regression forecast
├── requirements.txt
└── README.md

