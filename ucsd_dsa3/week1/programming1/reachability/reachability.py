#Uses python3
#done

import sys

def reach(adj, x, y):
    visit=set([])
    dfs(adj,visit,x)
    if y in visit:
        return 1
    return 0

def dfs(adj,visit,x):
    visit.add(x)
    for i in adj[x]:           #all the edges
        if (i in visit)==0:    #hasn't be reached
            dfs(adj,visit,i)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(adj)
    print(reach(adj, x, y))
