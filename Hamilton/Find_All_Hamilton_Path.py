"""
hamitonian path:

undirected graph - visiting each vertex in the graph once without repetation


"""
class Graph:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adj = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 

def hamiton_path(graph, v, visited,path,n):
  # if visited all verticies, can add path to return result array
  if len(path) ==n: 
    res.append(path.copy())
    return 
  #else dfs visit all other unvisited nodes
  for w in graph.adj[v]:
    if visited[w]==False:
      visited[w]=True
      path.append(w)

      hamiton_path(graph, w, visited, path,n )

      visited[w] =False
      path.pop()    

if __name__ =='__main__':
  edges= [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  n =4

  graph=Graph(edges,n)
  res=[]
  path =[]
  for i in range(n):
    path =[i]
    visited=[False]*n
    visited[i]=True
    hamiton_path(graph, i, visited,path,n)
