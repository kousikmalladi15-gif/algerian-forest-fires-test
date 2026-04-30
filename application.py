import pickle
from flask import Flask, request, render_template

application = Flask(__name__)
app = application

net_model = pickle.load(open('models/net-cv.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        region_map = {"Bejaia": 0, "Sidi-Bel": 1}
        class_map = {"not fire": 0, "fire": 1}
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = class_map.get(request.form.get('Classes'))
        Region = region_map.get(request.form.get('Region'))


        data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        pred = net_model.predict(data)
        

        return render_template('index.html', result=round(pred[0], 2))
    
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)