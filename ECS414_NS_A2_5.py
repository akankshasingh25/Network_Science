import pandas as pd
import numpy as np
import networkx as nx
import collections

# read the CSV file into a pandas dataframe
df = pd.read_csv(r'C:\Users\akank\Dropbox\My PC (LAPTOP-NQ9H8NTJ)\Documents\Sem 8\NS\A2\dolphin_edges.csv')
print(df)

# determine the number of nodes in the graph
num_nodes = max(df['x'].max(), df['y'].max())

# create an empty adjacency matrix
adj_matrix = np.zeros((num_nodes, num_nodes))

# iterate over the edges in the dataframe and fill in the adjacency matrix
for index, row in df.iterrows():
    source = row['x']
    target = row['y']
    adj_matrix[source-1][target-1] = 1
    adj_matrix[target-1][source-1] = 1  # since the graph is undirected

# print the adjacency matrix
print(adj_matrix.shape)

# save adjacency matrix as Networkx Graph
data = pd.DataFrame(adj_matrix)
G = nx.from_pandas_adjacency(data)

# save Networkx Graph as dictionary of list (input to the function defined below)
graph = nx.to_dict_of_lists(G)
print(graph)

# function to compute the shortest paths from a given node to all other nodes using BFS
def bfs_shortest_paths(graph, start):
    queue = collections.deque([start])
    visited = set([start])
    distances = {start: 0}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[node] + 1
    return distances

# function to compute the closeness centrality of a node
def closeness_centrality_node(graph, node):
    distances = bfs_shortest_paths(graph, node)
    total_distance = sum(distances.values())
    num_nodes = len(distances) - 1  # exclude the starting node
    if num_nodes > 0:
        return (num_nodes) / total_distance
    else:
        return 0.0
    
# closeness centrality of all nodes in the graph
centrality = {}
for node in graph:
    centrality[node] = closeness_centrality_node(graph, node)

# results
for node, centrality in centrality.items():
    print(f"Node {node} has closeness centrality {centrality:.4f}")