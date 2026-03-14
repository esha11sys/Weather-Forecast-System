from .weather_api import get_current_weather, get_forecast
from .config import API_KEY
import json

FAV_FILE="data/favourites.json"

def fetch_current(city):
    return get_current_weather(city)

def fetch_forecast(city):
    return get_forecast(city)

#-----------------FAVORITES FEATURE------------------#

def load_favorites():
    try:
        with open(FAV_FILE,"r") as file:
            return json.load(file)

            if data is None:
                return []

            return data     
    except:
        return[]

def save_favorites(favorites):
    with open(FAV_FILE,"w") as file:
        json.dump(favorites,file,indent=4)

def add_favorite(city):
    favorites = load_favorites()

    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        print(city,"added to favorites")
    else:
        print("city already in favorites")

def show_favorites():
    favorites = load_favorites()

    if not favorites:
        print("no favorite cities yet")
    else:
        print("\nFavorite Cities:")
        for city in favorites:
            print("-",city)

def show_favorite_weather():
    favorite=load_favorites()


    if not favorite:
        print("no favorite cities found.")
        return

    print("\favorite cities weather\n")

    for city in favorite:
        data=fetch_current(city)

        if data.get("cod")==200:
            temp=data["main"]["temp"]
            desc=data["weather"][0]["description"]

            print(f"{city}:{temp}degree celcius,{desc}")
        else:
            print(f"{city}:weather data not available")                                                           

