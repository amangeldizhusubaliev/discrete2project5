
from heapq import *

def dijkstra(g,n,src,dest,path):
    d = [-1] * n 
    p = [None] * n
    d[src] = 0
    p[src] = [src,0]
    q = [(0, src)]
    while (q):
        v = heappop(q)[1]
        for i in g[v]:
            u = i[0]
            w = i[1]
            if d[u] == -1 or d[u] > d[v] + w:
                d[u] = d[v] + w
                p[u] = [v,w]
                heappush(q, (d[u], u))
            
    dist = d[dest]
    if dist != -1:
        v = dest
        while v != src:
            path.append([[p[v][0],v], p[v][1]])
            v = p[v][0]
        path.reverse()
    return dist
    

n = 5
g = [[] for _ in range (0, n)]

g[0].append([1,2])
g[1].append([0,2])

g[0].append([2,2])
g[2].append([0,2])

g[0].append([3,7])
g[3].append([0,7])

g[1].append([2,1])
g[2].append([1,1])

g[1].append([3,3])
g[3].append([1,3])

g[1].append([4,3])
g[4].append([1,3])

g[2].append([4,1])
g[4].append([2,1])

src,dest = 3, 0
path = []
dist = dijkstra(g,n,src,dest,path)
if dist == -1:
    print('there is no any path from %d to %d' %(src + 1, dest + 1))
else:
    print('shortest path from %d to %d has a total weight %d and consists of %d edges:\n' %(src + 1, dest + 1, dist, len(path)) )
    for i in path :
        print('%d %d %d'%(i[0][0] + 1, i[0][1] + 1, i[1]))

