# python3
#done
import sys

NA = -1

def build_trie(patterns):
    tree = dict()
    tree[0]={}
    max_node=0
    
    for pattern in patterns:
        current_node=0
        for char in pattern:
            if char in tree[current_node]:
                current_node=tree[current_node][char]
            else:
                max_node+=1
                new_node=max_node       
                tree[current_node][char]=new_node
                current_node=new_node
                tree[new_node]={}
        tree[current_node][-1]=-1
    # write your code here
    return tree

class Node:
    def __init__ (self):
        self.next = [NA] * 4


def forward_1_point(pos,text,Tree):
    start_pos=pos
    current=0
    while True:
        if -1 in Tree[current]:
            return start_pos
        elif pos==len(text):
            return -1 
        elif text[pos] in Tree[current]:  
            current=Tree[current][text[pos]]  #go to next node
            pos+=1
        else:
            return -1


def solve (text, n, patterns):
    result = []
    Tree=build_trie(patterns)
    for i in range(len(text)):
        if forward_1_point(i,text,Tree)!=-1:
            result.append(i)

    return result


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]




ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
