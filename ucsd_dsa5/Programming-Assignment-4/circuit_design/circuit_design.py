# python3
import sys
#sys.setrecursionlimit(10**6)
# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
#def isSatisfiable():
#    for mask in range(1<<n):
#        result = [ (mask >> i) & 1 for i in range(n) ]
#        formulaIsSatisfied = True
#        for clause in clauses:
#            clauseIsSatisfied = False
#            if result[abs(clause[0]) - 1] == (clause[0] < 0):
#                clauseIsSatisfied = True
#            if result[abs(clause[1]) - 1] == (clause[1] < 0):
#                clauseIsSatisfied = True
#            if not clauseIsSatisfied:
#                formulaIsSatisfied = False
#                break
#        if formulaIsSatisfied:
#            return result
#    return None

#result = isSatisfiable()
#if result is None:
#    print("UNSATISFIABLE")
#else:
#    print("SATISFIABLE");
#    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))


class edge:
    def __init__(self,from_,to_):
        self.from_=from_
        self.to_=to_
        
class graph:
    def __init__(self,vertexs):
        self.vertexs={}
        for i in vertexs:
            self.vertexs[i]=set([])
        
    def add_edge(self,edge):
        self.vertexs[edge.from_].add(edge.to_)  #add a new edge
            
    def DFS(self):
        self.clock=0
        self.pre={}
        self.post={}
        for i in self.vertexs.keys():
            self.pre[i]=0
            self.post[i]=0
        for i in self.vertexs.keys():
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
        self.pre={}
        self.post={}
        for i in self.vertexs.keys():
            self.pre[i]=0
            self.post[i]=0
#        self.clock=0
#        for i in self.pre.keys():
#            self.pre[i]=0
#            self.post[i]=0
            
    def scc(self,x,scc_list):
        
        scc_list.append(x)
        self.clock+=1
        self.pre[x]=self.clock
        for i in self.vertexs[x]:   #all the neighbors
            if self.pre[i]==0:   #haven't visit this vertex
                #print(i)
                self.scc(i,scc_list)
        self.clock+=1
        self.post[x]=self.clock
                
    
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
post_order=[[post_order[i],i] for i in post_order.keys()]   #get list, post_order,key
post_order=sorted(post_order,key=lambda x:x[0])[::-1] #sort list
all_scc=[]
for i in post_order:
    if original_graph.post[i[1]]==0:  #not visited yet
        scc_list=[]
        original_graph.scc(i[1],scc_list)
        all_scc.append(scc_list)
    
def valid_or_not(all_scc):
    for i in all_scc:
        for j in i:
            if -j in i:
                return  False
    return True

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
    

        

        
        
        