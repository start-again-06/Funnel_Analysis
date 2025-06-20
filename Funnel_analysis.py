import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

steps = overall_df["Step"]
customers = overall_df["Customers"]
conversion_rates = customers / customers.shift(1)
conversion_rates.iloc[0] = 1.0  # First step is 100%

cumulative_retention = (customers / customers.iloc[0]) * 100
final_conversion = customers.iloc[-1] / customers.iloc[0] * 100

plt.figure(figsize=(10, 6))
sns.lineplot(x=steps, y=cumulative_retention, marker="o", linewidth=2)
plt.title("Cumulative Retention Across Funnel")
plt.ylabel("Cumulative Retention (%)")
plt.xlabel("Funnel Step")
plt.tight_layout()
plt.savefig("/mnt/data/cumulative_retention.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.lineplot(x=steps, y=customers, marker="o", linewidth=2, color="darkgreen")
plt.title("Customer Count at Each Funnel Step")
plt.ylabel("Customers")
plt.xlabel("Funnel Step")
plt.tight_layout()
plt.savefig("/mnt/data/customer_drop_lineplot.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(x=steps, y=conversion_rates*100, palette="coolwarm")
plt.title("Step-by-Step Conversion Rates")
plt.ylabel("Conversion Rate (%)")
plt.xlabel("Funnel Step")
plt.tight_layout()
plt.savefig("/mnt/data/conversion_rate_per_step.png")
plt.close()

plt.figure(figsize=(6, 3))
plt.text(0.5, 0.5, f"Final Conversion Rate:\n{final_conversion:.2f}%", 
         ha='center', va='center', fontsize=18, color='darkblue')
plt.axis('off')
plt.tight_layout()
plt.savefig("/mnt/data/final_conversion_kpi.png")
plt.close()

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.5),
        label=steps.tolist(), color="blue"
    ),
    link=dict(
        source=list(range(len(steps)-1)),
        target=list(range(1, len(steps))),
        value=customers.shift(1).fillna(0).values.tolist()
    )
)])
fig.update_layout(title_text="Funnel Drop-off - Sankey Diagram", font_size=12)
fig.write_html("/mnt/data/funnel_sankey.html")

generated_files = [
    "funnel_chart.png",
    "churn_percentage.png",
    "cumulative_retention.png",
    "customer_drop_lineplot.png",
    "conversion_rate_per_step.png",
    "final_conversion_kpi.png",
    "funnel_sankey.html",
    "funnel_summary.csv"
]

generated_files
