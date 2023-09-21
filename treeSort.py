class Node(object): 
def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
          self.root = None
        
    def insert(self, data): 
          self.root = self._insert_value(self.root, data)  
          return self.root is not None

    def _insert_value(self, node, data):  
        if node is None: 
	node = Node(data)
        else:
         	if data <= node.data:
                	            node.left = self._insert_value(node.left, data)
            	else:
                             node.right = self._insert_value(node.right, data)
        return node

        
def in_order_traversal(self): 
        def _in_order_traversal(root):
  	if root is None:
                	         pass
            	else:
                 	         _in_order_traversal(root.left)
              	         print(root.data, end=' ')
             	         _in_order_traversal(root.right)
        	         _in_order_traversal(self.root)

array = [15, 5, 17, 1, 8]  

bst = BinarySearchTree()
for x in array:
        bst.insert(x)
    
bst.in_order_traversal()





#카운팅 정렬
def countingSort(input):
    size = len(input)
    output = [0] * size

    max = input[0]
    for i in range(1,len(input)):
        if max < input[i]:
            max = input[i]
    
    count = [0] * (max+1)

    for i in range(0, size):
        count[input[i]] += 1
        
    for i in range(1, max+1):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        output[count[input[i]] - 1] = input[i]
        count[input[i]] -= 1
        i -= 1
        
    print(output)


data = [4, 2, 2, 8, 3, 3, 1]
print(data)
countingSort(data)
