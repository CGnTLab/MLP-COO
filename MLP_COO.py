##Date = 18-05-2022
##Developer = Aswathi Viswanathan

import joblib
import pandas as pd

model= joblib.load('MLP-COO.model.pkl')

## Independent dataset ##
df_ind = pd.read_csv('Example_input.csv')
del df_ind['Sample ID']
X_ind = df_ind
Y_predict_ind = model.predict(X_ind)

##Creating the output file ##
 
sample = pd.read_csv('Example_input.csv')
sam_column =  sample[['Sample ID']]
predicted_Class= pd.DataFrame(Y_predict_ind)
predicted_Class.loc[predicted_Class[0] == 0 , 0] = 'ABC'
predicted_Class.loc[predicted_Class[0] == 1 , 0] = 'GCB'
predicted_Class.rename(columns = {0:'Predicted COO'}, inplace = True)
sam_column.rename(columns = {'Samples':'Sample'}, inplace = True)
output_file = pd.concat([sam_column,predicted_Class],axis = 1)
output_file.to_csv('MLP-COO.output.txt', index=None, sep='\t')
