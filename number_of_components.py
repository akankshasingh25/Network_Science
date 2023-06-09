# Write a program to find the number of components in an undirected network.

# We solve this problem using Depth First Search.

# class Graph represents an undirected graph using adjacency list representation
class Graph:
	def __init__(self, V):
		# No. of nodes
		self.V = V
		# Pointer to an array containing adjacency lists
		self.adj = [[] for i in range(self.V)]

	# Function to return the number of components in an undirected graph
	def NumberofComponents(self):
		# Mark all the nodes as not visited
		visited = [False for i in range(self.V)]
		# To store the number of connected components
		count = 0
		for v in range(self.V):
			if (visited[v] == False):
				self.DFS(v, visited)
				count += 1
				
		return count
		
	def DFS(self, v, visited):
		# Mark the current node as visited
		visited[v] = True

		# Repeating for all the connected nodes to current node
		for i in self.adj[v]:
			if (not visited[i]):
				self.DFS(i, visited)

	# Making an undirected graph by adding edges for nodes	
	def Edge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)
		
# Driver code	
if __name__=='__main__':
	
	g1 = Graph(5)
	g1.Edge(1, 0)
	g1.Edge(1, 2)
	g1.Edge(2, 3)
	g1.Edge(3, 4)
	print(g1.NumberofComponents())

	g2 = Graph(9)
	g2.Edge(1, 0)
	g2.Edge(1, 2)
	g2.Edge(2, 3)
	g2.Edge(3, 0)
	g2.Edge(4, 5)
	g2.Edge(5, 6)
	g2.Edge(6, 4)
	g2.Edge(7, 8)
	print(g2.NumberofComponents())

	g3 = Graph(6)
	g3.Edge(1, 3)
	g3.Edge(2, 3)
	g3.Edge(0, 4)
	g3.Edge(5, 4)
	print(g3.NumberofComponents())

"""Output:
1
3
2
"""
