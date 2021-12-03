# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:18:16 2021

@author: 1134677
"""

from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

@app.route("/index", methods=["POST"])
def index():
    if request.method == 'POST':
        try:
            response = request.get_json(force=True)
            print(f"\nresponse : {response}")
            name = response["name"]
            print(name)
            print(jsonify({'result':name, 'errorcode': "1",  'errormessage':""}))
            return jsonify({'result':name, 'errorcode': "1",  'errormessage':""})
        except Exception as e:
               print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")
               result=""
               return jsonify({'result':result, 'errorcode': "1",  'errormessage':"Error!"})
           
    #return "Hello user!"

if __name__ == "__main__":
    app.run(host=0.0.0.0, debug=True)
