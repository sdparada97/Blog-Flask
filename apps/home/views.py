from flask import Blueprint, request, url_for, redirect, render_template, flash

bp_home = Blueprint('home', __name__, template_folder="../../templates/home")

@bp_home.route("/")
def home():
    return render_template('index.html')