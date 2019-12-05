def getHightstown():
    import json
    import requests
    from datetime import datetime as dt
    import datetime, pytz

    url = "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.2695538,-74.5232089"
    place = "Hightstown, NJ"

    #Make API Call
    response = requests.get(url)
    response_json = response.json()


    time_adjust = -18000

    #Get Current Conditions from API data
    current_weather = response_json["currently"]

    #Pull data from current conditions
    current_dict = {}
    current_list_try = ["apparentTemperature",  "cloudCover", "humidity", "precipIntensity", "precipAccumulation", "precipProbability", "summary", "temperature", "time", "uvIndex"]

    for elements in current_list_try:
        if elements in current_weather:
            current_dict[elements] = current_weather[elements]
            
    #Adjusts Time to local time
    current_dict["time"] = current_dict["time"] + time_adjust

    #Gets the Day of the week and the time in AM PM format
    current_dict["time"] = f"{dt.utcfromtimestamp(current_dict['time']).strftime('%A')} {dt.utcfromtimestamp(current_dict['time']).strftime('%r')}"
    
    #Correct Formats Current
    current_dict["apparentTemperature"] = f'{round(current_dict["apparentTemperature"])} °F' #Round 
    current_dict["cloudCover"] = f'{round(current_dict["cloudCover"] * 100)}%' #Percentage
    current_dict["humidity"] = f'{round(current_dict["humidity"] * 100)}%'
    current_dict["precipProbability"] = f'{round(current_dict["precipProbability"] * 100)}%'
    current_dict["temperature"] = f'{round(current_dict["temperature"])} °F'
    if "precipAccumulation" in current_dict:
        current_dict["precipAccumulation"] = f'Snowfall Accumulation: {current_dict["precipAccumulation"]} Inches'
    

    #Hourly Conditions
    hourly_weather = response_json["hourly"]["data"]

    #Pull data from Hourly Conditions
    hourly_list = []
    hourly_elements_try = ["apparentTemperature", "cloudCover", "humidity", "precipIntensity", "precipAccumulation", "precipProbability", 
                    "summary", "temperature", "time", "uvIndex", "windSpeed"]
    hourly_elements = []
    for hours in hourly_weather:
        hour_dict = {}
        for element in hourly_elements_try:
            if element in hours:
                hour_dict[element] = hours[element]
                if element not in hourly_elements:
                    hourly_elements.append(element)
        try:
            hour_dict["time"] = dt.utcfromtimestamp(int(hours["time"]) + int(time_adjust)).strftime('%A %r')
        except:
            print('hour_dict["time"] failed')
        try:
            hour_dict["apparentTemperature"] = f'{round(hour_dict["apparentTemperature"])} °F' #Round 
        except:
            print('hour_dict["apparentTemperature"] failed')
        try:
            hour_dict["cloudCover"] = f'{round(hour_dict["cloudCover"] * 100)}%' #Percentage
        except:
            print('hour_dict["cloudCover"] failed')
        try:
            hour_dict["humidity"] = f'{round(hour_dict["humidity"] * 100)}%'
        except:
            print('hour_dict["humidity"] failed')
        try:
            hour_dict["precipProbability"] = f'{round(hour_dict["precipProbability"] * 100)}%'
        except:
            print('hour_dict["precipProbability"] failed')
        try:
            hour_dict["temperature"] = f'{round(hour_dict["temperature"])} °F'
        except:
            print('hour_dict["temperature"] failed')
        try:
            hour_dict["windSpeed"] = round(hour_dict["windSpeed"])
        except:
            print('hour_dict["windSpeed"]')
        
        hourly_list.append(hour_dict)


    #Daily
    daily_weather = response_json["daily"]["data"]

    #Pull data from Daily Conditions
    daily_elements_try = ["cloudCover", "humidity", "icon", "precipIntensity", "precipIntensityMax", 
    "precipIntensityMaxTime", "precipProbability", "precipType", "precipAccumulation", "summary", "sunriseTime", "sunsetTime", "temperatureHigh", 
    "temperatureHighTime", "temperatureLow", "temperatureLowTime", "time", "uvIndex", "uvIndexTime", "windSpeed"] 
    daily_elements = []
    daily_list = []

    for days in daily_weather:
        daily_dict = {}
        for elements in daily_elements_try:
            # print("elements")
            if elements in days:
                # print(elements)
                daily_dict[elements] = days[elements]
                # print(daily_dict[elements])
                if elements not in daily_elements:
                    daily_elements.append(elements)
                    # print(daily_elements)
        try:
            daily_dict["cloudCover"] = f'{round(daily_dict["cloudCover"] * 100)}%'
        except:
            print('daily_dict["cloudCover"] failed')
        try:
            daily_dict["humidity"] = f'{round(daily_dict["humidity"] * 100)}%'
        except:
            print('daily_dict["humidity"] failed')
        try:
            daily_dict["precipProbability"] = f'{round(daily_dict["precipProbability"] * 100)}%'
        except:
            print('daily_dict["precipProbability"] failed')
        try:
            daily_dict["temperatureHigh"] = f'{round(daily_dict["temperatureHigh"])} °F'
        except:
            print('daily_dict["temperatureHigh"] failed')
        try:
            daily_dict["temperatureLow"] = f'{round(daily_dict["temperatureLow"])} °F'
        except:
            print('daily_dict["temperatureLow"] failed')
        try:
            daily_dict["windSpeed"] = round(daily_dict["windSpeed"])
        except:
            print('daily_dict["windSpeed"] failed')

        #TIMES
        try:
            daily_dict["precipIntensityMaxTime"] = f"{dt.utcfromtimestamp(daily_dict['precipIntensityMaxTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["precipIntensityMaxTime"] failed')
        try:
            daily_dict["sunriseTime"] = f"{dt.utcfromtimestamp(daily_dict['sunriseTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["sunriseTime"] failed')
        try:
            daily_dict["sunsetTime"] = f"{dt.utcfromtimestamp(daily_dict['sunsetTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["sunsetTime"] failed')
        try:
            daily_dict["temperatureHighTime"] = f"{dt.utcfromtimestamp(daily_dict['temperatureHighTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["temperatureHighTime"] failed')
        try:
            daily_dict["temperatureLowTime"] = f"{dt.utcfromtimestamp(daily_dict['temperatureLowTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["temperatureLowTime"] failed')
        try:
            daily_dict["time"] = f"{dt.utcfromtimestamp(daily_dict['time'] + time_adjust).strftime('%A %B %d')}"
        except:
            print('daily_dict["time"] failed')
        try:
            daily_dict["uvIndexTime"] = f"{dt.utcfromtimestamp(daily_dict['uvIndexTime'] + time_adjust).strftime('%r')}"
        except:
            print('daily_dict["uvIndexTime"] failed')
        
        # print(daily_dict["precipIntensityMaxTime"])
        
        daily_list.append(daily_dict)
        


    #Add all data sets to a list to pass to app
    try:
        next_hour = response_json["minutely"]["summary"]
    except:
        print("next hour failed")
        next_hour = "Unavailable"

    data = [place, current_dict, hourly_list, daily_list, next_hour]

        #Add Alerts
    if "alerts" in response_json:
        all_alerts = response_json["alerts"]
        alerts = []
        for messages in all_alerts:
            alerts.append(messages["description"])
    else:
        alerts = []
        alerts.append("CLEAR") 
        data.append(alerts)

    print("END")

    return data