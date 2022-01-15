##grpah coloring - vertex coloring - minimal number of colors use

#find a way of coloring graph's vertices such that no two adjcent vertices share the same color.

class Graph:
  def __init__(self, n, edges):
    self.n =n 
    self.adj={i: [] for i in range(n)}
    for s, d in edges:
      self.addEdge(s,d)
  def addEdge(self,s,d):
    self.adj[s].append(d)
    self.adj[d].append(s)
def color_graph(graph):
  #use hashmap to store which color assigned to a vertex
  d= {}
  #loop through each vertex
  for i in range(graph.n):
    # if i's adj vertices has been colors, find a set of these colors
    assigned=set()
    for j in graph.adj[i]:
      if j in d:
        assigned.add(d[j])
    #find minimum unassigned color for vertex-i to avoid duplicates with its adjacent
    color =1
    
    for c in assigned:
      if c!=color:
        break
      color+=1
    d[i]=color
  return d

if __name__=='__main__':
  edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
  n =6 
  graph =Graph(n,edges)
  colors_map =color_graph(graph)
