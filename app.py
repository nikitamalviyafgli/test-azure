import numpy as np, pandas as pd, import os, requests
from flask import Flask, render_template, request, jsonify

@app.route('/result', methods=['POST', 'GET'])
def main():
  if request.method == 'POST':
    return jsonify({"result":"success"})
