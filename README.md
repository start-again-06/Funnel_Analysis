# Funnel_Analysis

## Funnel Analysis Visualization
This repository provides a comprehensive Python-based pipeline for performing multi-step funnel analysis using customer activity data. The scripts enable analysts and product managers to understand user behavior at each stage of a conversion funnel, identify drop-off points, and evaluate retention and conversion metrics. The outputs include static and interactive visualizations, along with tabular summaries for detailed insights.

## Features
The pipeline provides advanced analytics and visualizations, including:

- **Funnel Chart:** Horizontal bar chart showing the number of customers at each step of the funnel, helping to identify bottlenecks and drop-off points.  
- **Churn Percentage Chart:** Visual representation of percentage drop-offs between consecutive steps, providing insights into user churn.  
- **Cumulative Retention Curve:** Line chart representing the percentage of users remaining at each step compared to the first step, highlighting overall retention trends.  
- **Line Plot of Customer Count:** Trend visualization of customer numbers across funnel steps, useful for tracking changes over time or across cohorts.  
- **Step-by-Step Conversion Rates:** Bar chart showing conversion rates between each pair of consecutive funnel steps, enabling granular analysis of process efficiency.  
- **Final Conversion KPI:** Visual KPI representing the overall retention or conversion from the first to the last step of the funnel.  
- **Sankey Diagram:** Interactive flow diagram showing how users move between steps, providing a clear and intuitive view of user journeys.  
- **Funnel Summary Table:** CSV file containing detailed metrics for each funnel step, including drop-off counts, retention percentages, and churn rates, suitable for further analysis or reporting.

## System Architecture

The Funnel Analysis system is designed in a modular architecture to handle data ingestion, processing, visualization, and reporting efficiently.

## High-Level Design

### Data Layer
- **Source:** Customer activity logs from e-commerce, SaaS, or subscription platforms.  
- **Storage:** CSV, Excel, or database extracts containing sequential funnel steps.  

### Data Processing Layer
- Cleaning and validating input data  
- Mapping user actions to funnel steps  
- Aggregating metrics such as counts, drop-offs, and retention  
- Generating structured tables for visualization and KPI computation  

### Analytics Layer
- Calculate step-wise conversion rates and churn percentages  
- Compute cumulative retention curves  
- Calculate final funnel KPIs and segment-level statistics  

### Visualization Layer
- Static charts using Matplotlib and Seaborn  
- Interactive plots and Sankey diagrams using Plotly  
- Provides clear, actionable visual outputs for decision-making  

### Output Layer
- Save charts as PNGs  
- Export interactive Sankey diagrams as HTML  
- Save summarized funnel metrics as CSV for reporting or further analysis 

## Output Files

| File Name                     | Description                                         |
|-------------------------------|-----------------------------------------------------|
| `funnel_chart.png`             | Horizontal bar chart of customer count per step    |
| `churn_percentage.png`         | Drop-off percentage per funnel stage               |
| `cumulative_retention.png`     | Cumulative retention curve showing % users retained|
| `customer_drop_lineplot.png`   | Line plot tracking customer count trends           |
| `conversion_rate_per_step.png` | Step-by-step conversion rate bar chart             |
| `final_conversion_kpi.png`     | Visual representation of final conversion KPI     |
| `funnel_sankey.html`           | Interactive Sankey diagram of user flows          |
| `funnel_summary.csv`           | Tabular summary of funnel metrics                  |

## Requirements
- **Python Version:** 3.7+  
- **Libraries:**  
  - `matplotlib`  
  - `seaborn`  
  - `plotly`  
  - `pandas`  
  - `numpy` 

## Usage

- Prepare your dataset with sequential steps representing the funnel  
- Run the analysis script to generate charts and CSV outputs  
- Examine funnel charts and churn analysis to identify bottlenecks  
- Leverage the Sankey diagram and retention curves for flow and trend insights  
- Use segment-wise metrics for targeted improvement strategies  

## Applications

- Customer journey analysis for e-commerce, SaaS, or subscription services  
- Churn identification and retention strategy planning  
- Conversion rate optimization across marketing and product funnels  
- Executive dashboards for tracking KPIs and funnel performance  

This repository provides a complete and flexible toolkit for funnel analytics, enabling teams to convert raw customer activity data into actionable insights and visual storytelling.
