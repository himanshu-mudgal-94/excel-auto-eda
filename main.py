#!/usr/bin/env python3
"""
main.py - simple Auto-EDA for the sample Excel
Usage:
  python main.py --data data/sales_data.xlsx
"""
import os
import sys
import argparse
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path):
    if not os.path.exists(path):
        print(f"[ERROR] file not found: {path}")
        sys.exit(1)
    if path.lower().endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)
    return df


def basic_eda(df):
    print("\n=== BASIC EDA ===")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nHead:")
    print(df.head().to_string())

    print("\nDtypes:\n", df.dtypes)
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]
    if not nulls.empty:
        print("\nNull counts (non-zero):\n", nulls)

    # numeric summary -> CSV
    num_desc = df.describe(include=[np.number]).T
    num_desc["null_count"] = df.isnull().sum()
    out_csv = os.path.join(OUTPUT_DIR, "summary_numeric.csv")
    num_desc.to_csv(out_csv)
    print("Saved numeric summary to", out_csv)


def plots(df):
    print("\n=== PLOTTING ===")
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # histograms
    for c in num_cols:
        plt.figure(figsize=(6, 3))
        df[c].dropna().hist(bins=20)
        plt.title(f"Histogram: {c}")
        plt.xlabel(c)
        plt.ylabel("count")
        fname = os.path.join(OUTPUT_DIR, f"hist_{c}.png")
        plt.tight_layout()
        plt.savefig(fname)
        plt.close()
        print("Saved", fname)

    # correlation heatmap
    if len(num_cols) >= 2:
        corr = df[num_cols].corr()
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation heatmap")
        fname = os.path.join(OUTPUT_DIR, "correlation_heatmap.png")
        plt.tight_layout()
        plt.savefig(fname)
        plt.close()
        print("Saved", fname)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", "-d", required=True, help="Path to CSV/XLSX")
    args = parser.parse_args()

    df = load_data(args.data)
    basic_eda(df)
    plots(df)

    print("\nAll done. Check the 'output/' folder for CSVs and PNGs.")


if __name__ == "__main__":
    main()
