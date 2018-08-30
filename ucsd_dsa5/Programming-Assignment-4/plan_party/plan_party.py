#uses python3
#done
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.max=0


def ReadTree():
    size = int(input())


    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)
    max1=tree[vertex].weight        #this value is self+grand child
    max2=0                          #this value is child
    for child in tree[vertex].children:
        if child!=parent:
            max2+=tree[child].max
            for grandchild in tree[child].children:
                if((grandchild!=child ) &(grandchild!=parent)):
                    max1+=tree[grandchild].max
    tree[vertex].max=max(max1,max2)
        

    


def MaxWeightIndependentTreeSubset(tree):

    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    # You must decide what to return.
    return tree[0].max


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()