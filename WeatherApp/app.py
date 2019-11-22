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

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    # print(data[0])
    # print("__________________________")
    # print(data[1])
    # print("__________________________")
    # print(data[2])
    print(data[2])
    return render_template('results.html')









if __name__=='__main__':
    app.run(debug=True)
