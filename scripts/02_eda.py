import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv(
    "data/nigerian_retail_and_ecommerce_cross_channel_sales_data.csv"
)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df.info()

# Total Online Sales
total_online = df["total_online_spend_ngn"].sum()

print("\nTotal Online Sales (NGN):")
print(total_online)

# Total Offline Sales
total_offline = df["total_offline_spend_ngn"].sum()

print("\nTotal Offline Sales (NGN):")
print(total_offline)

total_sales = total_online + total_offline

print("\nTotal Sales (NGN):")
print(total_sales)

# Percentage of Total Sales
online_percentage = (total_online / total_sales) * 100
offline_percentage = (total_offline / total_sales) * 100

print("\nOnline Sales Percentage:")
print(round(online_percentage, 2), "%")

print("\nOffline Sales Percentage:")
print(round(offline_percentage, 2), "%")

# Sales by City
city_sales = (
    df.groupby("city")[["total_online_spend_ngn", "total_offline_spend_ngn"]]
      .sum().round(2)
)

print("\nSales by City:")
print(city_sales)

# Total Sales by City

city_sales["total_sales"] = (
    city_sales["total_online_spend_ngn"]
    + city_sales["total_offline_spend_ngn"]
)

print(city_sales)

city_sales = city_sales.sort_values(
    by="total_sales",
    ascending=False
)

print(city_sales)

print("\nTop 5 Cities by Sales")

print(city_sales.head())

# City Contribution %
city_sales["sales_percentage"] = (
    city_sales["total_sales"] / total_sales
) * 100

city_sales["sales_percentage"] = city_sales["sales_percentage"].round(2)

print(city_sales.head())

# Online Channel Distribution

online_channel = df["online_channel"].value_counts()

print("\nOnline Channel Distribution:")
print(online_channel)

# Online Channel Percentage

online_channel_percentage = (
    df["online_channel"]
      .value_counts(normalize=True)
      .mul(100)
      .round(2)
)

print("\nOnline Channel Percentage:")
print(online_channel_percentage)

# Offline Store Distribution

offline_store = df["offline_store"].value_counts()

print("\nOffline Store Distribution:")
print(offline_store)

# Offline Store Percentage

offline_store_percentage = (
    df["offline_store"]
      .value_counts(normalize=True)
      .mul(100)
      .round(2)
)

print("\nOffline Store Percentage:")
print(offline_store_percentage)

# payment_counts = df['Payment_Method'].value_counts()
# print(payment_counts)

print(df.columns.tolist())

print(df["total_online_spend_ngn"].describe())

print(df["total_offline_spend_ngn"].describe())

city_sales = (
    df.groupby("city")[
        ["total_online_spend_ngn",
         "total_offline_spend_ngn"]
    ]
    .sum()
)

city_sales["Total Sales"] = (
    city_sales["total_online_spend_ngn"] +
    city_sales["total_offline_spend_ngn"]
)

city_sales = city_sales.sort_values(
    "Total Sales",
    ascending=False
)

print(city_sales)

# Top 10 Cities by Total Sales
top10 = city_sales.head(10)

print(top10)

## Visualize Top 10 Cities by Total Sales
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

top10["Total Sales"].plot(
    kind="bar",
    color="steelblue",
    edgecolor="black"
)

plt.title("Top 10 Cities by Total Sales", fontsize=16)

plt.xlabel("City", fontsize=12)

plt.ylabel("Total Sales (NGN)", fontsize=12)

plt.xticks(rotation=45, ha="right")

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig(
    "images/top10_cities_total_sales.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Test