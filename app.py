import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle
import pandas as pd 
from preprocess import preprocess_input


app = Flask(__name__)
model = pickle.load(open('saved_rf.pkl','rb'))

@app.route('/') 
def home() :
    return render_template('index.html')

@app.route('/predict',methods=['POST'])


def predict() :

    ''''''

    #retreive the input data from the form
    input_features = request.form.to_dict()
    print(input_features)
    
    
    features = [float(feature) for feature in preprocess_input(input_features) ]

    features = np.array([features])

    output = model.predict_proba(features)[0]
    print(output)

    if  np.argmax(output) == 1 :
        return render_template('index.html',prediction_text='Campaign success {} %'.format(round(output[1]*100,2)))
    else :
        return render_template('index.html',prediction_text='Campaign failure {} %'.format(round(output[0]*100,2)))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=801)



