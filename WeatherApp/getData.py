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

##Going to attempt geolocator function first:
# def key():
#     key = "5fc1f583fa2e15d8a27208e502ba5fb0"
#     return key
#     #Works!
#     #Get user input from App as variable selection

#     #Convert selection to coordinates 
# def LatLong(city):
#     from geopy.geocoders import Nominatim
#     geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
#     location = geolocator.geocode(city)
#     latitude = location.latitude
#     longitude = location.longitude
#     coordinates = [latitude, longitude]
#     return coordinates
#     # key = "5fc1f583fa2e15d8a27208e502ba5fb0"
#     # return key
#     url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'
#     return url
#     key = "5fc1f583fa2e15d8a27208e502ba5fb0"
#     url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'
#     return url

# def URL(city):
#     from geopy.geocoders import Nominatim
#     geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
#     location = geolocator.geocode(city)
#     latitude = location.latitude
#     longitude = location.longitude
#     # coordinates = [latitude, longitude]
#     # return coordinates
#     key = "5fc1f583fa2e15d8a27208e502ba5fb0"
#     # return key
#     url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'
#     print(url)
#     return url

# URL("Bayonne, NJ")
# print("ok")

def getWeather(city):
    import json
    import requests
    key = "5fc1f583fa2e15d8a27208e502ba5fb0"

    #Get user input from App as variable selection

    #Convert selection to coordinates 
    # selection = "Bayonne, NJ" #For Testing purposes ONLY
    
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
 

    #Get URL for API call to DarkSky
    url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'

    #Make API Call
    response = requests.get(url)
    response_json = response.json()

    #Get Current Conditions from API data
    current_weather = response_json["currently"]

    #Pull data from current conditions
    current_dict = {}
    current_list_try = ["apparentTemperature", "TEST", "cloudCover", "humidity", "precipIntensity", "precipProbability", "summary", "temperature", "time", "uvIndex"]
    current_list = []
    for x in current_list_try:
        if x in current_weather:
            current_list.append(x)
            current_dict[x] = current_weather[x]
    # print("Current Weather Complete")
    # print(current_dict)
    #Hourly Conditions
    hourly_weather = response_json["hourly"]["data"]
    #Pull data from Hourly Conditions
    hourly_list = []
    hourly_elements_try = ["apparentTemperature", "cloudCover", "humidity", "precipIntensity", "precipProbability", 
                    "summary", "temperature", "time", "uvIndex", "windSpeed"]
    hourly_elements = []
    for hours in hourly_weather:
        hour_dict = {}
        for element in hourly_elements_try:
            if element in hours:
                hour_dict[element] = hours[element]
                if element not in hourly_elements:
                    hourly_elements.append(element)
        hourly_list.append(hour_dict)
    # print("hourly weather complete")
    # print(hourly_list)
    #Daily
    daily_weather = response_json["daily"]["data"]

    #Pull data from Daily Conditions
    daily_elements_try = ["cloudCover", "humidity", "icon", "precipIntensity", "precipIntensityMax", 
    "precipIntensityMaxTime", "precipProbability", "precipType", "summary", "sunriseTime", "sunsetTime", "temperatureHigh", 
    "temperatureHighTime", "temperatureLow", "temperatureLowTime", "time", "uvIndex", "uvIndexTime", "windSpeed"] 
    daily_elements = []
    daily_list = []

    for days in daily_weather:
    #     print(days)
    #     print("_____________")
        daily_dict = {}
        for elements in daily_elements_try:
    #         print(elements)
            if elements in days:
    #             print(elements)
                daily_dict[elements] = days[elements]
                if elements not in daily_elements:
                    daily_elements.append(elements)
        daily_list.append(daily_dict)
    # print("daily weather complete")
    # print(daily_list)
    #Add all data sets to a list to pass to app
    data = [current_dict, hourly_list, daily_list]

    return data

# getWeather()