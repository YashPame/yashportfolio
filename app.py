from flask import Flask, render_template
from Backlist import Projects, Contact, About
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', Projects=Projects, Contact=Contact, About=About)


if __name__ == '__main__':
    app.run(debug=True)
