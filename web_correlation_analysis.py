import pandas as pd
import numpy as np

csv_files = ['web_ortho.csv', 'web_mem.csv', 'web_exec.csv', 'web_HL.csv', 'web_DT.csv', 'web_contemp.csv']
features = ['Orthogonality', 'Memory efficiency', 'Execution speed', 'High level', 'Dynamically typed', 'Contemporary features']


Map = {}
output_file = open("web_correlation_results.txt", "w")

for i in range(len(csv_files)):
    file_name = 'data/' + csv_files[i]
    data = pd.read_csv(file_name)
    feature = features[i]
    df = pd.DataFrame(data)
    Map[feature] = df.corr().iloc[0,1]

print('Correlation factors for Web Industry')
for feature in features:
    output = feature + ': ' +str(Map[feature])
    print(output)
    output_file.write(output+'\n')

output_file.close()

