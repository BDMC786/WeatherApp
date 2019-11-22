def getWeather(city):
    import json
    import requests
    from datetime import datetime
    key = "5fc1f583fa2e15d8a27208e502ba5fb0"
    adj = 18000 # to be used as a way to convert to Eastern time, until a better method is found

    #Get user input from App as variable selection

    #Convert selection to coordinates 
    # selection = "Bayonne, NJ" #For Testing purposes ONLY
    
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude

    #Get location name from geopy
    city_mod = f"{location}".split(", ")
    place = f'{city_mod[0]}, {city_mod[2]}'
 

    #Get URL for API call to DarkSky
    url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'

    #Make API Call
    response = requests.get(url)
    response_json = response.json()

    #Get Current Conditions from API data
    current_weather = response_json["currently"]

    #Pull data from current conditions
    current_dict = {}
    current_list_try = ["apparentTemperature",  "cloudCover", "humidity", "precipIntensity", "precipProbability", "summary", "temperature", "time", "uvIndex"]
    current_list = []
    for x in current_list_try:
        if x in current_weather:
            current_list.append(x)
            current_dict[x] = current_weather[x]
    #Gets the Day of the week and the time in AM PM format
    current_dict["time"] = f"{datetime.utcfromtimestamp(current_dict['time']).strftime('%A')} {datetime.utcfromtimestamp(current_dict['time']).strftime('%H:%M')}"

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

    #Convert Time to AM/PM fprmat
    for hours in hourly_list:
        #print(hours["time"])
        hours["time"] =  datetime.utcfromtimestamp(hours["time"]).strftime('%r')
        

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
    data = [place, current_dict, hourly_list, daily_list]

    return data

# getWeather()