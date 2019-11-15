from flask import Flask, request, render_template
import getData
#import scrape #Name of functions from getData.py file, code to be reconfig'ed to functions later

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html') #MUST credit DarkSky and link to page


@app.route('/', methods=['POST'])
def getKey():
    print("_________________________")
    city = request.form['text']
    key = key #Needs to be it's own function
    print("key")
    print(key)
    print("test")
    coordinates = getData.LatLong(city)
    latitude = coordinates[0]
    longitude = coordinates[1]
    print(latitude)
    print(longitude)
    return render_template('index.html')
    #team = request.form['text'] #Example for getting User Input
    #return render_template("results.html",  background =  background, record = record ) #Example for this App, set variables (e.g. "daily_weather to this program")






if __name__=='__main__':
    app.run(debug=True)
