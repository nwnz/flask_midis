from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

posts = ("Привет","Hi, am new post","Hello")

@app.route('/', methods=["GET", "POST"])
def index():
    return jsonify(posts)

@app.route('/<int:post_id>', methods=["GET", "POST"])
def post_view(post_id):
    try:
        post_id_view = posts[int(post_id)]
        return render_template("post_view.html", post_id_view=post_id_view, post_id=post_id)
    except IndexError:
        abort(418)


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", debug=True)

