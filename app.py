from flask import Flask, render_template, request, abort, jsonify, redirect, send_from_directory
import os
app = Flask(__name__)

#posts = [[0, "Привет"], [1, "Hi, am new post"], [2, "Hello"]]

tree = os.walk(top='./cats',topdown=True)
a = list()
for i in tree:
    a= i[2]
posts = list()
count = 0
for i in a:
    posts.append([count,i])
    count += 1


print(type(posts))
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', posts=posts)
    if request.method == "POST":
        if "post_id" in request.form:
            id_post = request.form["post_id"]
            return redirect(f"/{id_post}")
        if "pics" in request.form:
            return send_from_directory("./cats", 'pics.jpg')

@app.route('/<int:post_id>', methods=["GET", "POST"])
def post_view(post_id):
    try:
        post_name = posts[post_id][1]
        return render_template("post_view.html", post_name=post_name)
    except IndexError:
        abort(418)



@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route('/pikabu', methods=["GET"])
def pikabu():
    return redirect("/about")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", debug=True)

