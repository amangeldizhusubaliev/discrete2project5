
# NOT FINISHED YET
# Currently problem is in line  19
def dijkstra(g,n,src,dest,dist,path):
    q = [] # set<pair<int, int>> q; *******
    d = [-1] * n # vector<int> d(n, -1);
    p = [None] * n # vector<pair<int, int>> p(n);
    d[src] = 0
    p[src] = [src,0]
    q.append([d[src], src])
    while (q):
        v = q[0][1]
        q.remove(q[0])
        for i in g[v]:
            u = i[0]
            w = i[1]
            if d[u] == -1 or d[u] > d[v] + w:
                print (d[u],'/',u,' ')
                q.remove([d[u],u])
                d[u] = d[v] + w
                p[u] = [v,w]
                q.append[d[u],u]

                tem = list(set(q))
                tem.sort(key=q.index)
                q = tem
            
    dist = d[dest]
    if dist != -1:
        v = dest
        while v != src:
            path.append[ [p[v][0],v], p[v][1] ]
            v = p[v][0]
        path.reverse()
    return
    

n = 5
g = []
for i in range(0,n):
    g.append([])
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

src,dest,dist = 3, 0, 0
path = []
dijkstra(g,n,src,dest,dist,path)
if dist == -1:
    print('there is no any path from %d to %d\n' %(src + 1, dest + 1))
else:
    print('shortest path from %d to %d has a total weight %d and consists of %d edges.\n' %(src + 1, dest + 1, dist, len(path)) )
    for i in path :
        printt('%d %d %d\n'%(i[0][0] + 1, i[0][1] + 1, i[1]))

