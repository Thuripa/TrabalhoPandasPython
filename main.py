import pandas as pd

# 1 - Carrega uma base de dados pré selecionada
planetas = pd.read_csv("planets.csv")

# 2 - Operações com a base

# a. Pelo menos um filtro de coluna;

# Pega os dados da terra
terra = planetas[planetas["Planet"] == "Earth"]

# Exibe os dados da terra
#print(terra)


# b. Pelo menos duas operações de filtro;

# Exibe os planetas cuja distância do sol seja maior do que 1 bilhão de km
#planetas_distantes = planetas[planetas["Distance from Sun (10^6 km)"] > 1000]

#print(planetas_distantes)


# Exibe os planetas maiores em tamanho do que a terra, porém menores em massa

# Pega os planetas maiores que a terra
planetas_maiores = planetas[planetas["Diameter (km)"] > 12756]
#print(planetas_maiores)


# Pega os planetas menores em masas
planetas_maiores_e_mais_leves = planetas_maiores[planetas_maiores["Density (kg/m^3)"] < 5514]
print(planetas_maiores_e_mais_leves)

# c. Pelo menos duas operações de groupby.



# d. Salvar os dados filtrados em um .csv novo.
