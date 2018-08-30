#Uses python3
#done
import sys




def acyclic(adj):
    visit=set([])
    post=set([])
    cycle=[]
    for i in range(len(adj)):
        if (i in post)==0:     #vertex
            dfs(adj,visit,post,i,cycle)
            #print(cycle)
            if cycle:
                #print(cycle)
                return 1
    return 0

def dfs(adj,visit,post,x,cycle):
    visit.add(x)
    for i in adj[x]:      #all neighbors of x
        #print(x,i,post,visit)
        if(i in visit):   
            if (i in post)==0:   #this means cycle 
                 
                cycle.append(i)
                
        if(i in visit)==0:
            dfs(adj,visit,post,i,cycle)
    post.add(x)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
