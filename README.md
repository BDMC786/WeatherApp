# WeatherApp

Web application available here: https://weatherbri.herokuapp.com/

This repo contains a weather forecast application. It is a live web application hosted on Heroku. 

This is a flask application. It also uses geopy Nominatim. 

This web application gives the weather forecast for any location in the world. It takes the users request by two means. The first is the search feature, where a user can enter any location, such as a city and state, county, a named location (e.g. "Empire State Building"), or a street address. The input is sent to the back end, where Nominatim converts the location entered into geographical coordinates. These coordinates are used to send the API call to Dark Sky to retrieve the data. The data is parsed and processed (desired data is extracted and transformed including formatting, and organized for rendering). The data is returned to the app.py file and rendered. The second method for getting a forecast is to use the shortcut links on the home page (index.html) to get the weather for that location. This was added as a convenience since I would be using this for my personal use, location I (or my family and frinds) would find most useful were given easier access. These links navigate to that location's specific route. The app then gets the forecast for that location with a seperate python file with a hard coded url for the API call for that specific location. Everything else works as the search option.


This version unfortunately contains an error that I didn't anticipate. I made the mistake of hard-coding the timezone offset. This means that during daylight saving time, the time is off by an hour. Subsequently, the days are off as well. Obviously this is a significant flaw. I have learned an important lesson about the pitfalls of hard coding values! 

Later versions of this contain not only a fix for my coding blunder, but also cleaner, more efficient coding practices. It also has additional features for users. 

Unfortunately, Dark Sky API has been bought by Apple and will no longer be accepting API calls from the public once 2022 ends. I will be leaving this up until then even as I move to my subsequent iterations of this application using Open Sky API as my data source. I wanted the versions to be seperate and distinct, so I have not simply replaced this version with later versions. 
