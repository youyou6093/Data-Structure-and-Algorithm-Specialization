#Uses python3
#done

import sys


def negative_cycle(adj, cost):
    
    return int(bf(adj,cost))

def relax(adj,cost,dist,prev,u):
    relaxed=False
    for i,j in enumerate(adj[u]):
        if dist[j]>dist[u]+cost[u][i]:
            relaxed=True
            dist[j]=dist[u]+cost[u][i]
            prev[j]=u
    return relaxed




def bf(adj,cost):
    dist=[100000 for i in range(len(adj))]
    prev=[-1]*len(adj)
    dist[0]=0
    for i in range(len(adj)-1):
        for j in range(len(adj)):
            relax(adj,cost,dist,prev,j)
    # print(dist)
    for j in range(len(adj)):
        if (relax(adj,cost,dist,prev,j)==1):
            return 1
    return 0





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    #print(adj)
    print(negative_cycle(adj, cost))
