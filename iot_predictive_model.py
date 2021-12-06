import pandas as pd
import numpy as np
from sklearn import linear_model


file_name = 'data/' + 'predictive_iot.csv'
data = pd.read_csv(file_name)
df = pd.DataFrame(data)
features = ['Ortho','Contem','DT','HL','Exec','Mem','n-6','n-5','n-4','n-3','n-2','n-1']
languages = ['Java', 'Python','JavaScript','C','C++']
X = df[features]
Y = df['n']
regr = linear_model.LinearRegression()
regr.fit(X,Y)

output_file = open("iot_prediction_results.txt", "w")

for index in df.index:
    X_pred = [df['Ortho'][index],df['Contem'][index],df['DT'][index],df['HL'][index],df['Exec'][index],df['Mem'][index],df['n-5'][index],df['n-4'][index],df['n-3'][index],df['n-2'][index],df['n-1'][index],df['n'][index]]
    predicted = regr.predict([X_pred])
    output = languages[index]
    output = output +': '+str(predicted[0])
    output_file.write(output+'\n')

output_file.close()


