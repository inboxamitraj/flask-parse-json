import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/users')
def user_list():
    # r = requests.get('https://api.github.com/user', auth=('<YourUserName>', '<YourToken>'))
    user_list_request = requests.get('https://reqres.in/api/users?page=1')
    user_list_data = user_list_request.json()
    print(user_list_data)
    return render_template("app.html", rows=user_list_data)


@app.route('/')
def sg_time():
    sg_time_request = requests.get('http://worldtimeapi.org/api/timezone/Asia/Singapore')
    sg_time_data = sg_time_request.json()
    print(sg_time_data)
    return render_template("sg_time.html", rows=sg_time_data)


if __name__ == '__main__':
    app.run(debug=True)
