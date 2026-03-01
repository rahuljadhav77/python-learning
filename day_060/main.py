import json

def get_weather(city):
    # Simulating an API response
    api_response = {
        "London": {"temp": 15, "condition": "Cloudy"},
        "New York": {"temp": 22, "condition": "Sunny"},
        "Tokyo": {"temp": 18, "condition": "Rainy"}
    }
    
    data = api_response.get(city, {"temp": "Unknown", "condition": "N/A"})
    print(f"Weather in {city}: {data['temp']}°C, {data['condition']}")

if __name__ == '__main__':
    cities = ["London", "New York"]
    for city in cities:
        get_weather(city)
