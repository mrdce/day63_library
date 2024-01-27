# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# cursor.execute('''
# CREATE TABLE books
# (id INTEGER PRIMARY KEY
# , title varchar(250) NOT NULL UNIQUE
# , author varchar(250) NOT NULL
# , rating FLOAT NOT NULL)''')
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

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
        return f'<{self.title} - {self.author} - {self.rating}>'

# with app.app_context():
#     db.create_all()

# new_book = Book(id=1, title="Harry Potter", author="Joanne Rowling", rating=9.3)
with app.app_context():
    all_books = db.session.query(Book).all()
    print(all_books)
    # new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()
