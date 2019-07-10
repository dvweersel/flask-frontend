from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():

    model = {'api_url': 'http://localhost:5555/'}
    return render_template('main/home.html', **model)
