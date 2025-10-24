from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Cargar dataset
df = pd.read_csv("mi_dataset.csv")

# Subir a Elasticsearch
for i, row in df.iterrows():
    doc = row.to_dict()
    es.index(index="mi_indice", document=doc)

# Graficar distribución por producto
res = es.search(index="mi_indice", size=1000, query={"match_all": {}})
productos = [hit["_source"]["producto"] for hit in res['hits']['hits']]

plt.hist(productos)
plt.title("Distribución por producto")
plt.savefig("grafica.png")
