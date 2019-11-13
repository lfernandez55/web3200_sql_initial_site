from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact_page')
def contact():
    return render_template('contact.html')

@app.route('/seedDB')
def seedDB():
        return 'stub'

@app.route('/erase_DB')
def eraseDB():
        return 'stub'

@app.route('/all_books')
def all_books():
        return 'stub'

@app.route('/add_book', methods={'GET','POST'})
def addbook():
        return 'stub'
