# app.py
from flask import Flask, request, render_template
import json
from model import analyze_financial_data

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        file = request.files['datafile']
        data = json.load(file.stream)  # Load JSON data from the uploaded file
        results = analyze_financial_data(data)
        return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
