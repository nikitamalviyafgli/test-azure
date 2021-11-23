import numpy as np, pandas as pd, import os, requests
from flask import Flask, render_template, request, jsonify

@app.route('/result', methods=['POST', 'GET'])
def main():
  return jsonify({"result":"success"})
