from flask import *
import random

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html")

@app.route("/RandomNumberGenerator", methods=["GET", "POST"])
def RnGen():
    if request.method == "POST":
        number = int(request.form.get("number"))
        result = randomize(number)
        number - 1
        return result
        # return render_template("RandomNumberGenerator.html")
    return render_template("RandomNumberGenerator.html")

def randomize(number):
    result = random.randrange(1, number)
    return str(result)




if __name__ == '__main__':
    app.run(debug=True)

