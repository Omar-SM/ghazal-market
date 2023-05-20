class CategoryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.Brand=None
class Category:
    def __init__(self):
        self.root = None
        self.current = None
    def defineRoot(self, data):
        if self.root == None:
            newNode = CategoryNode(data)
            self.root = newNode
        else:
            print("Root already inserted")
    def insert(self, node, option, data):
        if node != None:
            newNode = CategoryNode(data)
            if option == "left" and node.left == None:
                node.left = newNode
            elif option == "right" and node.right == None:
                node.right = newNode
            else:
                print("Enter a valid insert commmand")
    def searchBST(self , node, data):
        if node == None:
            return False
        else:
            if node.data==data:
                return True
            elif data<node.data:
                self.searchBST(node.left,data)
            else:
                self.searchBST(node.right,data)



class BrandNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.product=None
class Brand:
    def __init__(self):
        self.head=None
        self.current=None
        self.tail=None

    
    def tailmarker(self):   #this method is used to mark the tail of the list
        self.current=self.head
        while self.current is not None:
            if self.current.next is None:
                self.tail=self.current
            self.current=self.current.next

    def searchLinkedList(self,brandName,category):
        BST=Category()
        if BST.searchBST(category)==True:
            self.current=self.head
            while self.current is not None:
                if self.current.data==brandName:
                    return True
                else:
                    self.current=self.current.next
        else:
            return False

    def trav(self):
        self.current=self.head
        while self.current is not None:
            print(self.current.data)
            self.current=self.current.next

    def insert(self, data):
        n=BrandNode(data)
        if self.head is None:
            self.head =n
            self.current = n
            self.tail=n
        else:
            if self.current is None:
                self.current = self.head
                n.next = self.current.next
                self.current.next = n
                self.current = n
                if n.next is None:
                    self.tail=n
        
    def append(self,data):
        n=BrandNode(data)
        self.tailmarker()
        if self.head is None:
            self.head=n
            self.current=n
            self.tail=n
        else:
            self.tail.next = n
            self.tail = n
            self.current = n
    

class ProductNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Product():
    def __init__(self):
        self.head=None
        self.current=None
        self.tail=None

    
    def tailmarker(self):   #this method is used to mark the tail of the list
        self.current=self.head
        while self.current is not None:
            if self.current.next is None:
                self.tail=self.current
            self.current=self.current.next

    def trav(self):
        self.current=self.head
        while self.current is not None:
            print(self.current.data)
            self.current=self.current.next

    def insert(self, data):
        n=ProductNode(data)
        if self.head is None:
            self.head =n
            self.current = n
            self.tail=n
        else:
            if self.current is None:
                self.current = self.head
                n.next = self.current.next
                self.current.next = n
                self.current = n
                if n.next is None:
                    self.tail=n
        
    def append(self,data):
        n=ProductNode(data)
        self.tailmarker()
        if self.head is None:
            self.head=n
            self.current=n
            self.tail=n
        else:
            self.tail.next = n
            self.tail = n
            self.current = n
    def remove(self,data):
        rem_data=None
        prev=self.head
        self.current=self.head
        while self.current!=data:
            if self.current.data==data:
                if self.current.data['quantity']==0:
                    rem_data=data
                    prev.next=self.current.next
                    self.current.next=None
                    print("the removed data : "+str(rem_data))
                    return
                else:
                    print("cannt remove this product(items still exist)")
                    return
            else:
                if self.current.next is None:
                    print("there is no such data to remove")
                    break
                else:
                    prev=self.current
                    self.current=self.current.next
    
    def addProduct(self , data):
        BST=Category()
        brnd=Brand()
        if BST.search(data['category'])==True:
            if brnd.search(data['brand'])==True:
                self.append(data)
            else:
                brnd.append(data['brand'])
                self.append(data)
        else:
            if BST.root>data['category']:
                BST.insert(BST.root,'left',data['category'])
                BST.Brand=brnd.append(data['brand'])
                brnd.product=self.append(data)
            else:
                BST.insert(BST.root,'right',data['category'])
                BST.Brand=brnd.append(data['brand'])
                brnd.product=self.append(data)
    def sell(self,data,amount):
        self.current=self.head
        while self.current.data!=data:
            if self.current.data==data:
                if self.current.data['quantity']!=0 and self.current.data['quantity']>=amount:
                    quantity=self.current.data['quantity']
                    quantity=quantity-amount
                    self.current.data['quantity']=quantity
                else:
                    print("cant sell this item bcz quantity is :"+int(self.current.data['quantity']))
                    return
            self.current=self.current.next
            
    def searchProduct(self,data):
        BST=Category()
        brnd=Brand()
        if BST.search(data['category'])==True:
            if brnd.search(data['brand'])==True:
                self.current=self.head
                x=0
                while self.current.data!=data:
                    if self.current.data==data:
                     print(self.current.data)
                     x=1
                     return
                    self.current=self.current.next
                if x==0:
                    print("the product doesnt exist")
            else:
                print("the category exist, but the brand and the product does not exist")
        else:
            print("all this category doesnt exist")
