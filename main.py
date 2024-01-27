from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.rating}"


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["book"]
                        , author=request.form["author"]
                        , rating=request.form["rating"]
                        )
        db.session.add(new_book)
        db.session.commit()

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        new_book = Book(title=request.form["book"]
                        , author=request.form["author"]
                        , rating=request.form["rating"]
                        )
        db.session.add(new_book)
        db.session.commit()

    return render_template("edit.html")


if __name__ == "__main__":
    app.run(debug=True, port=8001)

