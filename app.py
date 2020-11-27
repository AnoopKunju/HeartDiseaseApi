import numpy as np
from flask import Flask, request,jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) #load model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    age=trestbps=chol=thalach=oldpeak=sex_0=sex_1=cp0=cp1=cp2=cp3=fbs0=fbs1=restecg0=restecg1=restecg2=exang0=exang1=slope0=slope1=slope2=ca0=ca1=ca2=ca3=ca4=thal0=thal1=thal2=thal3 = 0

    features_list = [age,trestbps,chol,thalach,oldpeak,sex_0,sex_1,cp0,cp1,cp2,cp3,fbs0,fbs1,restecg0,restecg1,restecg2,exang0,exang1,slope0,slope1,slope2,ca0,ca1,ca2,ca3,ca4,thal0,thal1,thal2,thal3]
    for f in features_list:
        f = 0

    try:
        age= float(request.args.get('Age'))
    except ValueError:
        return render_template('error.html')
    
    try:
        trestbps = float(request.args.get('trestbps'))
    except ValueError:
        return render_template('error.html')
    
    try:
        chol = float(request.args.get('chol'))
    except ValueError:
        return render_template('error.html')
    
    try:
        thalach = float(request.args.get('thalach'))
    except ValueError:
        return render_template('error.html')

    try:
        oldpeak = float(request.args.get('oldpeak'))
    except ValueError:
        return render_template('error.html')
  
    sex = request.args.get('sex')
    if sex == 'female':
        sex_0 = 1.
    else:
        sex_1 = 1.
    
    cp = request.args.get('cp')
    if cp == 'cp0':
        cp0 = 1.
    elif cp == 'cp1':
        cp1 = 1.
    elif cp == 'cp2':
        cp2 = 1.
    else:
        cp3 = 1.
    
    fbs = float(request.args.get('fbs'))
    if fbs > 120:
        fbs1 = 1.

    restecg = request.args.get('restecg')
    if restecg == 'restecg0':
        restecg0 = 1.
    elif restecg == 'restecg1':
        restecg1 = 1.
    else:
        restecg2 = 1.
    
    exang = request.args.get('exang')
    if exang == 'No':
        exang0 = 1.
    else:
        exang1 = 1.
    
    slope = request.args.get('slope')
    if slope == 'slope0':
        slope0 = 1.
    elif slope == 'slope1':
        slope1 = 1.
    else:
        slope2 = 1.
    
    ca = request.args.get('ca')
    if ca == 'ca1':
        ca0 = 1.
    elif ca == 'ca1':
        ca1 = 1.
    elif ca == 'ca2':
        ca2 = 1.
    elif ca == 'ca3':
        ca3 = 1.
    else:
        ca4 = 1

    thal = request.args.get('thal')
    if thal == 'thal1':
        thal0 = 1.
    elif thal == 'thal1':
        thal1 = 1.
    elif thal == 'thal2':
        thal2 = 1.
    else:
        thal3 = 1.

    features_list = [age,trestbps,chol,thalach,oldpeak,sex_0,sex_1,cp0,cp1,cp2,cp3,fbs0,fbs1,restecg0,restecg1,restecg2,exang0,exang1,slope0,slope1,slope2,ca0,ca1,ca2,ca3,ca4,thal0,thal1,thal2,thal3]
    features =[]
    for f in features_list:
        features.append(f)
    
    final_features = [np.array(features)] #add features here
    print(final_features)
    prediction = int(model.predict(final_features))
    # output = round(prediction)
    print(prediction)
    print("##################")
    if prediction == 1:
        text = "--> Condition of Heart at Risk and Chance of Heart Disease is high"
    else:
        text = "-->Condition of Heart is Healthy and Chance of Heart Disease is low"


    return render_template('index.html', prediction_text = text)

if __name__ == "__main__":
    app.run(debug=True)