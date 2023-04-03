"""
This program will ask the user to enter a city name, and the program will retrieve weather data and display it.
The program is written in python. Weather data is retrieved through an API service. The information is processed
displayed.

Name: TonyMontana-dev
"""

# IMPORT THE MODULES REQUIRED IN ORDER TO RUN THIS PROGRAM
# KEYS is a personal file where you should store your API KEYS for security. Check the readme document for more information
import requests, json, keys


# Introduction method
def introduction():
    print("Welcome to the WeatherToday!")
    name = input("Please enter your name: ")

    print("\nHello ", name)
    print("Here you will be able to enter the name of a city in the world, and retrive current weather data.")


# Main processes of the program elaboration | METHOD
def WeatherProgram():
    # Input phase
    city_name = input("\nPlease enter the name of the city: ")  # Save input into a variable
    base_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={keys.api_key}"  # Use variable to create URL variable and import API KEY from keys.py
    data = requests.get(base_URL)  # Request data file from URL

    x = data.json()  # Convert JSON file to Python formatted file

    if (x['cod'] != '404'):
        # DECLARE WEATHER VARIABLES
        print(f"\nLocation ----> {data.json().get('name')}, {data.json().get('sys').get('country')}")  # Retrieve location data
        print(f"Temperature ----> {data.json().get('main')['temp']}°F")  # Retrieve Temperature
        print(f"Weather description ----> {data.json().get('weather')[0].get('description')}")  # Retrieve Weather description
        print(f"Min/Max Temperature ----> {data.json().get('main')['temp_min']}°F/{data.json().get('main')['temp_max']}°F")  # Retrieve Min/Max temperature data
        print(f"Humidity ----> {data.json().get('main')['humidity']}%")  # Retrieve Humidity data
        print(f"Wind ----> {data.json().get('wind')['speed']} mph")  # Retrieve Wind data

    else:
        print("\n << ! Invalid Input ! >>\nThe name of the city entered was not found.")  # Return error statement for mistaken input


# MAIN FUNCTION
def main():
    introduction()  # Call function introduction
    flag = True  # Set status of the loop to TRUE == GO AHEAD
    WeatherProgram()  # Call main program function
    while (flag == True):
        choice = input("\nWould you like to search for another city? <yes/no>\nEnter choice: ")  # Ask if user wants to continue
        if (choice == "yes" or choice == "y"):
            WeatherProgram()
        elif (choice == "no" or choice == "n"):
            print("\nThank you for using the program.\nGood Bye!")  # Exit program with a conclusion statement
            flag = False  # Set status of the loop to False == STOP IMMEDIATELY


# START PROGRAM
main()
