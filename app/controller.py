from flask import render_template
from app import app
from app.models.event_list import events

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/info')
def info():
    return render_template('info.html', title="Info", events=events)