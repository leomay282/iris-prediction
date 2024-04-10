import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    result = ""
    if request.method == 'POST':
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
        input3 = request.form.get('input3')
        input4 = request.form.get('input4')

        json_request = {
            "features": [[input1, input2, input3, input4]]
        }

        response = requests.get(url="inference_dock:5001", json=json_request)

        result = f"Flower Class: {response.json()}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5002)