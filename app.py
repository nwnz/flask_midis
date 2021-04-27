#im here
from flask import Flask, render_template, request, abort, jsonify, redirect, send_from_directory
from flask_httpauth import HTTPBasicAuth
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


@app.route('/user/<user_id>', methods=["GET"])
def get_user_lk(user_id):
    user_link = {"user_id" : user_id, "lisk_list" : ["www.google.com, www.ya.ru, www.vk.com"]  }
    return jsonify(user_link)

@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html") , 200

@app.route('/pikabu', methods=["GET"])
def pikabu():
    return redirect("/about")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", debug=True)



# from flask import Flask
# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash
#
# app = Flask(__name__)
# auth = HTTPBasicAuth()
#
# users = {
#     "john": generate_password_hash("hello"),
#     "susan": generate_password_hash("bye")
# }
#
# @auth.verify_password
# def verify_password(username, password):
#     if username in users and \
#             check_password_hash(users.get(username), password):
#         return username
#
# @app.route('/')
# @auth.login_required
# def index():
#     return "Hello, {}!".format(auth.current_user())
#
# if __name__ == '__main__':
#     app.run()
