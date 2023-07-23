import requests

# Prompt the user to enter the IP address
ip_address = input("Enter the IP address: ")

# Construct the API URL with the user-provided IP address
api_url = f"https://api.api-ninjas.com/v1/iplookup?address={ip_address}"

# Make the API request
response = requests.get(api_url, headers={"X-Api-Key": "KEY"})

# Process the API response
if response.status_code == 200:
    data = response.json()
    if "country" in data:
        print("Country:", data["country"])
    else:
        print("Country information not available.")
    
    if "region" in data:
        print("Region:", data["region"])
    else:
        print("Region information not available.")
    
    if "city" in data:
        print("City:", data["city"])
    else:
        print("City information not available.")
    
    if "latitude" in data and "longitude" in data:
        print("Latitude:", data["latitude"])
        print("Longitude:", data["longitude"])
    else:
        print("Latitude and longitude information not available.")
    
    # ... add more fields as needed
else:
    print("Error:", response.status_code, response.text)
