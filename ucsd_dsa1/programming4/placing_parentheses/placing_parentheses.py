#finished
# Uses python3
def seperate(a):
    #a=input()
    digit=[int(a[i]) for i in range(len(a)) if ((i%2)==0)]
    symbol=[a[i] for i in range(len(a)) if ((i%2)==1)]



    return digit,symbol



def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinandMax(i,j,dic_M,dic_m,digit,symbol):
    min1=+10000000000
    max1=-10000000000
    for k in range(i,j):
        a=evalt(dic_M[i,k],dic_M[k+1,j],symbol[k-1])
        b=evalt(dic_M[i,k],dic_m[k+1,j],symbol[k-1])
        c=evalt(dic_m[i,k],dic_M[k+1,j],symbol[k-1])
        d=evalt(dic_m[i,k],dic_m[k+1,j],symbol[k-1])
        min1=min(min1,a,b,c,d)
        max1=max(max1,a,b,c,d)
    return min1,max1

def get_maximum_value(digit,symbol):
    n=len(digit)
    dic_m={}
    dic_M={}
    for i in range(1,n+1):
        dic_M[i,i]=digit[i-1]
        dic_m[i,i]=digit[i-1]
    for s in range(1,n):
        for i in range(1,n-s+1):
            j=i+s
            dic_m[i,j],dic_M[i,j]=MinandMax(i,j,dic_M,dic_m,digit,symbol)
    return dic_M[1,n]



if __name__ == "__main__":
    
    
    digit,symbol=seperate(input())
    print(get_maximum_value(digit,symbol))
