import pandas as pd

pd.Series(data=5)
lista_nomes = "Howard Ian Peter Jonah Kellie".split()
pd.Series(lista_nomes)
dados = {

    'nome1': 'Howard',

    'nome2': 'Ian',

    'nome3': 'Peter',

    'nome4': 'Jonah',

    'nome5': 'Kellie',

}
pd.Series(dados)
cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
pd.Series(lista_nomes, index=cpfs)
series_dados = pd.Series(lista_nomes, index=cpfs)
series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print("Quantidade de linhas =", series_dados.shape)#retorna uma tupla com o n de linhas
print("Tipo de dados=", series_dados.dtypes)#retorna o tipo de dados, se for misto será object
print("Os valores são únicos?", series_dados.is_unique)#verifica se os valores são únicos, sem duplicações
print("Existem valores nulos?", series_dados.hasnans)#verifica se existem valores nulos
print("Quantos valores existem?", series_dados.count())#conta quantos valores existem (exclui os nulos)
print("Qual o menor valor?", series_dados.min())#extrai os menores valores das Series(precisam ser valores do mesmo tipo)
print("Qual o maior valor?", series_dados.max())#extrai os maiores valores, nas mesmas condições do min.
print("Qual a média aritmética?", series_dados.mean())#extrai a média aritmética de uma Series numérica.
print("Qual o desvio padrão?", series_dados.std())#extrai o desvio padrão de uma Series numérica.
print("\nResumo:\n", series_dados.describe())#exibe um resumo sobre os dados na Series


