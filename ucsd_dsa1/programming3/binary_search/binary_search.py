#finished
# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    #print (left,right,x)
    while((right-left)!=1):
        mid=int((left+right)/2)
        if x>=a[mid]:
            left=mid
        else:
            right=mid
        #print (left,right)
    if a[left]==x:
        return left
    else:
        return -1

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    #print("finish")
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        #binary_search(a,x)
        print(binary_search(a, x), end = ' ')
