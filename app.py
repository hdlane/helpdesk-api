from flask import Flask, request
import os
import sqlite3


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
    data = []
    if request.method == "GET":
        with sqlite3.connect("computers.db") as computers:
            computers.row_factory = sqlite3.Row
            cursor = computers.cursor()
            query = cursor.execute("SELECT * FROM computers")
            res = query.fetchall()
        for item in res:
            data.append({
                "ComputerName": item["computer_name"],
                "UserName": item["user_name"],
                "IpAddress": item["ip_address"],
                "Os": item["os"],
                "Model": item["model"],
                "Drive": item["drive"],
                "Uptime": item["uptime"],
                "LastContact": item["last_contact"],
            })
        return data
    if request.method == "POST":
        data = request.get_json()
        print()
        if (
            "ComputerName" in data and
            "MacAddress" in data and
            "UserName" in data and
            "LastContact" in data and
            "IpAddress" in data and
            "Os" in data and
            "Model" in data and
            "Uptime" in data and
            "Drive" in data
        ):
            computer_name = data["ComputerName"]
            mac_address = data["MacAddress"]
            user_name = data["UserName"]
            last_contact = data["LastContact"]
            ip_address = data["IpAddress"]
            os = data["Os"]
            model = data["Model"]
            uptime = data["Uptime"]
            drive = data["Drive"]
            with sqlite3.connect("computers.db") as computers:
                cursor = computers.cursor()
                query = cursor.execute(f"""
                SELECT * FROM computers WHERE mac_address = '{mac_address}'
                """)
                res = query.fetchone()
                if res is None:
                    cursor.execute(f"""
                    INSERT INTO computers VALUES
                        ('{computer_name}', '{mac_address}',
                         '{user_name}', '{ip_address}', '{os}', '{model}', '{drive}',  '{uptime}',  '{last_contact}')
                    """)
                if res is not None:
                    cursor.execute(f"""
                    UPDATE computers
                    SET computer_name = '{computer_name}',
                        user_name = '{user_name}',
                        ip_address = '{ip_address}',
                        os = '{os}',
                        model = '{model}',
                        drive = '{drive}',
                        uptime = '{uptime}',
                        last_contact = '{last_contact}'
                    WHERE
                        mac_address = '{mac_address}'
                    """)
        return "OK", 200
    else:
        return "Invalid JSON", 400
