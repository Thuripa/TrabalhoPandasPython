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

# Lê o arquivo com as genéticas
tabela_geneticas = pd.read_csv("leafly_strain_data.csv")

#pd.set_option('max_colwidth', 10)

# a. Pelo menos um filtro de coluna;
# Separa as genéticas da acordo com a coluna espécie (type)
sativas = tabela_geneticas.loc[tabela_geneticas["type"] == "Sativa"]
indicas = tabela_geneticas.loc[tabela_geneticas["type"] == "Indica"]
hibridas = tabela_geneticas.loc[tabela_geneticas["type"] == "Hybrid"]

# b. Pelo menos duas operações de filtro;
# Separa as genéticas indicas com eficácia no tratamento da depressão
#indicas_depressao = indicas.loc[indicas['depression'] != "0%",
                                         #['name', 'type', 'depression', 'thc_level']]
#print(indicas_depressao)

# Separa as genéticas com eficácia no tratamento do câncer
#geneticas_cancer = tabela_geneticas.loc[tabela_geneticas['cancer'] != "0%", ['name', 'type', 'cancer', 'thc_level']]
#print(geneticas_cancer)


# Registra a tabela em um arquivo csv
#indicas_depressao.to_csv("geneticas_depressao.csv")


# group by
grupopor = tabela_geneticas.groupby('name').sum()
print(grupopor)

# Separa as genéticas indicas com efeito calmante e que não causam sono






