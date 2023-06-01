class EmployeeNode:
    def __init__(self, name = "", position = "", age = 0, salary = 0.00):
        self.info = {
            "name" : name.lower(),
            "position" : position,
            "age" : age,
            "salary" : salary
        }
        self.left = None
        self.right = None
         
class Employee:
    def __init__(self):
        self.root = None
        self.current = None

    def searchEmployee(self, name : str, node : EmployeeNode):
        if node == None:
            return None
        
        name = name.lower()

        if node.info["name"] == name:
            return node
        
        elif name < node.info["name"]:
            return self.search(name, node.left)
        
        else:
            return self.search(name, node.right)
            
    def addEmployee(self, node : EmployeeNode, name : str, position : str, age : int, salary : float):
        name = name.lower()

        if not node:
            node = self.root

        if not self.root:
            newNode = EmployeeNode(name, position, age, salary)
            self.root = newNode
            print(f"{name} is added to the root")
            return
        
        if name == node.info["name"]:
            print(f"{name} is part of the staff")
        
        elif name < node.info["name"]:
            node.left = self.addEmployee(node.left, name, position, age, salary)

        else:
            node.right = self.addEmployee(node.right, name, position, age, salary)

    def deleteEmployee(self, name : str, node : EmployeeNode):
        name = name.lower()
        
        if name < node.info["name"]:
            node.left = self.deleteEmployee(name, node.left)
        
        elif name > node.info["name"]:
            node.right = self.deleteEmployee(name, node.right)
        
        else:
            if node.left == None and node.right == None:
                return None
            
            if node.left == None:
                return node.right
            
            if node.right == None:
                return node.left
            
            replacement = self.findSmallest(node.right)
            node.info = replacement
            node.right = self.deleteEmployee(node.right, replacement)
            return node
        
    def findSmallest(self, node : EmployeeNode):
        if node.left == None:
            return node.info
        
        else:
            return self.findSmallest(node.left)
        

    def alterEmployee(self, node : EmployeeNode, name : str, position : str, age : int, salary : float):
            employeeNode = self.searchEmployee(name, node)
            if employeeNode:
                employeeNode.info = {
                    "name" : name,
                    "position" : position,
                    "age" : age,
                    "salary" : salary
                }
                print(f"{name} has been updated")
                return employeeNode
            else:
                print(f"{name} not found")
                return

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

    def printAllEmployees(self, node : EmployeeNode):
        if not node:
            node = self.root
        
        if not self.root:
            print("There are no employees.")
            return
        
        levels = self.height(node) + 1

        for level in range(levels):
            self.printNodesOnLevel(node, level)

    def printNodesOnLevel(self, node : EmployeeNode, level : int): # Breadth First
        if node == None:
            return
        
        elif level == 0:
            print(node.info["name"] + ", ")
            return
        
        else:
            self.printNodesOnLevel(node.left, level - 1)
            self.printNodesOnLevel(node.right, level - 1)
    
    