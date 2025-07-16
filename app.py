import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Ambil port dari environment atau gunakan 5000 sebagai default
    app.run(host='0.0.0.0', port=port, debug=False)  # Gunakan host '0.0.0.0' untuk akses publik