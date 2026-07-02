#!/usr/bin/python3
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename='products.json'):
    with open(filename, 'r') as f:
        return json.load(f)


def read_csv(filename='products.csv'):
    products = []
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename='products.db'):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        }
        for row in rows
    ]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
   uery parameter. Optionally filter by 'id'.
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template(
                'product_display.html', error="Wrong source"
            )
    except sqlite3.Error:
        return render_template(
            'product_display.html', error="Error reading database"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template(
                'product_display.html', error="Product not found"
            )
        return render_template('product_display.html', products=filtered)

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
