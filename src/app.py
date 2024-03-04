import pandas as pd

from utils import db_connect
engine = db_connect()

# your code here
engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('/workspaces/machine-learning-python-template/data/raw/AB_NYC_2019.csv')
data.to_sql('2019-ABNB', engine, if_exists='replace', index=False)
