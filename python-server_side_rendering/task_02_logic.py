#!/usr/bin/python3
"""
Module task_02_logic

A Flask application that dynamically renders a list of items read
from a JSON file, using Jinja's loop and conditional constructs.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Read the list of items from items.json and render them
    dynamically in items.html.
    """
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
