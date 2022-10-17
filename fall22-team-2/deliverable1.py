import matplotlib as plt
import numpy as np
import pandas as pd

data_set = pd.read_csv("fy2022pa-4.csv")
print(data_set)
# remove columns for confined data set
data_set = data_set.drop(columns=['CORNER_UNIT','PROP_VIEW','ORIENTATION','FIRE_PLACE','KITCHEN_STYLE3',
            'KITCHEN_STYLE2','KITCHEN_STYLE1','BTHRM_STYLE3','BTHRM_STYLE2','BTHRM_STYLE1'])
print(data_set)
# remove rows where column LU(Land use) equals condon parking(CP), Industrial(I), Exempt(E), Exempt(Chapter 1) (EA)
data_set.drop(data_set[data_set['LU'] == 'CP'].index, inplace=True)
data_set.drop(data_set[data_set['LU'] == 'I'].index, inplace=True)
data_set.drop(data_set[data_set['LU'] == 'E'].index, inplace=True)
data_set.drop(data_set[data_set['LU'] == 'EA'].index, inplace=True)
print(data_set)