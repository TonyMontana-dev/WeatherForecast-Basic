# WeatherForecast Basic
This program is called WeatherForecast. The purpose of this program is to let the user choose a
city and retrieve the current meteorological data available through the API provided by
OpenWeatherMap.

# What are APIs?
Let's start with an explanation of what an API is and why we use them. API stands for
Application Programming Interface and is used to make two computers or computer
programs communicate. APIs will provide different types of services based on the purpose.
OpenWeatherMap gives us the availability to retrieve with a free account current weather
data based on a city name, city ID, geographic coordinates, and/or zip code. The city name is
accepted in more than 30 languages and the data is retrieved for the current time of the
request. The program has a database of 200,000 cities, and it will provide information
collected from different sources (satellites, local weather models, radars, etc…). The API will
provide three formats of data sets such as JSON, XML, and HTML, then since we are using
Python in this program, convert it into a python-formatted file.
What are the main processes of this program?

# Which data will the program provide?
The program will ask the user for a city name, then it will display the following data:
  ● Location name
  ● Temperature data
  ● Weather description
  ● Minimum & Maximum Temperature data
  ● Humidity data
  ● Wind data

The program will let the user choose if he/she wants to continue searching for other
cities or exit the program. Also, if the input is mistaken, it will provide an exception
statement describing the error.

# IMPORTANT NOTE
Note that this program uses two Python libraries. JSON and requests, the last one is
not a built-in library. Therefore, you will probably need to install it before running the
program (A suggestion would be to try with a 3.8 or lower version of the python IDLE).
Below you will find two URLs that will help you with the installation of the required
library.
# USEFUL URLs for REQUIREMENTS
Link to the download and instructions for the correct installation:
Download Files → https://pypi.org/project/requests/#files
Library description and guide → https://pypi.org/project/requests/#description
Entire documentation of the library → https://docs.python-requests.org/en/latest

--- END OF README NOTE ---
