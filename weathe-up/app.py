from flask import Flask,render_template
app = Flask(__name__)




import urllib.request
import json

url = 'https://api.covid19api.com/summary'

with urllib.request.urlopen(url) as response:
    data = response.read()
    y = json.loads(data)




@app.route('/')
def world():
    return render_template('index.html',data=y)


if __name__ == '__main__':
    app.run(debug=True)




























if __name__ == '__main__':
    app.run(debug=True)
