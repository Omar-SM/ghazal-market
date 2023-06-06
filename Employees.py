#In the class EmployeeNode we have:
#The __init__ method takes several parameters: name, position, age, and salary, with default values assigned.
#Inside the __init__ method, the instance variable self.info is initialized as a dictionary containing information about an employee. The keys of the dictionary are "name", "position", "age", and "salary"
#The left and right attributes are used to linl the node to its left and right children in the tree
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

    #searchEmployee check if the current node is None. If it is, it means that the search has reached the end of a branch without finding the desired employee, so None is returned to indicate that the employee was not found.         
#The name parameter is converted to lowercase using the lower() method. This is done to ensure case-insensitive comparison when checking the employee's name.
#The code then checks if the name of the employee stored in the info dictionary of the current node matches the name parameter. If there is a match, it means that the desired employee has been found, so the current node is returned.
#If the name does not match the current node's name, the code checks if the name parameter is lexicographically smaller than the current node's name. This comparison is done using the < operator.
#If the name parameter is smaller, it means that the desired employee might be in the left subtree of the current node. The searchEmployee method is recursively called with the name parameter and the left child node of the current node as arguments.
#If the name parameter is not smaller than the current node's name, it means that the desired employee might be in the right subtree of the current node. The searchEmployee method is recursively called with the name parameter and the right child node of the current node as arguments.
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

    #The function addEmployee checks if the node parameter is None. If it is, it means that no node has been provided, and the code assigns the root node to node. This allows the method to be called without explicitly passing the root node when initially adding an employee.        
    #Then it checks if the root node (self.root) is None. If it is, it means that the tree is empty, and the new employee will be added as the root node. The EmployeeNode is created with the provided attributes, assigned to self.root, and a message is printed indicating that the employee has been added as the root node.
    #If the root node already exists, the code checks if the name of the new employee (name) matches the name of the current node (node.info["name"]). If there is a match, it means that the employee is already part of the staff, and a message is printed to indicate that.
    #If the name does not match the current node's name, the code checks if the name parameter is lexicographically smaller than the current node's name. If it is, it means that the new employee should be added to the left subtree of the current node. The addEmployee method is recursively called on the left child node of the current node, and the returned value is assigned to node.left.
    #If the name parameter is not smaller than the current node's name, it means that the new employee should be added to the right subtree of the current node. The addEmployee method is recursively called on the right child node of the current node, and the returned value is assigned to node.right.
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

    #The code then checks if the name parameter is smaller than the name of the current node (node.info["name"]). If it is, it means that the employee to be deleted might be in the left subtree of the current node. The deleteEmployee method is recursively called on the left child node of the current node, and the returned value is assigned to node.left.
    #If the name parameter is not smaller than the name of the current node, the code checks if it is lexicographically greater. If it is, it means that the employee to be deleted might be in the right subtree of the current node. The deleteEmployee method is recursively called on the right child node of the current node, and the returned value is assigned to node.right.
    #If the name parameter is equal to the name of the current node, it means that the employee to be deleted has been found.
    #If the current node has no children (both left and right are None), it means that it is a leaf node. In this case, returning None will effectively remove the node from the tree.
    #If the current node has no left child, the right child takes its place in the tree. The method returns the right child node, effectively removing the current node from the tree.
    #If the current node has no right child, the left child takes its place in the tree. The method returns the left child node, effectively removing the current node from the tree.
    #If the current node has both left and right children, a replacement node is found by calling the findSmallest method with the right child of the current node. The findSmallest method finds the smallest node in a subtree, which will be used as a replacement for the current node.
    #The information (info) of the replacement node is assigned to the current node, effectively replacing its data with the replacement node's data.
    #The deleteEmployee method is recursively called on the right child node of the current node, passing the replacement node as the name parameter. This step is done to remove the duplicate node from the right subtree.
    #Finally, the method returns the modified current node.
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
    
    #findSmallest checks if the left child of the current node (node.left) is None. If it is, it means that the current node is the leftmost node in the subtree and therefore represents the smallest employee in that subtree. In this case, the method returns the info dictionary of the current node (node.info), which contains the attributes of the smallest employee.
    #If the left child of the current node is not None, it means that there are smaller nodes in the left subtree. The method recursively calls itself, passing the left child node (node.left) as the argument. This step is repeated until the leftmost node is reached, and then the attribute dictionary of that node is returned.  
    def findSmallest(self, node : EmployeeNode):
        if node.left == None:
            return node.info
        
        else:
            return self.findSmallest(node.left)
        

    #The method begins by calling the searchEmployee method with the name parameter and the current node (node) as arguments. The searchEmployee method is expected to return the EmployeeNode object representing the employee to be altered, if it exists in the tree.
    #If employeeNode is not None, it means that the employee to be altered has been found in the tree. In this case, the attributes of the employeeNode are updated with the new values provided in the position, age, and salary parameters. The name parameter is not updated because it serves as the unique identifier for the employee.
    #After updating the info dictionary of the employeeNode, a message is printed indicating that the employee has been successfully updated.
    #Finally, the employeeNode is returned as the result of the method.
    #If employeeNode is None, it means that the employee to be altered was not found in the tree. In this case, a message is printed indicating that the employee was not found, and None is returned.
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

    #height checks if the node parameter is None. If it is, it means that the current node is a leaf node or an empty subtree, and its height is considered to be -1. This is because the height of a leaf node is 0, and the height of an empty subtree is -1. Therefore, -1 is returned.
    #If the node is not None, the code proceeds to check if the current node has no children, i.e., both the left and right child nodes are None. In this case, it means that the current node is a leaf node, and its height is considered to be 0. Therefore, 0 is returned.
    #If the current node has children, the code recursively calls the height method on both the left and right child nodes (node.left and node.right, respectively). This step is done to determine the heights of the left and right subtrees of the current node.
    #The heights of the left and right subtrees are stored in the variables heightLeftSubtree and heightRightSubtree, respectively.
    #Next, the code compares the heights of the left and right subtrees. If the height of the left subtree (heightLeftSubtree) is greater than the height of the right subtree (heightRightSubtree), it means that the left subtree is taller. In this case, the height of the current node is considered to be the height of the left subtree plus 1. Therefore, heightLeftSubtree + 1 is returned.
    #If the height of the right subtree is greater than or equal to the height of the left subtree, it means that the right subtree is taller or they have equal heights. In this case, the height of the current node is considered to be the height of the right subtree plus 1. Therefore, heightRightSubtree + 1 is returned.
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

    #printAllEmployees checks if the node parameter is None. If it is, it means that the method was called without providing a specific starting node. In this case, the node parameter is set to the root of the tree (self.root) if it exists. This step ensures that the printing process starts from the root node.
    #If the root of the tree (self.root) is None, it means that there are no employees in the tree. In this case, a message is printed indicating that there are no employees, and the method returns.
    #The code determines the number of levels in the tree by calling the height method, passing the node parameter. The height method calculates the height of the tree, which represents the maximum number of edges in the longest path from the root to a leaf node. Adding 1 to the height gives the number of levels in the tree.
    #A loop is used to iterate over each level in the tree. The loop variable level represents the current level being processed.
    #Within the loop, the printNodesOnLevel method is called, passing the node parameter and the current level as arguments. The printNodesOnLevel method is expected to print the employee nodes at the specified level.
    #After the loop iterates over all levels, the printing process is complete.
    def printAllEmployees(self, node : EmployeeNode):
        if not node:
            node = self.root
        
        if not self.root:
            print("There are no employees.")
            return
        
        levels = self.height(node) + 1

        for level in range(levels):
            self.printNodesOnLevel(node, level)

    #printNodesOnLevel if the node parameter is None. If it is, it means that the current node is a leaf node or an empty subtree, and there are no nodes to print at this level. In this case, the method simply returns without performing any further actions.
    #If the level parameter is 0, it means that the current node is at the desired level for printing. In this case, the name of the employee, accessed through the info dictionary of the node, is printed. The name is followed by a comma and a space for formatting purposes. After printing, the method returns.
    #If the level parameter is greater than 0, it means that the desired level for printing has not been reached yet. In this case, the code recursively calls the printNodesOnLevel method on both the left and right child nodes (node.left and node.right, respectively), with the level parameter decremented by 1. This step is done to traverse down the tree and reach the desired level.
    def printNodesOnLevel(self, node : EmployeeNode, level : int): # Breadth First
        if node == None:
            return
        
        elif level == 0:
            print(node.info["name"] + ", ")
            return
        
        else:
            self.printNodesOnLevel(node.left, level - 1)
            self.printNodesOnLevel(node.right, level - 1)