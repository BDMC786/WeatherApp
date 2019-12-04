from flask import Flask, request, render_template
import getData
import getBayonne
import getMontclair
import getNYC
#import scrape #Name of functions from getData.py file, code to be reconfig'ed to functions later

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html') #MUST credit DarkSky and link to page


@app.route('/', methods=['POST'])
def function():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/bayonne")
def bayonne():
    try:
        data = getBayonne.getBayonne()
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/bayonne', methods=['POST'])
def bayonneFunction():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)


@app.route("/montclair")
def montclair():
    try:
        data = getMontclair.getMontclair()
    except:
        return render_template("error.html")

    return render_template('shortcut.html', data = data)

@app.route('/montclair', methods=['POST'])
def montclairFunction():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('shortcut.html', data = data)


@app.route("/new_york")
def NYC():
    try:
        data = getNYC.getNYC()
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/new_york', methods=['POST'])
def NYCFunction():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/culver_IN")
def Culver():
    import getCulver
    try:
        data = getCulver.getCulver()
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/culver_IN', methods=['POST'])
def CulverFunction():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/hightstown")
def Hightstown():
    import getHightstown
    try:
        data = getHightstown.getHightstown()
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/hightstown', methods=['POST'])
def HightstownFunction():
    city = request.form['text']

    if city.lower() == "new york":
        city = "manhattan"
    elif city.lower() == "new york, ny":
        city = "manhattan"
    elif city.lower() == "new york, new york":
        city = "manhattan"
    elif city.lower() == "new york ny":
        city = "manhattan"
    elif city.lower() == "new york new york":
        city = "manhattan"

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)


if __name__=='__main__':
    app.run(debug=True)
