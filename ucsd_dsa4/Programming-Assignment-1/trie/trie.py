#Uses python3
import sys
#DONE
# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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

    # write your code here
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    #print tree
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
