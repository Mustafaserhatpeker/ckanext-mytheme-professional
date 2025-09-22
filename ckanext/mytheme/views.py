from flask import Blueprint


mytheme = Blueprint(
    "mytheme", __name__)


def page():
    return "Hello, mytheme!"


mytheme.add_url_rule(
    "/mytheme/page", view_func=page)


def get_blueprints():
    return [mytheme]
