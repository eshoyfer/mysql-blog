from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Given title and post, will add the values into the table accordingly
def toTable(title, post):

    # Setting up SQLite stuff.
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    # Does it exist? If not, create it.
    # In either case, insert the values as requested.
    c.execute('''create table if not exists posts(title text, post text)''')
    c.execute("INSERT INTO posts VALUES(%s, %s)" % (title, post))

    # A note on functionality: 
    # Given an identical title, the entries will coexist. 
    # A request for a particular title page will yield all entries with the same title.

    print c.fetchall()
    conn.commit()
    conn.close()

# Given a title, will return an iterable of associated blog posts.
# [List of Strings] 
def postsWithTitle(title):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()  

    q = '''
    SELECT post FROM POSTS WHERE title == %s
    ''' % (title)

    sql_posts_table = c.execute(q) 
    posts_list = []

    for post in sql_posts_table:
        print post
        posts_list.append(post[0])

    #print posts_list

    return posts_list
    

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
        
        

@app.route("/<title>")
def title(title):

    rows = postsWithTitle(title)
    return render_template("title.html", comments=rows)

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
