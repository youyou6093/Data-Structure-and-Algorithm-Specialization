# python3
#done


from sys import stdin
import itertools

EPS = 1e-6
PRECISION = 20



#part 1: Solve a linear equation
class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while(a[pivot_element.row][pivot_element.column]==0):
        pivot_element.column+=1
        if pivot_element.column==len(a):
            return -1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    
    row=pivot_element.row
    column=pivot_element.column
    size=len(a)
    b[row]/=a[row][column]
    a[row]=[a[row][k]/a[row][column] for k in range(size)]


    for i in range(size):
        if i!=row:
            # print (a[row][column])
            ratio=-a[i][column]/a[row][column] 
            a[i]=[a[i][k]+ratio*a[row][k] for k in range(size)]
            b[i]=b[i]+ratio*b[row]
    

    

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        if SelectPivotElement(a, used_rows, used_columns)==-1:
            return -1
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

#----------------------------------


def satisfy(A,b,solution):            #check whether a solution satisify the inequality
    for i,j in enumerate(A):         #i number ,j coefficients
        left=0
        for k,l in enumerate(j):
            left+=solution[k]*l
        if left>(b[i]+1e-3):
            return False
    return True


def get_value(c,solution):              # get optimal
    sum=0
    for i in range(len(c)):
        sum+=c[i]*solution[i]
    return sum



def solve_diet_problem(n, m, A, b, c):  
    # add axis>=0 inequality
    for i in range(m):
        equailty=[0 if j!=i else -1 for j in range(m)]
        A.append(equailty)
        b.append(0)     

    #add a check for infinity  
    A.append([1 for j in range(m)])
    b.append(10000000000)         
    size=len(b)
    subsets=list(itertools.combinations(range(size),m))
    #get all subsets of linear equations
    result=[]
    #solve all subsets
    for i in subsets:
        sub_matrix=[A[j][:] for j in i]
        sub_results=[b[j] for j in i]
        equation=Equation(sub_matrix,sub_results)
        if SolveEquation(equation)!=-1: 
            result.append(SolveEquation(equation))
    #keep the valid result 
    result=[j for j in result if satisfy(A,b,j)] 
    values=[get_value(c,j) for j in result]
    #if no solution found
    if values==[]:
        return -1,0
    #found the optimal
    max_index=0
    for i in range(len(values)):
        if values[i]>values[max_index]:
            max_index=i
    ansx=result[max_index]
    anst=0
    # if optimal is too big
    if values[max_index]>999999999:   #just some corner case
        anst=1
    return anst,ansx

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:  
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
    
