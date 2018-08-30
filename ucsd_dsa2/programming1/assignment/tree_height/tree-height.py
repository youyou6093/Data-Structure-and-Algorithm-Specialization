# python3
#done
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.dic={}
                for i,key in enumerate(self.parent):
                    if key in self.dic:
                        self.dic[key]+=[i]
                    else:
                        self.dic[key]=[i]
            

        def compute_height_old(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

        def compute_height(self):
            return self.compute_height_i(-1)-1

        def compute_height_i(self,key):
            if (key in self.dic)==0:
                return 1
            max_h=0
            for i in self.dic[key]:
                max_h=max(max_h,self.compute_height_i(i))
            return max_h+1


        


def main():
    tree = TreeHeight()
    tree.read()
    #print(tree.parent)
    #print(tree.compute_height())
    print(tree.compute_height())
threading.Thread(target=main).start()
