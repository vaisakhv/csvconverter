from glob import glob
import pandas as pd
import os

path = os.getcwd()
first = True
for file in glob(path+'\\files\\*.txt'):
    file_name = file.split('\\')[-1].split('.')[0]
    df = pd.read_csv(file, header=None)
    try:
        os.mkdir(path+'\\out\\')
        df.to_excel(path + '\\out\\' + file_name + '.xlsx')
    except FileExistsError:
        df.to_excel(path+'\\out\\'+file_name + '.xlsx', index=False, header=False)
