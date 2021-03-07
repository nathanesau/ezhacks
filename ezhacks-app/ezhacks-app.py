from flask import Flask
import requests
from datetime import datetime
import os
import json

from dataprep.eda import plot

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
