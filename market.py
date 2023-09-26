from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__)
app.config['SQLALCHEMY_URI'] = "sqlite:///market.db"
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), 
                   primary_key=True)

    name = db.Column(db.String(length=30), 
                     nullable=False, 
                     unique=True)
    price = db.Column(db.Integer(),
                      nullable=False)
    barcode = db.Column(db.String(length=30), 
                        nullable=False, 
                        unique=True)
    description = db.Column(db.String(length=30), 
                            nullable=False, 
                            unique=True)



# @app.route("/")
# def hello_world():
#     return "<h1> Hello, World! !!</h1>"


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = [
        {"id":1, "name":"Phone", "barcode":"1234560001", "price":500},
        {"id":2, "name":"Laptop", "barcode":"1234560001", "price":900},
        {"id":3, "name":"Keyboard", "barcode":"1234560001", "price":150},
    ]
    return render_template("market.html", items=items)






# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'<h2>User {escape(username)}<h2>'


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'