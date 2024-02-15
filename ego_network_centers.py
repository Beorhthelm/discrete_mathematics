import networkx as nx
import matplotlib.pyplot as plt


# Reads data from the dataset, and creates graph G
G = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
# Visualizes the graph
nx.draw(G, pos=nx.spring_layout(G), node_size=25, width=0.5)
plt.show()

# List of 'pseudocenters'
pseudocenters = [ "0", "107", "1684", "1912", "3437", "348", "612", "3980", "414", "686", "698" ]

# Finds one of the 'pseudocenters', which is actually not an ego network center
added_vertex = -1

for i in pseudocenters:
    G = nx.read_edgelist("facebook_combined.txt")
    G.remove_node(i)
    for j in list(G.nodes):
        degree = G.degree[j]
        if degree == 0:
            break
    else:   # only executes when there is no break in the inner loop
        added_vertex = i
        break
    continue

print(added_vertex)
