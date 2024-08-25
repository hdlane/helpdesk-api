import os
import sqlite3

from flask import Flask, request
from model import Model


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app


def init_db():
    if not os.path.isfile("computers.db"):
        connection = sqlite3.connect("computers.db")
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE computers(
            computer_name TEXT NOT NULL,
            mac_address TEXT NOT NULL UNIQUE,
            user_name TEXT,
            ip_address TEXT NOT NULL,
            os TEXT,
            model TEXT,
            drive TEXT,
            uptime TEXT,
            last_contact TEXT);
        """)
    with sqlite3.connect("computers.db") as computers:
        cursor = computers.cursor()
        query = cursor.execute("""
        SELECT EXISTS (
            SELECT name
            FROM sqlite_schema
            WHERE type='table' AND
            name='computers'
        )
        """)
        if (query.fetchone()[0] == 0):
            cursor.execute("""
            CREATE TABLE computers(
                computer_name TEXT NOT NULL,
                mac_address TEXT NOT NULL UNIQUE,
                user_name TEXT,
                ip_address TEXT NOT NULL,
                os TEXT,
                model TEXT,
                drive TEXT,
                uptime TEXT,
                last_contact TEXT);
            """)


app = create_app()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        model = Model()
        data = model.get_computers()
        return data
    if request.method == "POST":
        model = Model()
        data = request.get_json()
        if model.add_computer(data):
            return "OK", 200
        else:
            return "Invalid JSON", 400
