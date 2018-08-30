# python3
#done
import itertools
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
#def printEquisatisfiableSatFormula():
#    print("3 2")
#    print("1 2 0")
#    print("-1 -2 0")
#    print("1 -2 0")
clauses=[]
digits=range(1,4)
def varnum(i,j):    # i is vertex, j is color
    return 3*i+j

def exactly_one_of(literals):
    clauses.append([l for l in literals])
    
    for pair in itertools.combinations(literals,2):
        clauses.append([-l for l in pair])
        

#one color for each vertex        
for i in range(n):
    exactly_one_of([varnum(i,k) for k in digits])



#no same color for vertex closed to each other
for i in edges:
   for k in digits:
       #exactly_one_of([varnum(j-1,k) for j in i])
       literals=[varnum(j-1,k) for j in i]
       clauses.append([-literals[0],-literals[1]])

#printEquisatisfiableSatFormula()
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
