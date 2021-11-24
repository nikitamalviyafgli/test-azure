import numpy as np, pandas as pd, import os, requests
from flask import Flask, render_template, request, jsonify



app = Flask(__name__)
 
@app.route('/result', methods=['POST'])
def main():
  if request.method == 'POST':
   try:
    if 'file' not in request.files:
     return jsonify({"predict":"", "errorcode" : "1", 'errormessage':"File not selected!"})
    else:
     uploaded_file = request.files['file']
     return jsonify({"result":"success"})
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
