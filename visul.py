import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct the file path to match your local environment
data_path = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\combined_data.csv"
data = pd.read_csv(data_path)

# Set up the save path for the individual visualizations
save_dir = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign"

# 1. Customer Segmentation Analysis - Clustered bar chart for offer acceptance
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='AcceptedOffer', color='lightblue')
plt.title('Customer Segmentation Based on Accepted Offers')
plt.xlabel('Accepted Offer')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{save_dir}\\customer_segmentation.png")
plt.close()

# 2. Usage Patterns - Line chart for peak streaming hours (using AmazonPrimeVideoHours instead of VerizonStreamingHours)
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='PeakStreamingHour', y='AmazonPrimeVideoHours', hue='PeakStreamingDay')
plt.title('Peak Streaming Hours vs. Amazon Prime Video Hours')
plt.xlabel('Peak Streaming Hour')
plt.ylabel('Amazon Prime Video Hours')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{save_dir}\\peak_streaming_hours.png")
plt.close()

# 3. Correlation Between Offer Acceptance and Data Usage - Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='VerizonDataUsageGB', y='AmazonPrimeVideoHours', hue='AcceptedOffer')
plt.title('Correlation Between Verizon Data Usage and Amazon Prime Video Hours')
plt.xlabel('Verizon Data Usage (GB)')
plt.ylabel('Amazon Prime Video Hours')
plt.tight_layout()
plt.savefig(f"{save_dir}\\correlation_data_usage.png")
plt.close()

# 4. Purchase Behavior Analysis - Stacked bar chart for regular vs offer-based purchases
plt.figure(figsize=(10, 6))
purchase_data = data[['AmazonRegularPurchases', 'AmazonOfferPurchases']].copy()
purchase_data['TotalPurchases'] = purchase_data['AmazonRegularPurchases'] + purchase_data['AmazonOfferPurchases']
purchase_data = purchase_data.melt(value_vars=['AmazonRegularPurchases', 'AmazonOfferPurchases'], var_name='PurchaseType', value_name='Number of Purchases')

sns.barplot(data=purchase_data, x='PurchaseType', y='Number of Purchases', color='lightblue')
plt.title('Regular vs Offer-Based Amazon Purchases')
plt.xlabel('Purchase Type')
plt.ylabel('Number of Purchases')
plt.tight_layout()
plt.savefig(f"{save_dir}\\purchase_behavior.png")
plt.close()

# 5. Churn Prediction - Box plot for data usage and streaming habits based on offer acceptance
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='AcceptedOffer', y='VerizonDataUsageGB', color='lightgreen')
plt.title('Verizon Data Usage by Accepted Offer')
plt.xlabel('Accepted Offer')
plt.ylabel('Verizon Data Usage (GB)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{save_dir}\\churn_prediction.png")
plt.close()

# 6. Revenue Impact Estimation - Combined bar and line chart for regular vs offer-based purchases over time
plt.figure(figsize=(10, 6))
data['Month'] = pd.to_datetime(data['CustomerID'], format='%Y%m%d', errors='coerce').dt.month
revenue_data = data.groupby('Month')[['AmazonRegularPurchases', 'AmazonOfferPurchases']].sum().reset_index()
revenue_data['TotalPurchases'] = revenue_data['AmazonRegularPurchases'] + revenue_data['AmazonOfferPurchases']

ax1 = sns.barplot(data=revenue_data, x='Month', y='TotalPurchases', color='purple')
ax2 = ax1.twinx()
sns.lineplot(data=revenue_data, x='Month', y='AmazonOfferPurchases', color='red', marker='o', ax=ax2)

plt.title('Revenue Impact from Regular vs Offer-Based Purchases')
ax1.set_xlabel('Month')
ax1.set_ylabel('Total Purchases')
ax2.set_ylabel('Offer-Based Purchases')
plt.tight_layout()
plt.savefig(f"{save_dir}\\revenue_impact.png")
plt.close()

# 7. Geographical Analysis - Heatmap based on City and Verizon Data Usage
plt.figure(figsize=(10, 6))
city_usage = data.groupby('City')['VerizonDataUsageGB'].sum().reset_index()
city_usage_pivot = city_usage.pivot_table(index='City', values='VerizonDataUsageGB', aggfunc='sum')

sns.heatmap(city_usage_pivot, cmap='coolwarm')
plt.title('Heatmap of Verizon Data Usage by City')
plt.xlabel('Verizon Data Usage (GB)')
plt.ylabel('City')
plt.tight_layout()
plt.savefig(f"{save_dir}\\geographical_analysis.png")
plt.close()

# 8. Customer Lifetime Value (CLV) Estimation - Pareto chart for top customers contributing to revenue
plt.figure(figsize=(10, 6))
data['Revenue'] = data['AmazonRegularPurchases'] * 10 + data['AmazonOfferPurchases'] * 20  # Example revenue calculation

clv_data = data.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).reset_index()
clv_data['CumulativeRevenue'] = clv_data['Revenue'].cumsum()
clv_data['CumulativePercentage'] = 100 * clv_data['CumulativeRevenue'] / clv_data['Revenue'].sum()

sns.lineplot(data=clv_data, x='CustomerID', y='CumulativePercentage')
plt.title('Customer Lifetime Value (CLV) Estimation')
plt.xlabel('Customer ID')
plt.ylabel('Cumulative Percentage of Revenue')
plt.tight_layout()
plt.savefig(f"{save_dir}\\clv_estimation.png")
plt.close()

print(f"All individual visualizations saved to {save_dir}")
