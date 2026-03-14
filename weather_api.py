from src.config import API_KEY
import requests

def get_current_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print(url)
    response = requests.get(url)
    return response.json()

def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    print(url)
    response = requests.get(url)
    return response.json()
