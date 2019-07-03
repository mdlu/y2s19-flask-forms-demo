from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return 'You just made a GET request!'
    else:
        return 'You just made a POST request!'

app.run(debug=True)
