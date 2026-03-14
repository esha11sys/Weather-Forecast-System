def display_current(data):
    if "name" not in data:
        print("Error:", data.get("message"))
        return

    print("\nCurrent Weather")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"])
    print("Weather:", data["weather"][0]["description"])

def display_forecast(data):
    if "list" not in data:
        print("Error:", data.get("message"))
        return

    print("\n5 Day Forecast")
    for item in data["list"][:5]:
        print(item["dt_txt"], "| Temp:", item["main"]["temp"], "|", item["weather"][0]["description"])
