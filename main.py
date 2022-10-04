'''

About Dataset

Context
With the advent of Machine Learning algorithms, it is often to find their usage in a wide range of applications.
Nevertheless, such algorithms require a massive amount of data and several tasks still lake some properly described and
structured data. In such a context, this dataset aims at providing a unique source of cannabis-related information,
which have been directly scrapped from Leafly's website.

Content
The dataset is composed of the encoded data in .json and .csv formats, directly scrapped from Leafly's website. Additionally, it holds all meta-information that was possible to be extracted, as follows:

name;
image url;
type;
thc level;
most common terpene;
description;
positive effects;
negative effects; and
diseases it helps with.
Acknowledgements
If you use this dataset, we would be greatly thankful if you cite the following repository:

https://github.com/gugarosa/leaflyer

Inspiration
Fulfill the literature gap in cannabis-related data;
How to improve cannabis strain classification;
Do traditional classifiers are often sufficient to overcome such a task;
How the proposed task might benefit from more modern Computer Vision approaches.

'''

import pandas as pd

# Lê o arquivo com as genéticas
tabela_geneticas = pd.read_csv("leafly_strain_data.csv")

# Separa as geméticas da acordo com a espécie
sativas = tabela_geneticas.loc[tabela_geneticas["type"] == "Sativa"]
indicas = tabela_geneticas.loc[tabela_geneticas["type"] == "Indica"]
hibridas = tabela_geneticas.loc[tabela_geneticas["type"] == "Hybrid"]

# Separa as melhores genéticas indicas para insônia
print(sativas.describe())