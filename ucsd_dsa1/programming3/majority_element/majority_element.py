# Uses python3
# finished
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

   
    mid=int((left+right)/2)
    A=get_majority_element(a,left,mid)
    B=get_majority_element(a,mid,right)
    if (A==B):
        return A
    else:
        count1=0
        count2=0
        for i in range(left,right):
            if a[i]==A:
                count1+=1
            if a[i]==B:
                count2+=1
        if (count1>count2):
            if (count1 > (right-left)/2):
                return A
            else:
                return -1
        else:
            if count2 > (right-left)/2 :
                return B
            else:
                return -1
    #write your code here

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
       print(1)
    else:
       print(0)
    #x=int(get_majority_element(a,0,n))
    #x+=1
    #print (x)