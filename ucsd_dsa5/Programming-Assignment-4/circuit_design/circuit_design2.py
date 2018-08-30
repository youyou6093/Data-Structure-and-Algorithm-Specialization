# python3
import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

def trans(x):
    if x>0:
        return x-1
    if x<0:
        return -x+n-1

def trans_back(x):
    if x>=n:
        return -(x+1-n)
    else:
        return x+1


class edge:
    def __init__(self,from_,to_):
        self.from_=from_
        self.to_=to_
        
class graph:
    def __init__(self,vertexs):
        self.vertexs=[set([]) for i in vertexs]
        
    def add_edge(self,edge):
        self.vertexs[trans(edge.from_)].add(trans(edge.to_))  #add a new edge
            
    def DFS(self):
        self.clock=0
        self.pre=[0 for i in range(2*n)]
        self.post=[0 for i in range(2*n)]
        for i in range(2*n):
            if (self.post[i]==0):
                self.dfs(i)      #dfs this vertex
    
    def dfs(self,x):
        self.clock+=1
        self.pre[x]=self.clock
        for i in self.vertexs[x]:   #all the neighbors
            if self.pre[i]==0:   #haven't visit this vertex
                self.dfs(i)
        self.clock+=1
        self.post[x]=self.clock
                
                
    def reset_clock(self):
        self.clock=0
        self.pre=[0 for i in range(2*n)]
        self.post=[0 for i in range(2*n)]
            
    def scc(self,x,scc_list):
        scc_list.append(x)
        self.clock+=1
        self.pre[x]=self.clock
        for i in self.vertexs[x]:   #all the neighbors
            if self.pre[i]==0:   #haven't visit this vertex
                self.scc(i,scc_list)
        self.clock+=1
        self.post[x]=self.clock

def valid_or_not(all_scc):
    for i in all_scc:
        for j in i:
            if -j in i:
                return  False
    return True

def main():                
    global n   
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    edge_list_normal=[]
    edge_list_reverse=[]
    for i in clauses:
        edge_list_normal.append(edge(-i[0],i[1]))
        edge_list_normal.append(edge(-i[1],i[0]))
        edge_list_reverse.append(edge(i[1],-i[0]))
        edge_list_reverse.append(edge(i[0],-i[1]))
    vertex_list=list(range(1,n+1))+[-i for i in range(1,n+1)]

    original_graph=graph(vertex_list)
    inverse_graph=graph(vertex_list)

    for i in edge_list_normal:
        original_graph.add_edge(i)
    for i in edge_list_reverse:
        inverse_graph.add_edge(i)
        
    inverse_graph.DFS()
    post_order=inverse_graph.post   #get post order
    #inverse_graph.reset_clock()     #reset clock
    original_graph.reset_clock()
    back_up=post_order
    post_order=[[post_order[i],i] for i in range(2*n)]   #get list, post_order,key
    post_order=sorted(post_order,key=lambda x:x[0])[::-1] #sort list
    all_scc=[]
    for i in post_order:
        if original_graph.post[i[1]]==0:  #not visited yet
            scc_list=[]
            original_graph.scc(i[1],scc_list)
            all_scc.append(scc_list)
    for i in all_scc:
        for j in range(len(i)):
            i[j]=trans_back(i[j])
        


    if valid_or_not(all_scc):
        print('SATISFIABLE')
        
        
        
        values={}
        #all_scc=sorted(all_scc,key=lambda x:back_up[x[0]])[::-1]
        
        
        
        for i in all_scc:
            for j in i:
                if j not in values:
                    values[j]=1
                    values[-j]=0
        order=[]
        for i in values:
            if values[i]==1:
                order.append(i)
        order=sorted(order,key=lambda x:abs(x))
        order=[str(i) for i in order]
        print(' '.join(order))
    else :
        print('UNSATISFIABLE')
        

threading.Thread(target=main).start()     

        
        
        