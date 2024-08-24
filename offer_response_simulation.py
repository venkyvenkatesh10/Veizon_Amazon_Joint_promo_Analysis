import pandas as pd
import numpy as np

# Load the customer profiles from the CSV file
save_path_profiles = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\customer_profiles.csv"
customer_profiles = pd.read_csv(save_path_profiles)

# Define multiple offers
offers = [
    {"description": "First purchase: Buy two phones, one on us", "offer_provider": "Verizon"},
    {"description": "Buy a tablet: 30% off on us", "offer_provider": "Verizon"},
    {"description": "Bundle in TV shows, movies, or series: 10% discount", "offer_provider": "Verizon"},
    {"description": "20% off Amazon Prime subscription", "offer_provider": "Verizon"},
    {"description": "Free upgrade to the next Verizon plan tier for 3 months", "offer_provider": "Verizon"},
    {"description": "Buy one accessory, get another 50% off", "offer_provider": "Verizon"},
    {"description": "Free streaming service for 6 months with any Verizon plan", "offer_provider": "Verizon"},
    {"description": "Get a $50 gift card with any new phone purchase", "offer_provider": "Verizon"},
    {"description": "Bundle home internet with mobile for a 15% discount", "offer_provider": "Verizon"},
    {"description": "Double your data for 3 months at no extra cost", "offer_provider": "Verizon"},
    {"description": "Exclusive early access to new Verizon devices for premium members", "offer_provider": "Verizon"},
    {"description": "Buy a smartwatch and get 25% off your next bill", "offer_provider": "Verizon"},
    {"description": "Get 3 months of Verizon Cloud storage for free", "offer_provider": "Verizon"},
    {"description": "20% off your first month with Verizon's Unlimited Plan", "offer_provider": "Verizon"}
]

# Print out the details of the offers being simulated
print("Offers being simulated:")
for i, offer in enumerate(offers, 1):
    print(f"{i}. {offer['description']} (Provider: {offer['offer_provider']})")

print("\nSimulating customer responses to the offers...")

# Function to simulate offer response
def simulate_offer_response(row):
    """
    This function simulates whether a customer will accept or reject an offer.
    If the customer accepts an offer, it returns the offer description.
    If the customer rejects all offers, it returns "No Offer Accepted".
    """
    for offer in offers:
        offer_description = offer["description"]
        
        if offer_description == "First purchase: Buy two phones, one on us":
            response = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])
        
        elif offer_description == "Buy a tablet: 30% off on us":
            if row['VerizonPlan'] == 'Premium':
                response = np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
            else:
                response = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])

        elif offer_description == "Bundle in TV shows, movies, or series: 10% discount":
            response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])

        elif offer_description == "20% off Amazon Prime subscription":
            if row['AmazonPrimeStatus'] == 'Yes':
                response = 'No'
            else:
                if row['VerizonPlan'] == 'Premium':
                    response = np.random.choice(['Yes', 'No'], p=[0.7, 0.3])
                elif row['VerizonPlan'] == 'Standard':
                    response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])
                else:
                    response = np.random.choice(['Yes', 'No'], p=[0.3, 0.7])
        
        elif offer_description == "Free upgrade to the next Verizon plan tier for 3 months":
            response = np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
        
        elif offer_description == "Buy one accessory, get another 50% off":
            response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])
        
        elif offer_description == "Free streaming service for 6 months with any Verizon plan":
            if row['VerizonPlan'] == 'Premium':
                response = np.random.choice(['Yes', 'No'], p=[0.7, 0.3])
            else:
                response = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])

        elif offer_description == "Get a $50 gift card with any new phone purchase":
            response = np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
        
        elif offer_description == "Bundle home internet with mobile for a 15% discount":
            response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])
        
        elif offer_description == "Double your data for 3 months at no extra cost":
            if row['VerizonPlan'] == 'Premium':
                response = np.random.choice(['Yes', 'No'], p=[0.7, 0.3])
            else:
                response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])

        elif offer_description == "Exclusive early access to new Verizon devices for premium members":
            if row['VerizonPlan'] == 'Premium':
                response = np.random.choice(['Yes', 'No'], p=[0.8, 0.2])
            else:
                response = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])

        elif offer_description == "Buy a smartwatch and get 25% off your next bill":
            response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])

        elif offer_description == "Get 3 months of Verizon Cloud storage for free":
            response = np.random.choice(['Yes', 'No'], p=[0.6, 0.4])

        elif offer_description == "20% off your first month with Verizon's Unlimited Plan":
            response = np.random.choice(['Yes', 'No'], p=[0.5, 0.5])
        
        if response == 'Yes':
            return offer_description
    
    return "No Offer Accepted"

# Apply the function to simulate offer response
customer_profiles['AcceptedOffer'] = customer_profiles.apply(simulate_offer_response, axis=1)

# Define the save path for the offer responses
save_path_response = r"C:\Users\venka\Desktop\Verizon_Amazon_Joint_Campaign\accepted_offers.csv"

# Save the updated DataFrame with accepted offers to CSV
customer_profiles.to_csv(save_path_response, index=False)

print(f"Offer response data saved to {save_path_response}")
