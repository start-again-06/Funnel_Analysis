# Funnel_Analysis
# 📈 Funnel Analysis Visualization

This repository contains Python code and outputs for analyzing and visualizing a multi-step funnel using customer activity data. The script includes advanced analytics such as churn analysis, conversion rates, and segment-wise performance.

## 🔧 Features

The script performs the following:

- 📊 **Funnel Chart** – Horizontal bar showing customer count at each funnel step
- 📉 **Churn Percentage Chart** – Drop-off % at each stage
- 🔁 **Cumulative Retention Curve** – % of users remaining compared to step 1
- 📈 **Line Plot of Customer Count** – Trend of customer numbers across steps
- 📦 **Step-by-step Conversion Rates** – Bar chart of conversion between steps
- 🧮 **Final Conversion KPI** – Final retention % from first to last step
- 🧩 **Sankey Diagram** – Visual flow of users through the funnel
- 📁 **Funnel Summary Table** – CSV with drop, retention, and churn metrics

---

## 📁 Output Files

| File Name                      | Description                                 |
|-------------------------------|---------------------------------------------|
| `funnel_chart.png`            | Customer count at each step (bar chart)     |
| `churn_percentage.png`        | Drop-off % per step                         |
| `cumulative_retention.png`    | Cumulative retention curve                  |
| `customer_drop_lineplot.png`  | Line plot of customer counts                |
| `conversion_rate_per_step.png`| Bar chart of conversion rate per step       |
| `final_conversion_kpi.png`    | Final conversion rate (visual)              |
| `funnel_sankey.html`          | Interactive Sankey diagram (HTML)           |
| `funnel_summary.csv`          | Tabular funnel data summary                 |

---
✅ Requirements
Python 3.7+

matplotlib

seaborn

plotly

pandas

numpy

Install dependencies using:

bash
Copy
Edit
pip install matplotlib seaborn plotly pandas numpy
