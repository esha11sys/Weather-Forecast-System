import json
from src.weather_api import get_current_weather, get_forecast
from src.formatter import display_current, display_forecast
from src.config import API_KEY
from src.weather import add_favorite,show_favorites
from src.weather import show_favorite_weather

HISTORY_FILE = "data/search_history.json"

def save_history(city):
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []
    history.append(city)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_history():
    try:
        with open(HISTORY_FILE) as f:
            history = json.load(f)
        print("\nSearch History:")
        for city in history:
            print("-", city)
    except:
        print("No history found")

def menu():
    while True:
        print("\n------Weather App---------")
        print("1 Current Weather")
        print("2 Five Day Forecast")
        print("3 Search History")
        print("4 add favorite city")
        print("5 show favorite cities")
        print("6 favorite cities weather")
        print("7 Exit")

        choice = input("Choose: ")

        if choice == "1":
            city = input("Enter city: ")
            data = get_current_weather(city)
            display_current(data)
            save_history(city)

        elif choice == "2":
            city = input("Enter city: ")
            data = get_forecast(city)
            display_forecast(data)
            save_history(city)

        elif choice == "3":
            show_history()

        elif choice == "4":
            city = input("enter city name:")
            add_favorite(city)
            
        elif choice =="5":
            show_favorites()
        elif choice=="6":
            show_favorite_weather()
        elif choice=="7":    
            break;        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
