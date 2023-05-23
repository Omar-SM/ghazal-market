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

    # TO DO
    # It should take only the employee's name
    # If found it should return the node
    # The naming should be camelCase
    def search_employee(self, node, name):
        if node == None:
            return False
        
        else:
            if node.data == name:
                return True
            
            elif name < node.data:
                return self.search(node.left, name)
            
            else:
                return self.search(node.right, name)
    # Naming should be camelCase
    def insert_employee(self, node, data, name):
        if node == "root":
            newNode = EmployeeNode(data)
            self.root = newNode
            return name + "is added"
        
        elif node == None:
            newNode = EmployeeNode(data)
            return newNode
        
        else:
            if data == node.data:
                return name + "is part of the staff"
            
            elif data < node.data:
                node.left = self.insert(node.left, data)

            else:
                node.right = self.insert(node.right, data)
        
        return node

    # Naming should be camelCase
    def delete_employee(self, node, name):
        if node == None:
            return name + "is not part of the staff"
        
        else:
            if name < node.data:
                node.left = self.delete(node.left, name)
                return node
            
            elif name > node.data:
                node.right = self.delete(node.right, name)
                return node
            
            else:
                if node.left == None and node.right == None:
                    return None
                
                if node.left == None:
                    return node.right
                
                if node.right == None:
                    return node.left
                
                replacement = self.findSmallest(node.right)
                node.data = replacement
                node.right = self.delete(node.right, replacement)
                return node
        
    def findSmallest(self, node):
        if node.left == None:
            return node.data
        
        else:
            return self.findSmallest(node.left)
        
    def alterEmployee(self):
        # TO DO
        # It takes the employee's name to change their data
        # It takes as well the name to be changed to in case, position, age, and salary
        # They should be optional
        # Returns the edited employee node
        pass

    def printAllEmployees(self):
        # TO DO
        # It prints all Employee's name in a well formated way
        pass