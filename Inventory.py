import dataclasses


class CategoryNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.Brand = None

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

    # TO DO
    # The input is the category's name only
    # It should return the node that is pointing at the brands of the key category
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
                
    def printCategories(self):
        # TO DO
        # It should print all categories' names in the tree in a well formatted way
        pass

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

    # TO DO
    # The input it takes is brand's name, and category
    # It should return the node that is pointing at the products of the key brand
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

    # TO DO
    # It should take as input the category name and the category BST
    # These will be optional so make the code work if the user provided these info or didn't
    # In case category info is provided -> Search the category for the right brands list and print it
    # If not -> Just print the brands list
    # This way in case I'm doing a search providing the category's name and the BST it'll work
    # And if lets say I searched for a specified category in the category class and it return the node pointing to the brands list
    # If I want to print that list I don't need to check for the category's name
    # Contact me if you have any questions I tied to explain :)
    # Note: Printing them whould be in a well formatted way
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
    def __init__(self, data = { "name" : "", "category" : "", "brand" : "", "Price" : 0.00, "Quantity" : 0 }):
        self.data = data
        self.next = None 

class Product():
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None

    
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
    
    # TO DO
    # The input is the product's name, the category's name, the category, brand, price, and quantity
    # It should take the category as a BST
    # Search the category for the specified category, it should return the brands
    # Search the brands for the specified brand, it should return the products
    # Add the product to the linked list
    def addProduct(self, name = "", category = "", brand = "", price = 0.00, quantity = 0 ):
        newProduct = ProductNode({ name, category, brand, price, quantity })
        BST=Category()
        brnd=Brand()

        if BST.search(newProduct.data['category']) == True:
            if brnd.search(newProduct.data['brand']) == True:
                self.append(newProduct.data)
            else:
                brnd.append(newProduct.data['brand'])
                self.append(newProduct.data)
        else:
            if BST.root > newProduct.data['category']:
                BST.insert(BST.root,'left',newProduct.data['category'])
                BST.Brand=brnd.append(newProduct.data['brand'])
                brnd.product=self.append(newProduct.data)
            else:
                BST.insert(BST.root,'right',newProduct.data['category'])
                BST.Brand=brnd.append(newProduct.data['brand'])
                brnd.product=self.append(newProduct.data)

    # TO DO
    # The input is the name of the product, the category's name, the category, the brand, and quantity only
    # It should take the category as a BST (class instance)
    # Search the category for the specified category, it should return the brands
    # Search the brands for the specified brand, it should return the products
    # Search for the specified product and sell it
    # Leave the sales log part for Omar M (me)
    def sell(self, category, brand, name, amount):
        productToSell = ProductNode({ "name" : name, "category" : category, "brand" : brand })
        self.current = self.head
        while self.current.data:
            if self.current.data == productToSell.data:
                quantity = self.current.data['quantity']
                if quantity != 0 and quantity >= amount:
                    quantity -= amount
                    self.current.data['quantity'] = quantity
                    for i in range(amount):
                        SalesLog.addSaleLog({ name, category, brand, self.current.data['price']})
                    return

                else:
                    print("Quantity in stock is limited to: " + str(self.current.data['quantity']))
                    return
            
            self.current = self.current.next
    
    # TO DO
    # It should take the product's name, the category's name, the category, and brand only
    # It should take the category as a BST
    # Search the category for the specified category, it should return the brands
    # Search the brands for the specified brand, it should return the products
    # Search for the product key and return the node
    def searchProduct(self, data):
        BST = Category()
        brnd = Brand()

        if BST.search( data['category'] ) == True:
            if brnd.search( data['brand'] ) == True:
                self.current = self.head
                x = 0
                while self.current.data != data:
                    if self.current.data == data:
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

# This node is for the sales log Queue
# saleInfo is the data, containing the name, category, brand, and price of the product
class SalesNode:
    def __init__(self, saleInfo : dict = { "name" : "", "category" : "", "brand" : "", "price" : 0.00 }):
        self.saleInfo = saleInfo
        self.next = None

# The Sales Logs Queue
class SalesLog:
    def __init__(self):
        self.current = None
        self.front = None
        self.rear = None

    # print the sales log
    def traverse(self) -> None:
        if not self.front:
            print("There is no logs")
            return
        self.current = self.front
        while self.current:
            print(self.current.saleInfo)
            self.current = self.current.next

    # print the number of sales made
    def salesNumber(self) -> int:
        totalSalesNumber = 0
        if not self.front:
            return totalSalesNumber
        
        self.current = self.front
        while self.current:
            totalSalesNumber += 1
            self.current = self.current.next

        return totalSalesNumber
    
    def isEmpty(self) -> bool:
        return not self.front
        
    def getFront(self) -> dict:
        return self.front.saleInfo
    
    def getRear(self) -> dict:
        return self.rear.saleInfo
    
    # Enqueue a new sale
    def addSaleLog(self, saleInfo : dict = { "name" : "", "category" : "", "brand" : "", "price" : 0.00 }):
        newSaleNode = SalesNode(saleInfo)

        if self.isEmpty():
            self.front = newSaleNode
            self.rear = newSaleNode
            return

        self.rear.next = self.rear = newSaleNode

    # Delete the latest sale made
    def removeSaleLog(self) -> SalesNode | None:
        if self.isEmpty():
            print("There is nothing to dequeue")
            return
        
        self.current = self.front
        self.front = self.front.next

        # Fix rear
        if self.rear == self.current:
            self.rear = None

        dequeuedSale = self.current
        self.current = None
        return dequeuedSale
        
        

