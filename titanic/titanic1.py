import pandas as pd  # Importa a biblioteca pandas

# Caminho para o arquivo CSV
caminho_arquivo = 'train.csv'

# Carregar o dataset a partir do arquivo CSV
titanic = pd.read_csv(caminho_arquivo)

# Exibir as primeiras linhas do dataset
#print("Primeiras linhas do dataset:")
#print(titanic.head())

# Exibir informações gerais sobre o dataset
print("\nInformações do dataset:")
print(titanic.info())

# Exibir estatísticas descritivas do dataset
#print("\nEstatísticas descritivas:")
#print(titanic.describe(include='all'))

# Filtrar passageiros com idade menor de 18 anos
pessoas_de_18 = titanic[titanic['Age'] < 18]
pessoas_18_50 = titanic[(titanic['Age'] >= 18) & (titanic['Age'] <= 50)]
pessoas_de_50 = titanic[titanic['Age'] > 50]

# Contar o número de passageiros com idade menor de 18 anos
quantidade_pessoas_de_18 = pessoas_de_18.shape[0]
print("passageros com idade menor que 18 anos:",quantidade_pessoas_de_18)

quantidade_pessoas_18_50 = pessoas_18_50.shape[0]
print("passageros com idade entre 18 e 50 anos:",quantidade_pessoas_18_50)

quantidade_pessoas_de_50 = pessoas_de_50.shape[0]
print("passageros com idade acima de 50 anos:",quantidade_pessoas_de_50)

print("total:",titanic.count())
