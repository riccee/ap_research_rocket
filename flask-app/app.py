#!/usr/bin/python3

import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def launch():
    return render_template('index.html')
