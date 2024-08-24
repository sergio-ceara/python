import pandas as pd
from datetime import date
from IPython.display import display
import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pd.Series(data=0)
lista_nome = 'Paulo Sérgio Ferreira de Sousa'.split()

dfs = pd.Series(lista_nome) # Cria uma Series com um dicionário
data_extracao = date.today()
dfs['data_extracao'] = data_extracao
print(dfs.info())
print(dfs.head())
print("lista com print:\n",dfs)
display("lista com display:\n",dfs)
