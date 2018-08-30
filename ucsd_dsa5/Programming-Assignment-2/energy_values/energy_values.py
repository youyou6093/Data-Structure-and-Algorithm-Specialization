# python3
# done
EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)

    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    #make sure the selected pivot element is not zero
    while(a[pivot_element.row][pivot_element.column]==0):
        pivot_element.column+=1

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
    #normalize the pivot row
    b[row]/=a[row][column]
    a[row]=[a[row][k]/a[row][column] for k in range(size)]
    for i in range(size):
        if i!=row:
            ratio=-a[i][column]/a[row][column] 
            a[i]=[a[i][k]+ratio*a[row][k] for k in range(size)]
            b[i]=b[i]+ratio*b[row]

    #make the pivot column 0 unless for pivot row


    

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
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.6lf" % column[row],end=' ')

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
