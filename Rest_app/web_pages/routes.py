from flask import Blueprint

main = Blueprint('home', __name__)

@main.route('/')
def home_page():
    return 'Home page'