from flask import render_template
from app import app

# Views
@app.route('/news/<int:news_id>')
def index():

    return render_template('index.html', title = title)