"""/*
 * @Author: Shawn Zhang 
 * @Date: 2019-11-29 18:47:35 
 * @Last Modified by:   Shawn Zhang 
 * @Last Modified time: 2019-11-29 18:47:35 
 */
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '<h3> hello world!</h3>'
    return html