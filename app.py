# importing required packages
from flask import Flask

# create flask application
app = Flask(__name__)


# create home route
@app.route('/')
def index():
    return 'welcome to project'


# run flask application
if __name__ == '__main__':
    app.run()
