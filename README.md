# Weather App

Python CLI weather application using OpenWeather API.

## Features
- Current weather
- 5 day forecast
- Search history saved in JSON
- Modular project structure

## Run

pip install -r requirements.txt
python main.py


Weather Forecast Application

Project Description

The Weather Forecast Application is a command-line based Python project that allows users to check real-time weather information for any city. The application uses the OpenWeatherMap API to fetch weather data and display details such as temperature, humidity, weather description, and wind speed.

The application also stores search history and allows users to save favorite cities, making it easy to quickly check weather for frequently searched locations.

This project demonstrates the use of APIs, JSON file handling, modular programming, and command-line interfaces in Python.

---

Features

- Check current weather for any city
- View 5-day weather forecast
- Save search history
- Add and manage favorite cities
- View weather for all favorite cities
- Displays weather details including:
   - Temperature
   - Humidity
   - Weather description
   - Wind speed
- JSON-based persistent data storage
- Simple command-line interface
- Input validation
- Error handling for invalid city names

---

Tech Stack

- Python 3.8+
- Command Line Interface (CLI)
- OpenWeatherMap API
- JSON for data storage
- Requests library for API calls
- VS Code as IDE
- Git (optional for version control)

---

Installation Instructions

1. Install Python

Make sure Python 3.8 or above is installed.

Check using:

python --version

---

2. Download or Copy the Project Folder

Place the project folder on your computer.https://github.com/esha11sys/Weather-Forecast-System.git

---

3. Install Required Library

Install the requests library:

pip install requests

---

4. Add Your API Key

Open the file:

config.py

Add your OpenWeatherMap API key:

API_KEY = "your_api_key_here"

You can generate a free API key from:

https://openweathermap.org/api

---

How to Run the Project

Open terminal in the project directory and run:

python main.py

Follow the menu options displayed on the screen.

---

Example Menu

==== Weather Forecast Application ====

1 Current Weather
2 Five Day Forecast
3 View Search History
4 Add Favorite City
5 View Favorite Cities
6 Favorite Cities Weather
7 Exit

---

Example Output

Enter city name: London

City: London
Temperature: 9°C
Humidity: 63%
Weather: scattered clouds
Wind Speed: 3.7 m/s

---

Project Structure

WeatherApp

main.py
README.md
requirement.txt
tutorial.md

src/
    init.py
    weather.py
    weather_api.py
    formatter.py
    config.py

data/
    search_history.json
    favorites.json

tests/

cache/

---

Screenshots

Screenshots of the application output are included in the project folder inside the Word document file and also in screenshot folder
###Weather app###
![main menu](screenshot/current_weather.png)
![main menu](screenshot/favorite_cities2.png)
![main menu](screenshot/search_history.png)
![main mainu](screenshot/favorite_cities_weather.png)


---

Libraries Used

1. requests - for making API requests to openweathermap
2. json(built-in)- for storing search history and fovorite cities
3. datetime(built-in)- for handling time and date information

---

Tools Used
1. JSON for data persistence
2. Git for version control
3. CLI interface for user interaction
4. VS code as development enviroment

---

Skills and Concepts Used
1. python programming fundamentals
2. API Inegration using request
3. File handling with JSON
5. Command line interface application development
6. input validation and error handling
7. Menu driven program design
8. Basic data structures
9. Exception handling using try and except blocks

---

Why this project Matters (Real World Relevance)

Weather information is widely used in daily life for planning travel, outdoor activities, and logistics. This project demonstrates how software applications can integrate external APIs to provide real time information.
The application handles real world scenarios such as:
1. Fetching real-time weather data
2. Managing frequently searched cities
3. Storing User preferances
5. Display weather information in an easy to read format


This concepts are commonly used in weather  applications, travel apps and real time data systems.

---


Why recruiters value this :
This projest demonstrates understanding of:
1. API integration
2. data storage using JSON
3. CLI application development
4. Modular python programming
5. Error Handling and input validation

These are common skills required for backend development and realworld software applications.

---

Future Improvements

- Add graphical interface using Tkinter
- Display weather icons
- Add hourly weather forecast
- Export weather data to CSV
- Improve error handling

---

Author

Name:Kamakshi Mante
Batch: ITC Infotech - Python Developer
Submission Date:11 March 2026
Email:singwithyun@gmail.com

Python Weather Information System with API Integration Project
