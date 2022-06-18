# Importing required packages
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

# Create flask application
app = Flask(__name__)


# Create home route
@app.route('/')
def index():
    logging.info('testing logging module')
    return 'welcome to project'


# Run flask application
if __name__ == '__main__':
    app.run()