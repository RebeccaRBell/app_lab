from flask import render_template
from app import app
from models.order_list import orders


@app.route("/")
def index():
    return render_template("index.html", orders=orders)


@app.route("/orders/<int:index>")
def order(index):
    return render_template("order.html", orders=orders[index])
