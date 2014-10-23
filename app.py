from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def toTable(t,p):

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    c.execute('''create table if not exists posts(title text, post text)''')
    c.execute("INSERT INTO posts VALUES('" + t + "','" + p + "')")
    print c.fetchall()
    conn.commit()
    conn.close()
    

@app.route("/home", methods = ["GET","POST"])
@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        title = request.form["title"]
        post = request.form["post"]
        #button = request.form["b"]
        toTable(title,post)
        return render_template("home.html")
        
        

@app.route("/title")
def title():
    return render_template("title.html")


if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
