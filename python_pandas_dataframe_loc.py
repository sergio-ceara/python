import pandas as pd
import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
lista_nome = 'Paulo Sérgio Ferreira de Sousa'.split()
dfs = pd.DataFrame(lista_nome, columns=['nome']) # Cria uma Series com um dicionário
dfs['idade'] = 50
nova_linha = pd.DataFrame({'nome':['Ruthe'],'idade':[40]})
#dfs=pd.concat([dfs, nova_linha], ignore_index=False) # com false irá acrecentar no indice 0 mesmo que exista.xi
dfs=pd.concat([dfs, nova_linha], ignore_index=True) # com true irá acrecentar no próximo indice, nesta caso será 5.

print("Lista inteira:\n",dfs)
print("Lista idades menor igual a 40:",dfs.loc[(dfs['idade']<=40)])
print("Lista idades maior que 40:",dfs.loc[(dfs['idade']>40)])