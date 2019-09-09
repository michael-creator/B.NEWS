from flask import render_template,request, redirect , url_for
from ..request import get_news
from . import main

# Views
@main.route('/')
def index():

    output = get_news()

    return render_template('index.html', name = output)

@main.route('/news/sources')
def sources():

    output = get_news()