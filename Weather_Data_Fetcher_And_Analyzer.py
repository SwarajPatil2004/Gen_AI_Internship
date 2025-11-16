import requests
import csv
from datetime import datetime

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather(city: str, api_key: str) -> dict:
    """
    Fetches weather data for a given city using OpenWeatherMap API
    """
    # Base URL for the OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Complete URL with query parameters (city, API key, metric units)
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make GET request to the API with 10 second timeout
        response = requests.get(complete_url, timeout=10)
        
        # Raise an exception if HTTP error occurred (4xx or 5xx status codes)
        response.raise_for_status()
        
        # Parse JSON response into Python dictionary
        weather_data = response.json()
        
        # Check if the API returned an error code
        if weather_data.get("cod") != 200:
            print(f"Error: {weather_data.get('message', 'Unknown error')}")
            return None
        
        # Return the weather data dictionary
        return weather_data
        
    except requests.exceptions.ConnectionError:
        # Handle network connection errors
        print("Error: Network connection failed. Check your internet.")
        return None
    except requests.exceptions.Timeout:
        # Handle timeout errors (request took too long)
        print("Error: Request timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (404, 500, etc.)
        print(f"Error: HTTP error occurred - {e}")
        return None
    except requests.exceptions.RequestException as e:
        # Handle any other request errors
        print(f"Error: Request failed - {e}")
        return None

# Function to analyze weather data and generate summary
def analyze_weather(weather_data: dict) -> str:
    """
    Analyzes weather data and returns a summary with temperature category and warnings
    """
    # Check if weather_data is None (error occurred in fetch)
    if weather_data is None:
        return "Error: No weather data to analyze."
    
    # Extract temperature from the 'main' section of the response
    temperature = weather_data['main']['temp']
    
    # Extract wind speed from the 'wind' section
    wind_speed = weather_data['wind']['speed']
    
    # Extract humidity from the 'main' section
    humidity = weather_data['main']['humidity']
    
    # Categorize temperature into Cold, Mild, or Hot
    if temperature <= 10:
        summary = "Cold (≤10°C)"
    elif temperature <= 24:
        summary = "Mild (11-24°C)"
    else:
        summary = "Hot (≥25°C)"
    
    # List to store warning messages
    warnings = []
    
    # Check if wind speed exceeds 10 m/s and add warning
    if wind_speed > 10:
        warnings.append("High wind alert!")
    
    # Check if humidity exceeds 80% and add warning
    if humidity > 80:
        warnings.append("Humid conditions!")
    
    # Combine summary with warnings if any exist
    if warnings:
        summary += " | " + " | ".join(warnings)
    
    # Return the complete summary string
    return summary

# Function to log weather data to a CSV file
def log_weather(city: str, api_key: str, filename: str):
    """
    Fetches weather for a city and appends the data to a CSV file
    """
    # Fetch weather data using the fetch_weather function
    weather_data = fetch_weather(city, api_key)
    
    # Check if data was successfully fetched
    if weather_data is None:
        print("Failed to fetch weather data. Not logging.")
        return
    
    # Get current timestamp in readable format
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Extract relevant data from the weather response
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']
    
    # Generate analysis summary
    analysis = analyze_weather(weather_data)
    
    try:
        # Open file in append mode ('a') to add new data without overwriting
        with open(filename, 'a', newline='') as file:
            # Create CSV writer object
            writer = csv.writer(file)
            
            # Check if file is empty (new file) to write headers
            file.seek(0, 2)  # Move to end of file
            if file.tell() == 0:  # File is empty
                # Write header row with column names
                writer.writerow(['Timestamp', 'City', 'Temperature(°C)', 'Humidity(%)', 
                               'Wind Speed(m/s)', 'Description', 'Analysis'])
            
            # Write data row with all weather information
            writer.writerow([timestamp, city, temperature, humidity, wind_speed, 
                           description, analysis])
        
        # Confirm successful logging
        print(f"Weather data for {city} logged to {filename}")
        
    except Exception as e:
        # Handle any file writing errors
        print(f"Error: Failed to write to file - {e}")

# Main program execution
if __name__ == "__main__":
    # Prompt user to enter their OpenWeatherMap API key
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    # Prompt user to enter city name
    city = input("Enter city name: ")
    
    # Define output filename
    filename = "weather_log.csv"
    
    # Fetch and display weather data
    print("\nFetching weather data...")
    weather_data = fetch_weather(city, api_key)
    
    # If data was successfully fetched, display analysis
    if weather_data:
        analysis = analyze_weather(weather_data)
        print(f"\nWeather Analysis: {analysis}")
        
        # Log the data to CSV file
        log_weather(city, api_key, filename)