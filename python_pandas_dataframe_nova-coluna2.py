import pandas as pd
from datetime import date
from IPython.display import display
import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pd.Series(data=0)
lista_nome = 'Paulo Sérgio Ferreira de Sousa'.split()

dfs = pd.DataFrame(lista_nome, columns=['nome']) # Cria uma Series com um dicionário
data_extracao = date.today()
dfs['data_extracao'] = data_extracao
dfs['data_extracao'] = dfs['data_extracao'].astype('datetime64[ns]')
#print("DataFrame.info():\n",dfs.info())
#print("DataFrame.head():\n",dfs.head())
print("DataFrame  sem ordem:",dfs)
dfs.sort_values(by='nome', ascending=True, inplace=True)
print("DataFrame  ordem nome crescente:",dfs)
dfs.sort_values(by='nome', ascending=False, inplace=True)
print("DataFrame  ordem nome decrescente:",dfs)