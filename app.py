import re
from flask import Flask, request, render_template, redirect
import random
import string
import sqlite3 as sql

regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def order():
    select = str(request.form.get('combo_selector'))
    url = str(request.form.get('url'))
    qty = int(request.form.get('qty'))

    if not (re.match(regex, url) is not None):
        return render_template("index.html", error="Invalid URL")

    if qty < 1:
        return render_template("index.html", error="Quantity must be greater than 0")

    if qty > 1 and select == "free":
        return render_template("index.html", error="Free combo cannot be ordered in quantities greater than 1")

    if qty > 1 and select == "paid2":
        return render_template("index.html", error="Paid combo 2 cannot be ordered in quantities greater than 1")

    if select == "free":
        order_number = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                               for _ in range(20))
        with sql.connect("database.db") as con:
            cur = con.cursor()
            command = "INSERT INTO db (channel_url,combo,quantily,order_number) VALUES ('"+url+"', '" + \
                select+"','"+str(qty)+"','"+str(order_number)+"')"

            cur.execute(command)

            con.commit()

        return render_template("thank.html", order_number=order_number)

    return render_template("fix.html")


@app.route("/get_order")
def get_order():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM db")

        rows = cur.fetchall()

        print(rows)

        return str(rows)


if __name__ == '__main__':
    app.run()
