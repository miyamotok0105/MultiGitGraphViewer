# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask
from flask import Flask, render_template, Response
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
import jsonify

app = Flask(__name__)
# AppConfig(app)
# Bootstrap(app) 
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# app = Blueprint("data", __name__,
#     static_url_path='/data', static_folder='./data'
# )

@app.route('/')
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/season1.csv")
def getSession1Csv():
    with open("static/data/season1.csv") as fp:
        csv = fp.read()
    # csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=season1.csv"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True, threaded=False)


