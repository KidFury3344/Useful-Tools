from flask import *
import random

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html")

@app.route("/RandomNumberGenerator", methods=["GET", "POST"])
def RnGen():
    global l 
    l = []
    if request.method == "POST" and request.form.get("number") != "":
        num = int(request.form.get("number"))
        for i in range(1, num+1):
            l.append(i)
        return redirect("/RNGResult", 302)
    return render_template("RandomNumberGenerator.html")

@app.route("/RNGResult", methods=["GET", "POST"])
def RNGResult():
    if request.method == "POST" and request.form["generate"] == "Generate Number" and len(l) > 1:
        random.shuffle(l)
        result = l[0]
        l.sort()
        l.remove(result)
        out = l[-1]
        return render_template("RNGResult.html", out = str(out), result=str(result))
    elif request.method == "POST" and request.form["generate"] == "Generate Number" and len(l) == 1 :
        return redirect("/RandomNumberGenerator", 302)
    elif request.method == "POST" and request.form["generate"] == "Reset":
        return redirect("/RandomNumberGenerator", 302)
    else:
        random.shuffle(l)
        result = l[0]
        l.sort()
        l.remove(result)
        out = l[-1]
        return render_template("RNGResult.html", out = str(out), result=str(result))


if __name__ == '__main__':
    app.run(debug=True)

