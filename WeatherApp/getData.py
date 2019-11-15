# # Depenencies
# import json
# import requests
# key = "5fc1f583fa2e15d8a27208e502ba5fb0"

# #Get user input from App as variable selection

# #Convert selection to coordinates 
# selection = "Bayonne, NJ" #For Testing purposes ONLY
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
# location = geolocator.geocode(selection)
# latitude = location.latitude
# longitude = location.longitude
# print(latitude) #TEST

# #Get URL for API call to DarkSky
# url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'

# #Make API Call
# url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'
# print(url) #TEST
# response = requests.get(url)
# response_json = response.json()

# #Get Current Conditions from API data
# current_weather = response_json["currently"]

# #Pull data from current conditions
# current_dict = {}
# current_list = ["apparentTemperature", "cloudCover", "humidity", "precipIntensity", "precipProbability", "summary", "temperature", "time", "uvIndex"]
# for x in current_list:
#     current_dict[x] = current_weather[x]

# #Hourly Conditions
# hourly_weather = response_json["hourly"]["data"]


# #Pull data from Hourly Conditions
# hourly_list = []
# hourly_elements = ["apparentTemperature", "cloudCover", "humidity", "precipIntensity", "precipProbability", 
#                   "summary", "temperature", "time", "uvIndex", "windSpeed"]
# for hours in hourly_weather:
#     hour_dict = {}
#     for elements in hourly_elements:        
#         hour_dict[elements] = hours[elements]
#     hourly_list.append(hour_dict)

# #Daily
# daily_weather = response_json["daily"]["data"]

# #Pull data from Daily Conditions
# daily_elements = ["cloudCover", "humidity", "icon", "precipIntensity", "precipIntensityMax", 
# "precipIntensityMaxTime", "precipProbability", "precipType", "summary", "sunriseTime", "sunsetTime", "temperatureHigh", 
# "temperatureHighTime", "temperatureLow", "temperatureLowTime", "time", "uvIndex", "uvIndexTime", "windSpeed"] 
# daily_list = []

# for days in daily_weather:
#     daily_dict = {}
#     for elements in daily_elements:        
#         daily_dict[elements] = days[elements]
#     daily_list.append(daily_dict)

# #Complete Above Works, attempting below to break into functions
# # print("END")

#Going to attempt geolocator function first:
def key():
    key = "5fc1f583fa2e15d8a27208e502ba5fb0"
    return key
    #Works!
    #Get user input from App as variable selection

    #Convert selection to coordinates 
def LatLong(city):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    coordinates = [latitude, longitude]
    return coordinates
    key = "5fc1f583fa2e15d8a27208e502ba5fb0"
    return key

