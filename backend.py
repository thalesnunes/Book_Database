import sqlite3
from tkinter import *


def create_db():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert_db(text_box, title, author, year, isbn):

    item = (title, author, year, isbn)
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO books VALUES('{item[0]}', '{item[1]}', {item[2]}, {item[3]})")
    conn.commit()
    conn.close()
    text_box.delete(0, END)
    display_results(text_box, [item])


def update_db(title, author, year, isbn):

    item = (title, author, year, isbn)
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        f"UPDATE books SET author='{item[1]}', year={int(item[2])}, isbn={int(item[3])} WHERE title='{item[0]}'")
    conn.commit()
    conn.close()


def delete_db(title):

    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(f"DELETE FROM books WHERE title='{title}'")
    conn.commit()
    conn.close()


def view_all(text_box):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    items = cur.fetchall()
    conn.close()
    display_results(text_box, items)


def display_results(text_box, list_items):
    text_box.delete("0", END)
    list_items.sort()
    for item in list_items:
        text_box.insert(
            END, f'{item[0]} ({item[1]}), {item[2]}, ISBN: {item[3]}')


def search_db(text_box, title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM books WHERE title='{title}' OR author='{author}' OR year={year} OR isbn={isbn}")
    rows = cur.fetchall()
    conn.close()
    display_results(text_box, rows)
