import pandas as pd
df =pd.read_csv(r"C:\Users\malit\OneDrive\Desktop\AI Sales Insights Project\data\sales.csv",encoding="latin1")
df.dropna(inplace=True)

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')


total_sales = df["Sales"].sum()


region_sales = df.groupby("Region")["Sales"].sum()


top_region = region_sales.idxmax()
worst_region = region_sales.idxmin()


top_product = df.groupby("Product Name")["Sales"].sum().idxmax()


if "Order Date" in df.columns:
    df["Month"] = df["Order Date"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["Sales"].sum()
else:
    monthly_sales = None


insights = f"""
📊 SALES INSIGHTS REPORT

Total Sales: {total_sales}

Top Performing Region: {top_region}
Lowest Performing Region: {worst_region}

Best Selling Product: {top_product}

Business Insight:
- Focus more on {top_region} region for expansion.
- Improve strategies in {worst_region}.
- Promote {top_product} to maximize revenue.
"""

region_sales.to_csv("output/region_sales.csv")

if monthly_sales is not None:
    monthly_sales.to_csv("output/monthly_sales.csv")

with open("output/insights.txt", "w", encoding="utf-8") as f:
    f.write(insights)

print(" Analysis complete. Check output folder.")