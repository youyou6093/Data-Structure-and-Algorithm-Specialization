#python3
#done although there are a lot of tricky part






class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0




# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.n=n
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]          #vertex

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))    #the indices of the edges
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))       #the indices of the edges
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]     #id of an edges

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        

        #also update the residual graph
        if(id%2==0):
            forward_id=id
        else:
            forward_id=id-1
        u=self.edges[forward_id].u
        v=self.edges[forward_id].v
        utov=self.edges[forward_id].capacity-self.edges[forward_id].flow
        vtou=self.edges[forward_id].flow
        self.adj[u][v]=utov
        self.adj[v][u]=vtou


#get the residual graph
    def get_residual(self):
        self.adj={}
        for i in range(self.n):
            self.adj[i]={}            #construct points
        for i,j in enumerate(self.graph):
            for edge_id in j:         #
                if (edge_id % 2)==0:   #forward edge

                    u=self.edges[edge_id].u
                    v=self.edges[edge_id].v
                    
                    utov=self.edges[edge_id].capacity-self.edges[edge_id].flow
                    vtou=self.edges[edge_id].flow
                    #print(u,v,utov,vtou)
                    if v in self.adj[u]:
                        self.adj[u][v]+=utov

                    else:
                        self.adj[u][v]=utov
                    #print(self.adj)
                    if u in self.adj[v]:
                        self.adj[v][u]+=vtou
                    else:
                        self.adj[v][u]=vtou
                    #print(self.adj)
                    
#bfs
    def bfs(self):
        dis={}
        parent={}
        
        my_queue=[]
        for i in range(self.n):
            dis[i]=100000
            parent[i]=-1
        dis[0]=0
        my_queue.append(0)
        while my_queue:
            u=my_queue.pop(0)
            for i in self.adj[u].keys():    #all neighbors of u
                if self.adj[u][i]!=0:       #the edge actually exist
                    if dis[i]==100000:
                        my_queue.append(i)
                        dis[i]=dis[u]+1
                        parent[i]=u
        return parent

#find a good path, return -1 if not found
    def get_a_path(self):
        parent=self.bfs()
        pos=self.n-1
        path=[pos]
        while pos!=0:
            pos=parent[pos]
            if pos==-1:
                return -1
            path.append(pos)
        path=path[::-1]


        return path


#upadate the flow based on result
    def update(self,path):

        path=self.get_a_path()
        maxflow=self.adj[path[0]][path[1]]   #cap from 0 to 1
        for i in range(len(path)-1):
            start=path[i]
            end=path[i+1]
            cap=self.adj[start][end]
            if cap<maxflow:
                maxflow=cap

        for i in range(len(path)-1):
            start=path[i]
            end=path[i+1]
            ids=self.graph[start]
            for j in ids:
                if self.edges[j].v==end:
                    self.add_flow(j,maxflow)
                    break


#get the maximum flow
    def maximize_flow(self):
        self.get_residual()
        while True:
            path=self.get_a_path()
            if path!=-1:
                self.update(path)
            else:
                break

        





def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    dic={}

    for _ in range(edge_count):
        u,v,capacity = map(int, input().split())
        if (u,v) in dic:
            dic[u,v]+=capacity
        else:
            dic[u,v]=capacity

    for i in dic.keys():
        graph.add_edge(i[0]-1,i[1]-1,dic[i])

    # for _ in range(edge_count):
    #     u, v, capacity = map(int, input().split())
    #     graph.add_edge(u - 1, v - 1, capacity)
    return graph



#get the number of max flow
def max_flow(graph, from_, to):
    flow = 0
    graph.maximize_flow()
    for i in graph.graph[0]:
        flow+=graph.edges[i].flow
    return flow


if __name__ == '__main__':
    graph = read_data()
    graph.get_residual()
    # for i in range(len(graph.edges)):
    #     if i%2==0:
    #         print(graph.edges[i].u,graph.edges[i].v,graph.edges[i].capacity)
    #print(graph.adj)
    

    print(max_flow(graph, 0, graph.size() - 1))
