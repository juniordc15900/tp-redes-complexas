import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Ler a tabela e selecionar apenas as colunas necessárias
df = pd.read_csv('data_diseases.csv', delimiter='\t')

# Criar um grafo direcionado
G = nx.DiGraph()

# Iterar sobre as linhas da tabela
for _, row in df.iterrows():
    row = row.values[0].split(',')
    doenca = row[4]
    sim = row[1]
    
    # Adicionar aresta entre doença e sim
    G.add_edge(doenca, 'Diabetes', weight=sim)

# Plotar o grafo
pos = nx.spring_layout(G, seed=42)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title('Rede de Relação entre Doenças e Sim (Diabetes)')
plt.axis('off')
plt.show()