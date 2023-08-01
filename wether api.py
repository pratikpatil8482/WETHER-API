import requests

# Replace 'YOUR_API_KEY' with the provided API key
API_KEY = 'b6907d289e10d714a6e88b30761fae22'
BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "message" in data:
        print("Error:", data["message"])
    else:
        print(f"Weather forecast for {data['city']['name']}:")
        for forecast in data['list']:
            time = forecast['dt_txt']
            weather_description = forecast['weather'][0]['description']
            temperature = forecast['main']['temp']
            wind_speed = forecast['wind']['speed']
            pressure = forecast['main']['pressure']
            
            print(f"Time: {time}")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature} K")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Pressure: {pressure} hPa")
            print()

def main():
    while True:
        print("1. Get weather forecast for a city")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter the name of the city: ")
            get_weather(city)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
