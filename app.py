from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/konfiguracja')
def konfiguracja():
    if request.method == 'get':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')


        return redirect(url_for('index'))
    return render_template('konfiguracja.html')


@app.route('/analiza')
def analiza():
    return render_template('analiza.html')

if __name__ == '__main__':
    db.create_all()
    app.run()
