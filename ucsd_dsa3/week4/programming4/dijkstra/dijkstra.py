#Uses python3
#this problem I use a smart heap, instead of change priority, I make the 
#old distance invalid by increasing counts 
#done

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    dist=dijkstra(adj,cost,s)
    if dist[t][0]!=100000:
        return dist[t][0]
    else:
        return -1 

def dijkstra(adj,cost,s):
    dist=[[100000,1] for i in range(len(adj))]                     #set distance to infinite,count to 1
    prev=[-1]*len(adj)                             #parents
    dist[s][0]=0                                   #first vertex
    pair=[]
    for i,j in enumerate(dist):
        pair.append((j[0],[i,j[1]]))              #the entry in heap has this properities (distance,[index,count])
    heapq.heapify(pair)                           #construct the heap

    while pair:
        want=False                                #not sure whether to pop the first one
                                                  #becaue it might be the old distance that we haven't deleted
        while not want:                           #if we don't need that
            x=heapq.heappop(pair)                 #(distance,[index,count])     pop first
            if x[1][1]==dist[x[1][0]][1]:         #if the count is the same, we need that node          
                want=True
            if pair==[]:                          #if the heap is already empty
                break                                
        if want==False:                          
            break
        u=x[1][0]                                 #the vertex we poped
        #now I get the right vertex to pop
        for i,j in enumerate(adj[u]):   #i is the index, j is the vertex it connected
            if dist[j][0]>dist[u][0]+cost[u][i]:       #cost[u][i] is the length between u and v
                dist[j][0]=dist[u][0]+cost[u][i]       #update distance
                dist[j][1]+=1                          #add the count
                prev[j]=u                              #add parents
                new_entry=(dist[j][0],[j,dist[j][1]])  #put new distance information
                heapq.heappush(pair,new_entry)         #put into the heap


    return dist




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
    s, t = data[0] - 1, data[1] - 1
    #print(adj)
    #print(cost)
    print(distance(adj, cost, s, t))
