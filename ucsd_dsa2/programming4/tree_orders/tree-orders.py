# python3
#done
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a        #index
			self.left[i] = b       #index
			self.right[i] = c      #index  

	def inOrder(self):
		self.result = []
		# Finish the implementation
		# You may need to add a new recursive method to do that
		self.inorder_tra(0)
		return self.result

	def test(self,node):
		print(self.key[node])

	def inorder_tra(self,node):    #index of the array
		#print(self.key[node])
		#print(node)
		if node==-1:               #make sure there is childs
			#print("xx")
			return self.result
		#print(node)
		self.inorder_tra(self.left[node])   #left
		self.result.append(self.key[node])
		self.inorder_tra(self.right[node])  #right

	def preorder_tra(self,node):
		if node==-1:
			return self.result
		self.result.append(self.key[node])
		self.preorder_tra(self.left[node])
		self.preorder_tra(self.right[node])

	def preOrder(self):
		self.result = []
		self.preorder_tra(0)
		# Finish the implementation
		# You may need to add a new recursive method to do that
								
		return self.result


	def postorder_tra(self,node):
		if node==-1:
			return self.result
		self.postorder_tra(self.left[node])
		self.postorder_tra(self.right[node])
		self.result.append(self.key[node])

	def postOrder(self):
		self.result = []
		self.postorder_tra(0)
		# Finish the implementation
		# You may need to add a new recursive method to do that
								
		return self.result

def main():
	tree = TreeOrders()
	tree.read()
	#tree.inOrder()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
