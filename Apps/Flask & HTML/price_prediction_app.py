from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
fit_model=pickle.load(open('/Users/jaswanthsai/Documents/DATA 606/EDA/Final Gradient Boost Model.pkl','rb'))
car=pd.read_csv('/Users/jaswanthsai/Documents/DATA 606/EDA/eda_dataset.csv')
br = car['brand']
md = car['model']
ls = {}
for i in range(0, len(md)):
    ls[md[i]] = br[i]
print(ls)


@app.route('/',methods=['GET','POST'])
def index():
    brand = sorted(car['brand'].unique())
    model = sorted(car['model'].unique())
    finallist = ls
    car_age = sorted(car['car_age'].unique())
    mileage = car['mileage']
    fuel_type = car['fuel_type'].unique()
    drive_type = car['drive_type'].unique()
    accidents = sorted(car['accidents'].unique())
    owners = sorted(car['owners'].unique())
    MPG = car['MPG'].unique()




    return render_template('index.html', brand=brand, model=model, car_age=car_age, mileage=mileage,
                           fuel_type=fuel_type, drive_type = drive_type, finallist = finallist, accidents = accidents,
                           owners = owners, MPG = MPG, )

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    brand=request.form.get('brand')
    model=request.form.get('model')
    car_age=int(request.form.get('car_age'))
    mileage = int(request.form.get('mileage'))
    fuel_type=request.form.get('fuel_type')
    drive_type = request.form.get('drive_type')

    # transmission = request.form.get('transmission')
    accidents = request.form.get('accidents')
    owners = request.form.get('owners')
    MPG = request.form.get('MPG')



    prediction=fit_model.predict(pd.DataFrame(columns=[ 'brand', 'model','mileage','fuel_type',
                                                        'drive_type','accidents','owners','MPG','car_age'],
                              data=np.array([brand,model,mileage,fuel_type,drive_type,
                                             accidents,owners,MPG,car_age]).reshape(1, 9)))

    prediction1 = np.exp(prediction)
    return str(int(np.round(prediction1[0],2)))

if __name__ == '__main__':
    app.run(debug=True)