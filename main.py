'''

1. Entre no Kaggle (https://www.kaggle.com/datasets) e encontre uma base de dados que
interesse:
a. Precisa ser em .csv;
b. Não pode ser muito grande (< 10Mb).
2. Carregue o .csv da base utilizando a biblioteca Pandas e aplique algumas operações
com a base:
a. Pelo menos um filtro de coluna;
b. Pelo menos duas operações de filtro;
c. Pelo menos duas operações de groupby.
d. Salvar os dados filtrados em um .csv novo.
3. Imprima gráficos dessa base (filtrada ou do groupby) utilizando a matplotlib.
a. Pelo menos 3 gráficos.

'''

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Lê o arquivo com as genéticas
portugues = pd.read_csv("portuguese.csv")
matematica = pd.read_csv("Maths.csv")

# a. Pelo menos um filtro de coluna;

# Exibe as colunas de escola, sexo e idade
print("Português: ")
print(portugues.loc[:, ['school', 'sex', 'age']], '\n')
print()
print("Matemática: ")
print(matematica.loc[:, ['school', 'sex', 'age']], '\n')

# b. Pelo menos duas operações de filtro;

# Exibe a nota final de alunos de portugues que não possuem internet
print("Notas Português S/ Internet\n")
alunos_port_s_internet = portugues.loc[portugues['internet'] == "no",
                                       ['school', 'sex', 'age', 'internet', 'G1', 'G2', 'G3']]
print(alunos_port_s_internet, '\n')

# Exibe as notas femininas na matemática
print("Notas Femininas na matemática\n")
notas_femininas_matematica = matematica.loc[matematica['sex'] == "F",
                                            ['school', 'age', 'sex', 'G1', 'G2', 'G3']]
print(notas_femininas_matematica, '\n')

# Exibe as notas masculinas na matemática
print("Notas Masculinas na matemática\n")
notas_masculinas_matematica = matematica.loc[matematica['sex'] == "M",
                                            ['school', 'age', 'sex', 'G1', 'G2', 'G3']]
print(notas_masculinas_matematica, '\n')

# c. Pelo menos duas operações de groupby.

# EXIBE AS MÉDIAS de notas agrupadas pelo sexo

# Exibe as médias masculinas e femininas em matemática
print("Médias em Matemática:\n")
media_matematica = matematica[['sex', 'G1', 'G2', 'G3']].groupby('sex').mean()
print(media_matematica)
print()

# Exibe as médias masculinas e femininas em português
print("Médias em Português:\n")
media_portugues = portugues[['sex', 'G1', 'G2', 'G3']].groupby('sex').mean()
print(media_portugues)
print()

# EXIBE AS MÉDIAS de notas agrupadas pelo acesso à internet

# Média em português
print("Média em Português de acordo com o acesso à internet\n")
medias_portugues_s_internet = portugues[['internet', 'G1', 'G2', 'G3']].groupby('internet').mean()
print(medias_portugues_s_internet, '\n')

# Média em matemática
print("Média em Matemática de acordo com o acesso à internet\n")
medias_matematica_s_internet = matematica[['internet', 'G1', 'G2', 'G3']].groupby('internet').mean()

print(medias_matematica_s_internet, '\n')

# d. Salvar os dados filtrados em um .csv novo.

# Registra a tabela em um arquivo csv

# media_matematica.to_csv("media_matematica.csv")

# media_portugues.to_csv("media_portugues.csv")


# 3 - a. Pelo menos 3 gráficos.

# Necessário para desenhar o gráfico
matplotlib.use('TkAgg')

# Grafico 1

# Compara as médias

lista_notas_femininas_matematica = notas_femininas_matematica['G3'].to_list()
print(lista_notas_femininas_matematica)

lista_notas_masculinas_matematica = notas_masculinas_matematica['G3'].to_list()
print(lista_notas_masculinas_matematica)

plt.plot(lista_notas_masculinas_matematica, lista_notas_femininas_matematica)

plt.show()



# Grafico 2

# Grafico 3






