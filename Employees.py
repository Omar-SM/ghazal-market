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
            return self.searchEmployee(name, node.left)
        
        else:
            return self.searchEmployee(name, node.right)
            
    def addEmployee(self, node : EmployeeNode, name : str, position : str, age : int, salary : float):
        name = name.lower()

        if not self.root:
            newEmployee = EmployeeNode(name, position, age, salary)
            self.root = newEmployee
            print(f"{name} is added to the root")
            return self.root
        
        if not node:
            newEmployee = EmployeeNode(name, position, age, salary)
            return newEmployee
        
        if name == node.info["name"]:
            print(f"{name} is part of the staff")
        
        elif name < node.info["name"]:
            node.left = self.addEmployee(node.left, name, position, age, salary)

        else:
            node.right = self.addEmployee(node.right, name, position, age, salary)
        return node

    def deleteEmployee(self, name : str, node : EmployeeNode):
        name = name.lower()

        if not node:
            return None
        
        if name < node.info["name"]:
            node.left = self.deleteEmployee(name, node.left)
            return node
        
        elif name > node.info["name"]:
            node.right = self.deleteEmployee(name, node.right)
            return node
        
        else:
            if node.left == None and node.right == None:
                return None
            
            elif node.left == None:
                return node.right
            
            elif node.right == None:
                return node.left
            
            else:
                replacement = self.findSmallest(node.right)
                node.info['name'] = replacement['name']
                node.right = self.deleteEmployee(replacement['name'], node.right)
                return node
        
    def findSmallest(self, node : EmployeeNode):
        if node.left == None:
            return node.info
        
        else:
            return self.findSmallest(node.left)
        

    def alterEmployee(self, name : str, position : str, age : int, salary : float):
            employee = self.searchEmployee(name, self.root)
            if employee:
                employee.info = {
                    "name" : name,
                    "position" : position,
                    "age" : age,
                    "salary" : salary
                }
                return employee
            else:
                print(f"{name} not found")
                return

    def height(self, node) -> int:
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
            print(f"name: {node.info['name']}, position: {node.info['position']}, age: {node.info['age']}, salary: {node.info['salary']}.")
            return
        
        else:
            self.printNodesOnLevel(node.left, level - 1)
            self.printNodesOnLevel(node.right, level - 1)
    
    