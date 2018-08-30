# Uses python3
import sys

def optimal_weight(W,n,w,value_dic):
    
    if (W==0) or (n==0):
        value_dic[(W,n)]=0
    
    if (W,n) in value_dic:
        return value_dic[(W,n)]
    
    for i in range(1,n+1):         #金条数组
        for j in range(1,W+1):                #总重量
            #print ("kkk")
            value_dic[(j,i)]=optimal_weight(j,i-1,w,value_dic)
            if w[i-1]<=j:
                value=optimal_weight(j-w[i-1],i-1,w,value_dic)+w[i-1]
                if value_dic[(j,i)]<value:
                    value_dic[(j,i)]=value
    return value_dic[(W,n)]


if __name__ == '__main__':

    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    value_dic={}
    #print (W,n)
    print(optimal_weight(W, n,w,value_dic))
    #print (value_dic.keys())
