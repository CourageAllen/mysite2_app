from flask import Flask, render_template

app = Flask(__name__ )

@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/about")
def about():
    return " <h3> About Page </h3>"  


##This is where we run our app

if __name__  == " __main__":
    app.run(
        debug = True,
        port = 3000
    )