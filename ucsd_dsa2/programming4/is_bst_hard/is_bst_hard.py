#!/usr/bin/python3
#done
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  for i in range(len(tree)):
    if Isbst(tree,i)==0:
      return False


  return True



def compare(tree,value,c):
  if c==-1:
    return -1
  if value<=tree[c][0]:
    return 0         #smaller
  if value>tree[c][1]:
    return 1          #bigger


def Isbst(tree,node):
    key=tree[node][0]  #value
    lc=tree[node][1]   #lc index
    rc=tree[node][2]   #rc index
    if compare(tree,key,lc)==0 or compare(tree,key,rc)==1:
      #print(node)
      return False
    if key<=biggest_l(tree,node) or key>smallest_r(tree,node):
      #print (node,biggest_l(tree,node),smallest_r(tree,node))
      return False
    return True
    #else:

def biggest_l(tree,node):
    pos=tree[node][1] #lc index of the node
    if pos==-1:
      return tree[node][0]-1
    big=tree[pos][0]  #current maximum
    while tree[pos][2]!=-1:                   #rc index !=-1 
      pos=tree[pos][2]                        #update pos
      big=tree[pos][0]                        #update maximum

    return big

def smallest_r(tree,node):
    pos=tree[node][2]
    if pos==-1:
      return tree[node][0]
    small=tree[pos][0]
    while tree[pos][1]!=-1:
      pos=tree[pos][1]
      small=tree[pos][0]
    return small


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []     #key,lc,rc
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  # for i in tree:
  #   print(i)

  #print biggest_l(tree,3)
  #print smallest_r(tree,0)
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
