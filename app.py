# Importing required packages
from flask import Flask

# Create flask application
app = Flask(__name__)


# Create home route
@app.route('/')
def index():
    return 'welcome to project'


# Run flask application
if __name__ == '__main__':
    app.run()