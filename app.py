from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
 
@app.route('/index', methods=['POST'])
def main():
    rtext = "dummy"
    if request.method == 'POST':
        try:
            response = request.get_json(force=True)
            print("\n\nresponse : ", response)
            rtext = response['test']
        except Exception as E:
            print(E)
    return jsonify({"result": rtext})
   
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(host='0.0.0.0', port=8000,debug=True)
