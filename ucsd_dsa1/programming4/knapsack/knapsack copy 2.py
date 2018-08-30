# Uses python3
import sys

def optimal_weight(W,n,w):
    value_dic={}
    for i in range(W+1):
        value_dic[i,0]=0
    for i in range(n+1):
        value_dic[0,i]=0
    
    for i in range(1,n+1):         #金条数组
        for j in range(1,W+1):                #总重量
            value_dic[(j,i)]=value_dic[j,i-1]
            if w[i-1]<=j:
                value=value_dic[j-w[i-1],i-1]+w[i-1]
                if value_dic[(j,i)]<value:
                    value_dic[(j,i)]=value
    return value_dic[(W,n)]


if __name__ == '__main__':

    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
   
    
    print(optimal_weight(W, n,w))
