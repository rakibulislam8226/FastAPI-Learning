from flask import Blueprint, render_template

second = Blueprint("second", __name__, template_folder="templates")


@second.route("/second")
@second.route("/")
def second_home():
    return "Hello from second"
