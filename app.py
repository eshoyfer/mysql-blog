from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    #dat = request.args.get(
    return render_template("home.html")

@app.route("/title")
def title():
    return render_template("title.html")


if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
