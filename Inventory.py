class CategoryNode:
    def __init__(self, name : str = ""):
        self.name = name
        self.left = None
        self.right = None
        self.brand_head = None


class Category:
    def __init__(self):
        self.root = None
        self.current = None

    def inorderTraverse(self, node): # Depth First
        if node != None:
            self.inorderTraverse(node.left)
            print(node.data, " ")
            self.inorderTraverse(node.right)
    
    def defineRoot(self, data):
        if self.root == None:
            newNode = CategoryNode(data)
            self.root = newNode
        else:
            print("Root already inserted")

    def addCategoty(self, node : CategoryNode, categoryName : str):
        if not node:
            node = self.root

        if not node:
            newCategoryNode = CategoryNode(categoryName)
            self.root = newCategoryNode
            print("Root added")
            return

        if categoryName.lower() == node.name.lower():
            return "node already exists"
        
        elif categoryName.lower() < node.name.lower():
            node.left = self.addCategoty(node.left, categoryName)
        
        else:
            node.right = self.addCategoty(node.right, categoryName)

    def printLeafNodes(self, node):
        if node == None:
            print("No Leaf Nodes")
            return
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
        
    def searchCategory(self , node : CategoryNode, categoryName : str) -> CategoryNode | None:
        categoryName = categoryName.lower()

        if node == None:
            return None
    
        if node.name.lower() == categoryName:
            return node
        elif categoryName < node.name.lower():
            self.searchCategory(node.left, categoryName)
        else:
            self.searchCategory(node.right, categoryName)

class  brandNode:
    def __init__(self,data):
        self.next = None
        self.product_head = None
        self.data = data

class Brand:
    def __init__(self):
        self.head=None
        self.current=None
        self.tail=None

    
    def tailmarker(self, category : CategoryNode, categoryName):   #this method is used to mark the tail of the list
        checkNode = category.searchBST(category.root, categoryName)
        if checkNode == None:
            return None
        else:
            self.current = checkNode.brand_head
            while self.current is not None:
                if self.current.next is None:
                    self.tail = self.current
                self.current = self.current.next

    def searchBrand(self, brandName : str, category : CategoryNode, categoryName : str) -> brandNode | None:
        checkNode = category.searchBST(category.root, categoryName)
        if checkNode != None:
            self.current = checkNode.brand_head
            while self.current is not None:
                if self.current.data == brandName:
                    return self.current
                else:
                    self.current = self.current.next
        else:
            return None

    def printBrands(self, category : CategoryNode, categoryName : str):
        checkNode = category.searchBST(category.root, categoryName)
        if checkNode == None:
            return "this brand doesnt exist"
        else:
            self.current = checkNode.brand_head
            while self.current is not None:
                print(self.current.data)
                self.current = self.current.next

    def addBrand(self, data, category : CategoryNode, categoryName):
        n = brandNode(data)
        checkNode = category.searchBST(category.root,categoryName)
        if checkNode == None:
            category.addCategory(category.root, categoryName)
            category.brand_head = n
            self.head = n
            self.current = n
            self.tail = n
        else:
            self.tailmarker()
            self.tail.next = n
            self.tail = n
            self.current = n

# This node is for the sales log Queue
# saleInfo is the data, containing the name, category, brand, and price of the product
class SalesNode:
    def __init__(self, saleInfo : dict = { "name" : "", "category" : "", "brand" : "", "price" : 0.00 }):
        self.saleInfo = saleInfo
        self.next = None

    def __init__(self, name = "", category = "", brand = "", price = 0.0):
        self.saleInfo = {
            "name" : name,
            "category" : category,
            "brand" : brand,
            "price" : price
        }
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

class ProductNode:
    def __init__(self, data = { "name" : "", "category" : "", "brand" : "", "price" : 0.00, "quantity" : 0 }):
        self.data = data
        self.next = None 

    def __init__(self, name = "", category = "", brand = "", price = 0.0, quantity = 0):
        self.data = {
            "name" : name,
            "category" : category,
            "brand" : brand,
            "price" : price,
            "quantity" : quantity
        }
        self.next = None

class Product():
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None

    # This method is used to mark the tail of the list
    def tailmarker(self, category : Category, categoryName : str, brand : Brand, brandName : str):   
        if brand.searchBrand(brandName, category, categoryName):
            self.current = brand.head
            while self.current:
                if not self.current.next:
                    self.tail = self.current

                self.current = self.current.next
        else:
            return None

    def printAllProducts(self, category : Category, categoryName : str, brand : Brand, brandName : str):
        brandSearchResult = brand.searchBrand(brandName, category, categoryName)
        if brandSearchResult:
            self.current = brandSearchResult.product_head
            while self.current:
                if self.current.next:
                    print(self.current.data["name"] + ", ")
                else:
                    print(self.current.data["name"] + ".")
                self.current = self.current.next
    
    def addProduct(self, productName = "", category : Category = None, categoryName = "", brand : Brand = None, brandName = "", price = 0.00, quantity = 0):
        newProduct = ProductNode({ productName, categoryName, brandName, price, quantity })

        brandSearchResults = brand.searchBrand(brandName, category, categoryName)
        if brandSearchResults:
            self.current = brand.searchBrand(brandName, category, categoryName).product_head

            self.tailmarker(category=category, categoryName=categoryName, brand=brand, brandName=brandName)

            self.tail.next = self.tail = newProduct
        else:
            brand.addBrand(data=brandName, category=category, categoryName=categoryName)
            self.addProduct(productName=productName, category=category, categoryName=categoryName, brand=brand, brandName=brandName, price=price, quantity=quantity)

    def sellProduct(self, category : Category, categoryName : str, brand : Brand, brandName : str, productName : str, amount : int, salesLog : SalesLog):
        brandSearchResult = brand.searchBrand(brandName, category, categoryName)

        if not brandSearchResult:
            print("The category or the brand doesn't exists.")
            return None
        
        self.current = brandSearchResult.product_head
        while self.current:

            if self.current.data["name"] == productName:
                quantity = self.current.data['quantity']
                
                if quantity != 0 and quantity >= amount:
                    self.current.data['quantity'] -= amount

                    for i in range(amount):
                        salesLog.addSaleLog({ productName, categoryName, brandName, self.current.data['price']})
                    return

                else:
                    print("Quantity in stock is limited to: " + str(self.current.data['quantity']))
                    return None
            
            self.current = self.current.next
    
    def searchProduct(self, productName : str, category : Category, categoryName : str, brand : Brand, brandName : str):
        brandSearchResult = brand.searchBrand(brandName, category, categoryName)

        if not brandSearchResult:
            print("The category or brand doesn't exists.")
            return None
    
        self.current = brand.searchBrand(brandName, category, categoryName).product_head

        while self.current:
            if self.current.data["name"] == productName:
                return self.current.data
            self.current = self.current.next

        print("Product Not Found.")
        return None