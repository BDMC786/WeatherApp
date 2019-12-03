from flask import Flask, request, render_template
import getData
import getBayonne
import getMontclair
#import scrape #Name of functions from getData.py file, code to be reconfig'ed to functions later

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html') #MUST credit DarkSky and link to page


@app.route('/', methods=['POST'])
def function():
    city = request.form['text']

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

    try:
        data = getData.getWeather(city)
    except:
        return render_template("error.html")

    return render_template('shortcut.html', data = data)


if __name__=='__main__':
    app.run(debug=True)
