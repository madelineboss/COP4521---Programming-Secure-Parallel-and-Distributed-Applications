from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_nu():
    return 'Welcome'

@app.route('/user/<username>')
def user(username):
    return f'Hello {username}!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 50000)
    #visit http://127.0.0.1:50000 to see website