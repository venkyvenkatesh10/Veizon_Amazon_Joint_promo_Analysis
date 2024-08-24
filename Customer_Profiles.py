import pandas as pd
import numpy as np
import os
from faker import Faker

# Set random seed for reproducibility
np.random.seed(42)
fake = Faker()

# Define the number of customers
num_customers = 1000

# Generate random customer IDs (6-digit numbers)
customer_ids = np.random.randint(100000, 999999, num_customers)

# Generate random customer names using Faker
customer_names = [fake.name() for _ in range(num_customers)]

# Generate random ages between 18 and 70
ages = np.random.randint(18, 70, num_customers)

# Define a list of 20-30 cities and corresponding states
cities_states = [
    ('New York', 'NY'), ('Los Angeles', 'CA'), ('Chicago', 'IL'), ('Houston', 'TX'), 
    ('Phoenix', 'AZ'), ('San Diego', 'CA'), ('San Francisco', 'CA'), ('Dallas', 'TX'), 
    ('Austin', 'TX'), ('San Antonio', 'TX'), ('Fort Worth', 'TX'), ('Columbus', 'OH'), 
    ('Charlotte', 'NC'), ('Indianapolis', 'IN'), ('Denver', 'CO'), ('Seattle', 'WA'), 
    ('Washington', 'DC'), ('Boston', 'MA'), ('Las Vegas', 'NV'), ('Miami', 'FL'), 
    ('Atlanta', 'GA'), ('Detroit', 'MI'), ('Minneapolis', 'MN'), ('Tampa', 'FL'), 
    ('Orlando', 'FL'), ('Cleveland', 'OH'), ('Cincinnati', 'OH'), ('Kansas City', 'MO'), 
    ('Nashville', 'TN'), ('Portland', 'OR')
]

# Split cities_states into separate lists for cities and states
cities = [cs[0] for cs in cities_states]
states = [cs[1] for cs in cities_states]

# Generate random city, state, and address for each customer
random_cities = np.random.choice(cities, num_customers)
random_states = np.random.choice(states, num_customers)
addresses = [fake.street_address() for _ in range(num_customers)]
zip_codes = [fake.zipcode() for _ in range(num_customers)]

# Generate random Verizon plans (Basic, Standard, Premium)
verizon_plans = np.random.choice(['Basic', 'Standard', 'Premium'], num_customers)

# Generate random Amazon Prime subscription status (Yes, No)
amazon_prime_status = np.random.choice(['Yes', 'No'], num_customers)

# Generate random device make, model, and specifications
device_makes = ['Apple', 'Samsung', 'Google', 'Huawei', 'OnePlus']
device_models = ['iPhone 13', 'Galaxy S21', 'Pixel 6', 'P40 Pro', 'OnePlus 9']
device_specs = ['64GB, 4GB RAM', '128GB, 6GB RAM', '256GB, 8GB RAM', '512GB, 12GB RAM']

device_make = np.random.choice(device_makes, num_customers)
device_model = np.random.choice(device_models, num_customers)
device_spec = np.random.choice(device_specs, num_customers)

# Create the customer profiles DataFrame
customer_profiles = pd.DataFrame({
    'CustomerID': customer_ids,
    'Name': customer_names,
    'Age': ages,
    'Address': addresses,
    'City': random_cities,
    'State': random_states,
    'ZipCode': zip_codes,
    'VerizonPlan': verizon_plans,
    'AmazonPrimeStatus': amazon_prime_status,
    'DeviceMake': device_make,
    'DeviceModel': device_model,
    'DeviceSpecification': device_spec
})

# Define the save path for customer profiles
save_path_profiles = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\customer_profiles.csv"

# Save the customer profiles to CSV
os.makedirs(os.path.dirname(save_path_profiles), exist_ok=True)
customer_profiles.to_csv(save_path_profiles, index=False)

print(f"Customer profiles with detailed location and device information saved to {save_path_profiles}")
