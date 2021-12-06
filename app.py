import requests
from flask import Flask, render_template

# r = requests.get('https://api.github.com/user', auth=('<YourUserName>', '<YourToken>'))
r = requests.get('https://reqres.in/api/users?page=1')

data = r.json()
print(data)
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("app.html", rows=data)


if __name__ == '__main__':
    app.run(debug=True)
