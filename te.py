from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
       # render your html template
       return render_template('w1.html')

@app.route('/something')
def do_something():
       # when the button was clicked, 
       # the code below will be execute.
       print 'do something here'


if __name__ == '__main__':
       app.run()
