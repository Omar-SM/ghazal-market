
class categoryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.brand_head=None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.current = None

    def inorderTraverse(self, node): # Depth First
        if node != None:
            self.inorderTraverse(node.left)
            print(node.data, " ")
            self.inorderTraverse(node.right)
    
    def defineRoot(self, data ):
        if self.root == None:
            newNode = categoryNode(data)
            self.root = newNode
    
        else:
            print("Root already inserted")

    def insert(self, node, data):
        if node == None:
            newNode = categoryNode(data)
            self.root=newNode
            return "root added"
        else:
            if data == node.data:
                return "node already exists"
            elif data <node.data:
                node.left=self

    def printLeafNodes(self, node):
        if node == None:
            return "No Leaf Nodes"
        else:
            if node.left == None and node.right == None:
                print(node.data, " ")
                return
            if node.left != None:
                self.printLeafNodes(node.left)
            if node.right != None:
                self.printLeafNodes(node.right)

    def height(self, node):
        if node == None:
            return -1
        if node.left == None and node.right == None:
            return 0
        else:
            heightLeftSubtree = self.height(node.left)
            heightRightSubtree = self.height(node.right)

            if heightLeftSubtree > heightRightSubtree:
                return heightLeftSubtree + 1
            else:
                return heightRightSubtree + 1

    def levelOrderTraversal(self, node): # Breadth First
        levels = self.height(node) + 1
        for level in range(levels):
            self.printNodesOnLevel(node, level)

    def printNodesOnLevel(self, node, level): # Breadth First
        if node == None:
            return
        elif level == 0:
            print(node.data, " ")
            return
        else:
            self.printNodesOnLevel(node.left, level-1)
            self.printNodesOnLevel(node.right, level-1)
    
    def isBST(self, node):
        if node == None:
            return True
        if node.left != None and self.maxValue(node.left) > node.data:
            return False
        if node.right != None and self.minValue(node.right) < node.data:
            return False
        if self.isBST(node.left) == False or self.isBST(node.right) == False:
            return False
        
        return True
        
    def maxValue(self, node):
        if node == None:
            return 0
        maxLeft = self.maxValue(node.left)
        maxRight = self.maxValue(node.right)
        if maxLeft > maxRight:
            max = maxLeft
        else:
            max = maxRight
        if node.data > max:
            max = node.data
        return max

    def minValue(self, node):
        if node == None:
            return 1000000000
        minLeft = self.minValue(node.left)
        minRight = self.minValue(node.right)
        if minLeft < minRight:
            min = minLeft
        else:
            min = minRight
        if node.data < min:
            min = node.data
        return min
        
    def searchCategory(self , node, data):
        if node == None:
            return None
        else:
            if node.data==data:
                return node
            elif data<node.data:
                self.searchBST(node.left,data)
            else:
                self.searchBST(node.right,data)
class  brandNode:
    def __init__(self,data):
        self.next=None
        self.product_head=None
        self.data=data

class Brand:
    def __init__(self):
        self.head=None
        self.current=None
        self.tail=None

    
    def tailmarker(self,category:categoryNode,categoryName):   #this method is used to mark the tail of the list
        checkNode=category.searchBST(category.root,categoryName)
        if checkNode==None:
            return None
        else:
            self.current=checkNode.brand_head
            while self.current is not None:
                if self.current.next is None:
                    self.tail=self.current
                self.current=self.current.next

    def searchBrand(self,brandName,category:categoryNode,categoryName):
        checkNode=category.searchBST(category.root,categoryName)
        if checkNode!=None:
            self.current=checkNode.brand_head
            while self.current is not None:
                if self.current.data==brandName:
                    return self.current
                else:
                    self.current=self.current.next
        else:
            return None

    def trav(self,category:categoryNode,categoryName):
        checkNode=category.searchBST(category.root,categoryName)
        if checkNode==None:
            return "this brand doesnt exist"
        else:
            self.current=checkNode.brand_head
            while self.current is not None:
                print(self.current.data)
                self.current=self.current.next

    def insert(self, data,category:categoryNode,categoryName):
        n=brandNode(data)
        checkNode=category.searchBST(category.root,categoryName)
        if checkNode==None:
            category.insert(category.root,categoryName)
            category.brand_head=n
            self.head=n
            self.current=n
            self.tail=n
        else:
            self.tailmarker()
            self.tail.next = n
            self.tail = n
            self.current = n

    

