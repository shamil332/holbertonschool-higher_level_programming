#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        pass
    return data

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    if id_param:
        try:
            id_value = int(id_param)
            filtered = [item for item in data if item.get('id') == id_value]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid ID", products=[])

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

