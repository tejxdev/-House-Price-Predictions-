from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract 5 features from the form
        rm = float(request.form['RM'])
        age = float(request.form['AGE'])
        dis = float(request.form['DIS'])
        tax = float(request.form['TAX'])
        ptratio = float(request.form['PTRATIO'])
        
        # Default values for other features
        crim = 0.5
        zn = 0
        indus = 10
        chas = 0
        nox = 0.5
        rad = 5
        b = 350
        lstat = 10
        
        # Full feature list in correct order
        features = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]
        
        prediction = model.predict([features])
        return render_template('index.html', prediction_text=f'🏠 Predicted Price: ${prediction[0]:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
