#Uses python3
import sys
import math
import heapq

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
        print "pop=%d" %u
        #now I get the right vertex to pop
        for i,j in enumerate(adj[u]):   #i is the index, j is the vertex it connected
            if dist[j][0]>dist[u][0]+cost[u][i]:       #cost[u][i] is the length between u and v
                dist[j][0]=dist[u][0]+cost[u][i]       #update distance
                dist[j][1]+=1                          #add the count
                prev[j]=u                              #add parents
                new_entry=(dist[j][0],[j,dist[j][1]])  #put new distance information
                heapq.heappush(pair,new_entry)         #put into the heap


    return dist,prev




def minimum_distance(x, y):
    adj=[]
    cost=[]
    for i in range(len(x)):
        adj.append([j for j in range(len(x)) if j!=i])
        cost.append([((x[j]-x[i])**2+(y[j]-y[i])**2)**0.5 for j in range(len(x)) if j!=i])
    #print adj,cost
    dist,prev=dijkstra(adj,cost,2)
    result=0
    for i in dist:
        result+=i[0]
    print prev
    print dist
    return result
    





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    #print(x,y)
    print("{0:.9f}".format(minimum_distance(x, y)))
