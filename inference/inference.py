# Hicimos un contenedor que tiene un modelo de machine learning 
# podemos hacer predicciones sobre ese modelo a traves de un endpoint 
# que probamos con POSTMAN 

import pickle

from flask import Flask, request, jsonify 

app = Flask(__name__) # definicion de la app

with open('logistic_model.pkl', 'rb') as f:
    logistic_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/predict', methods=['GET'])
def predict ():
    print("entre al predict")
    if request.method == 'GET':
        prediction = None
        data= request.json
        x = data.get("features",[])
        if len(x) !=0:
            scaler_x = scaler.transform(x)
            prediction = logistic_model.predict(scaler_x)
            prediction = prediction.tolist()
    return jsonify(prediction)   

if __name__=='__main__':
    app.run(debug=True, host= '0.0.0.0', port='5001') # pongo el servidor dentro de la red que es parte de mi host