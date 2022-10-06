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
# Exibe um grafico de barras mostrando as médias masculinas e femininas em matemática

# Junta as 3 médias femininas numa única lista
lista_medias_fem_matematica = matematica.loc[matematica['sex'] == 'F', ['G1', 'G2', 'G3']]\
    .mean().values.tolist()

# Junta as 3 médias masculinas numa única lista
lista_medias_mas_matematica = matematica.loc[matematica['sex'] == 'M', ['G1', 'G2', 'G3']]\
    .mean().values.tolist()

# Define o eixo x
eixo_x = ['Média 1', 'Média 2', 'Média 3']
x = np.arange(len(eixo_x))
width = 0.35

# Cria Subgráficos Masculino e Feminino
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, lista_medias_fem_matematica, width, label='Feminino')
rects2 = ax.bar(x + width/2, lista_medias_mas_matematica, width, label='Masculino')

# Adiciona rótulos
ax.set_ylabel('Nota')
ax.set_title('Feminino x Masculino - Matemática')
ax.set_xticks(x, eixo_x)
ax.legend()

# Plota os valores no gráfico
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()


# Grafico 2
# Exibe um grafico de barras mostrando as médias masculinas e femininas em português

# Junta as 3 médias femininas numa única lista
lista_medias_fem_portugues = portugues.loc[portugues['sex'] == 'F', ['G1', 'G2', 'G3']]\
    .mean().values.tolist()

# Junta as 3 médias masculinas numa única lista
lista_medias_mas_portugues = portugues.loc[portugues['sex'] == 'M', ['G1', 'G2', 'G3']]\
    .mean().values.tolist()

# Define o eixo x
eixo_x = ['Média 1', 'Média 2', 'Média 3']
x = np.arange(len(eixo_x))
width = 0.35

# Cria Subgráficos Masculino e Feminino
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, lista_medias_fem_portugues, width, label='Feminino')
rects2 = ax.bar(x + width/2, lista_medias_mas_portugues, width, label='Masculino')

# Adiciona rótulos
ax.set_ylabel('Nota')
ax.set_title('Feminino x Masculino - Português')
ax.set_xticks(x, eixo_x)
ax.legend()

# Plota os valores no gráfico
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

# Grafico 3
# Resultado Geral Feminino x Masculino

# Soma as notas de matemática e português
resultado_feminino = lista_medias_fem_matematica + lista_medias_fem_portugues
resultado_masculino = lista_medias_mas_matematica + lista_medias_mas_portugues

# Extrai a média de notas
media_feminina = sum(resultado_feminino) / len(resultado_feminino)
media_masculina = sum(resultado_masculino) / len(resultado_masculino)

# Define o eixo x
eixo_x = ['Média Feminina', 'Média Masculina']
x = np.arange(len(eixo_x))
width = 0.35

# Cria Subgráficos Masculino e Feminino
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, media_feminina, width, label='Feminino')
rects2 = ax.bar(x + width/2, media_masculina, width, label='Masculino')

# Adiciona rótulos
ax.set_ylabel('Nota')
ax.set_title('Feminino x Masculino - Geral')
ax.set_xticks(x, eixo_x)
ax.legend()

# Plota os valores no gráfico
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()






