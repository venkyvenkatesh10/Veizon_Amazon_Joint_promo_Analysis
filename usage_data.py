import pandas as pd
import numpy as np
import random
import os  # Importing os module

# Load the accepted offers from the CSV file to get Subscriber IDs
save_path_accepted_offers = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\accepted_offers.csv"
accepted_offers = pd.read_csv(save_path_accepted_offers)

# Extract the Subscriber IDs
subscriber_ids = accepted_offers['CustomerID']

# Simulate Verizon data usage (in GB)
verizon_data_usage = np.random.uniform(0.5, 50.0, len(subscriber_ids)).round(2)

# Simulate Verizon streaming habits (hours)
verizon_streaming_hours = np.random.uniform(0, 100, len(subscriber_ids)).round(2)

# Simulate regular Amazon purchases (number of purchases)
amazon_regular_purchases = np.random.randint(0, 20, len(subscriber_ids))

# Simulate purchases made through offers (number of purchases)
amazon_offer_purchases = np.random.randint(0, 10, len(subscriber_ids))

# Simulate peak streaming hours (in the format HH:MM)
peak_streaming_hours = [f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}" for _ in range(len(subscriber_ids))]

# Simulate peak streaming days (random day of the week)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
peak_streaming_days = [random.choice(days_of_week) for _ in range(len(subscriber_ids))]

# Simulate Amazon Prime Video streaming (hours)
amazon_prime_video_hours = np.random.uniform(0, 50, len(subscriber_ids)).round(2)

# Create a DataFrame for usage data
usage_data = pd.DataFrame({
    'SubscriberID': subscriber_ids,
    'VerizonDataUsageGB': verizon_data_usage,
    'AmazonRegularPurchases': amazon_regular_purchases,
    'AmazonOfferPurchases': amazon_offer_purchases,
    'PeakStreamingHour': peak_streaming_hours,
    'PeakStreamingDay': peak_streaming_days,
    'AmazonPrimeVideoHours': amazon_prime_video_hours
})

# Define the save path for the usage data
save_path_usage = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\usage_data.csv"

# Save the usage data to CSV
os.makedirs(os.path.dirname(save_path_usage), exist_ok=True)
usage_data.to_csv(save_path_usage, index=False)

print(f"Usage data with detailed purchase and streaming information saved to {save_path_usage}")
