from flask import Flask, request, render_template
import getData
#import scrape #Name of functions from getData.py file, code to be reconfig'ed to functions later

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html') #MUST credit DarkSky and link to page


@app.route('/', methods=['POST'])
def function():
    print("_________________________")
    city = request.form['text']
    # # key = key #Needs to be it's own function
    # # print("key")
    # # print(key)
    # print("test")
    # coordinates = getData.LatLong(city)
    # latitude = coordinates[0]
    # longitude = coordinates[1]
    # print("Latitude")
    # print(latitude)
    # print(longitude)
    # key = getData.key() # from key funtion
    # print("key:")
    # print(key) #
    # return render_template('index.html')
    # url = getData.URL()
    # print("URL")
    # print(url)
    # # print("END")
    # url = getData.URL(city)
    # print(url)
    print(city)
    data = getData.getWeather(city)

    print(data[0])
    print("____________________________")
    print(data[1])
    print("____________________________")
    print(data[2])

    return render_template('results.html')









if __name__=='__main__':
    app.run(debug=True)
