# python3
#done
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.

def num(i,j):
    return (n*i+j)
digits=range(1,n+1)
clauses=[]

#appear in path.
for i in range(n):
    clauses.append([num(i,j) for j in digits])
    
#all vertex in path.
for j in range(1,n+1):
    clauses.append([num(i-1,j) for i in digits])

#only once in path
for i in range(n):
    for j in range(1,n+1):
        for k in range(j+1,n+1):
            clauses.append([-num(i,j),-num(i,k)])

#only one path number possible 
for i in range(1,n+1):
    for j in range(n):
        for k in range(j+1,n):
            clauses.append([-num(j,i),-num(k,i)])

adj=[[0 for i in range(n)] for j in range (n)]
for i in edges:
    adj[i[0]-1][i[1]-1]=1
    adj[i[1]-1][i[0]-1]=1

#connected edges
for i in range(n):
    for j in range(i+1,n):
        if adj[i][j]==0:
            #print(i,j)
            for k in range(1,n):
                clauses.append([-num(i,k),-num(j,k+1)])
                clauses.append([-num(j,k),-num(i,k+1)])


my_set=set([])
for i in clauses:
    for j in i:
        if abs(j) not in my_set:
            my_set.add(j)

print(len(clauses),len(my_set))
for i in clauses:
    i.append(0)
    xxx=[str(j) for j in i]
    print( ' '.join(xxx))