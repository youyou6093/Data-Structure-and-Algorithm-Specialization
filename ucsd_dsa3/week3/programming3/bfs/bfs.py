#Uses python3
#done
import sys
import queue

def distance(adj, s, t):
    dis=bst(adj,s)
    if dis[t]!=100000:
        return dis[t]
    else:
        return -1

def bst(adj,x):
    dis=[0]*len(adj)
    my_queue=[]
    for i in range(len(adj)):
        dis[i]=100000           #initialize the distance
    dis[x]=0
    my_queue.append(x)          #first points
    while my_queue:
        u=my_queue.pop(0)
        #my_queue=my_queue[1:]      #dequeue

        for i in adj[u]:           #the data points in u
            if dis[i]==100000:
                my_queue.append(i) 
                dis[i]=dis[u]+1
    return dis


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    #print(adj)
    print(distance(adj, s, t))
