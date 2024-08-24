import pandas as pd

# Load the accepted offers and usage data from CSV files
accepted_offers_path = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\accepted_offers.csv"
usage_data_path = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\usage_data.csv"

accepted_offers = pd.read_csv(accepted_offers_path)
usage_data = pd.read_csv(usage_data_path)

# Perform an inner join on CustomerID (SubscriberID)
combined_data = pd.merge(accepted_offers, usage_data, left_on='CustomerID', right_on='SubscriberID', how='inner')

# Drop the duplicate 'SubscriberID' column from the right DataFrame
combined_data = combined_data.drop(columns=['SubscriberID'])

# Define the save path for the combined data
combined_data_path = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\combined_data.csv"

# Save the combined data to CSV
combined_data.to_csv(combined_data_path, index=False)

print(f"Combined data saved to {combined_data_path}")
