import pandas as pd
import numpy as np

csv_files = ['iot_ortho.csv', 'iot_mem.csv', 'iot_exec.csv', 'iot_HL.csv', 'iot_DT.csv', 'iot_contemp.csv']
features = ['Orthogonality', 'Memory efficiency', 'Execution speed', 'High level', 'Dynamically typed', 'Contemporary features']


Map = {}
output_file = open("iot_correlation_results.txt", "w")

for i in range(len(csv_files)):
    file_name = 'data/' + csv_files[i]
    data = pd.read_csv(file_name)
    feature = features[i]
    df = pd.DataFrame(data)
    Map[feature] = df.corr().iloc[0,1]

print('Correlation factors for IoT Industry')
for feature in features:
    output = feature + ': ' +str(Map[feature])
    print(output)
    output_file.write(output+'\n')

output_file.close()