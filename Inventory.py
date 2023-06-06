class CategoryNode:
    def __init__(self, name : str = ""):
        self.name = name.lower()
        self.left = None
        self.right = None
        self.brand_head = None

class Category:
    def __init__(self):
        self.root = None
        self.current = None

    def addCategory(self, node : CategoryNode, categoryName : str):
        categoryName = categoryName.lower()
        
        if not self.root:
            newCategory = CategoryNode(categoryName)
            newCategory.brand_head = Brand()
            self.root = newCategory
            print("root added")
            return self.root
        
        elif not node:
            newCategory = CategoryNode(categoryName)
            newCategory.brand_head = Brand()
            return newCategory

        else:
            if categoryName == node.name:
                print("Category already exists")
            
            elif categoryName < node.name:
                node.left = self.addCategory(node.left, categoryName)
            
            else:
                node.right = self.addCategory(node.right, categoryName)
        return node

    def height(self, node : CategoryNode):
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

    def levelOrderTraversal(self, node : CategoryNode): # Breadth First
        levels = self.height(node) + 1
        for level in range(levels):
            self.printNodesOnLevel(node, level)

    def printNodesOnLevel(self, node : CategoryNode, level : int): # Breadth First
        if not node:
            return
        elif level == 0:
            print(node.name, " ")
            return
        else:
            self.printNodesOnLevel(node.left, level - 1)
            self.printNodesOnLevel(node.right, level - 1)
    
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

        if not node:
            return None
        else:
            if node.name == categoryName:
                return node
            elif categoryName < node.name:
                return self.searchCategory(node.left, categoryName)
            else:
                return self.searchCategory(node.right, categoryName)

class  brandNode:
    def __init__(self, name : str = ""):
        self.next = None
        self.product_head = None
        self.name = name.lower()

class Brand:
    def __init__(self):
        self.head = None
        self.current = None

    def searchBrand(self, brandName : str) -> brandNode | None:
        self.current = self.head
        while self.current:
            if self.current.name == brandName.lower():
                return self.current
            self.current = self.current.next
        return None

    def printBrands(self):
        self.current = self.head
        while self.current:
            print(self.current.name + ", ")
            self.current = self.current.next

    def addBrand(self, brandName : str) -> brandNode | None:
        newBrand = brandNode(brandName)
        newBrand.product_head = Product()

        if not self.head:
            self.head = newBrand
            return self.head
        
        self.current = self.head
        while self.current.next:
            self.current = self.current.next
        self.current.next = newBrand
        return self.current.next

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

    def __init__(self, name = "", category = "", brand = "", price = 0.0, quantity = 0):
        self.data = {
            "name" : name.lower(),
            "category" : category.lower(),
            "brand" : brand.lower(),
            "price" : price,
            "quantity" : quantity
        }
        self.next = None

class Product():
    def __init__(self):
        self.head = None
        self.current = None

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
    
    def addProduct(self, productName = "", categoryName = "", brandName = "", price = 0.00, quantity = 0):
        newProduct = ProductNode(productName, categoryName, brandName, price, quantity)

        if not self.head:
            self.head = newProduct
            return self.head
        
        self.current = self.head
        while self.current:
            if self.current.data["name"] == newProduct.data["name"]:
                self.current.data["quantity"] += newProduct.data["quantity"]
                return self.current.data
            self.current = self.current.next
        self.current = newProduct
        return self.current

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
    
    def searchProduct(self, productName : str):
        productName = productName.lower()
        self.current = self.head
        while self.current:
            if self.current.data["name"] == productName:
                return self.current.data
            self.current = self.current.next
        return None