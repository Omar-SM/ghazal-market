class Employee:
    def __init__(self, name, position, age, salary):
        self.name = name.lower()
        self.position = position
        self.age = age
        self.salary = salary

class Node:
    def __init__(self, employee):
        self.employee = employee
        self.left = None
        self.right = None

class EmployeeBST:
    def __init__(self):
        self.root = None

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
        
def insert_employee(self, node, data, name):
    if node == "root":
        newNode = Node(data)
        self.root = newNode
        return name + "is added"
    
    elif node == None:
        newNode = Node(data)
        return newNode
    
    else:
        if data == node.data:
            return name + "is part of the staff"
        
        elif data < node.data:
            node.left = self.insert(node.left, data)

        else:
            node.right = self.insert(node.right, data)
    
    return node

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

