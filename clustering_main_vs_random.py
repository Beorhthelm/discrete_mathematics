import networkx as nx
import numpy as np


# Reads data from the dataset, and creates graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# Shows the number of edges in G_fb
print("edges = " + str(G_fb.number_of_edges()))

# Shows number of nodes in G_fb
print("nodes = " + str(G_fb.number_of_nodes()))

# Computes a probability whether there is an edge between two vertices
edges = int(G_fb.number_of_edges())
nodes = int(G_fb.number_of_nodes())
edges_K = nodes * (nodes - 1) // 2
edge_probab = edges / edges_K
print(f'edge probability = {edge_probab}')

# Computes the ACC (average clustering coefficient) of G_fb
av_clust_coeff = nx.average_clustering(G_fb)
print(f'graph_acc = {av_clust_coeff}')


# Now let's generate a random graph. First let's initialize it
G_rand = nx.Graph()

# Generates edges in G_rand at random:
for i in range(nodes):
    for j in range(i):
        # Adds an edge between vertices i and j, with probability edge_probab (as in G_fb)
        generate_edge = np.random.choice([True, False], p=[edge_probab, 1 - edge_probab])
        if generate_edge:
            G_rand.add_edge(i, j)

# The above code is equivalent to the following stochastic graph generator function
# G_rand = nx.erdos_renyi_graph(nodes, edge_probab)

# The number of edges and the ACC of the new graph
print("rgraph_edges = " + str(G_rand.number_of_edges()))

rand_av_clust_coeff = nx.average_clustering(G_rand)

print("rgraph_acc = " + str(rand_av_clust_coeff))
