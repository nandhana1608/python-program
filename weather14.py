import json
import pandas as pd

# Sample JSON data
data = '''
{
    "weather": [
        {"city": "Thrissur", "temperature": 30, "humidity": 75},
        {"city": "Kochi", "temperature": 32, "humidity": 80},
        {"city": "Kozhikode", "temperature": 29, "humidity": 70}
    ]
}
'''

# Parse JSON data
weather = json.loads(data)

# Convert JSON into table
df = pd.DataFrame(weather["weather"])

# Display weather details
print("Weather Information:")
print(df)

# Display summary
print("\nWeather Report:")

print("Average Temperature:", round(df["temperature"].mean(), 2), "°C")
print("Average Humidity:", round(df["humidity"].mean(), 2), "%")
hottest = df.loc[df["temperature"].idxmax()]
coldest = df.loc[df["temperature"].idxmin()]

print("Hottest City:", hottest["city"])
print("Coldest City:", coldest["city"])