from flask import Flask,render_template


'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
## WSGI Application
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<html><h1>Introduction!</h1><p>My name is Bibash Chaudhary.</p></html>'
@app.route("/greet")
def greet():
    return render_template('greet.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)