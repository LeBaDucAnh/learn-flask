from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def check():
    return "Comming soon..."


if __name__ == '__main__':
    app.run()