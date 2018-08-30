#Uses python3
#done
import sys




def dfs(adj, pre, post, x):
    #write your code here
    global clock
    clock+=1
    pre[x]=clock
    for i in adj[x]:
        if pre[i]==0:
            dfs(adj,pre,post,i)
    clock+=1
    post[x]=clock
    


def toposort(adj):
    pre = [0] * len(adj)
    post = [0] * len(adj)
    for i in range(len(adj)):
        if(post[i]==0):

            dfs(adj,pre,post,i)
    #print(pre,post)
    return post

if __name__ == '__main__':
    global clock
    clock=0
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    post = toposort(adj)
    post=[(i[0]+1,i[1]) for i in enumerate(post)]
    post=sorted(post,reverse=True,key=lambda x:x[1])
    #print (post)
    for x in post:
        print(x[0], end=" ")

