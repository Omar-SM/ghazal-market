from Employees import Employee
from Inventory import Category, Brand, Product, SalesLog
import csv, re

employees = Employee()
categories = Category()
brands = Brand()
products = Product()
salesLog = SalesLog()

def main():
    print(f"Enter the number of the option you choose.")
    print(f"1. Employee")
    print(f"2. Product Inventory")
    try:
        option1 = int(input("-> ").strip())
        if option1 == 1:
            print("---------------------\n")
            print("1. Add Employee")
            print("2. Search for an Employee")
            print("3. Remove an Employee")
            print("4. Edit Employee Data")
            print("5. Print All Employees")

            option2 = int(input("-> ").strip())
            match option2:
                case 1:
                    print("1. Enter a CSV File of Employees")
                    print("2. Enter One Employee")
                    option4 = int(input("-> "))

                    if option4 == 1:
                        fileName = input("File Name or Path: ")

                        if re.search(".+\.csv", fileName):
                            print("The file is either not a valid file name or it is not a csv file.")
                            return
                        
                        with open(fileName, 'r') as employeesFile:
                            csvReader = csv.DictReader(employeesFile)

                            for column in csvReader:
                                employees.insertEmployee(
                                    column['name'],
                                    column['position'],
                                    column['age'],
                                    column['salary']
                                )

                            employeesFile.close()
                            print("All Employees are uploaded successfully")
                            return

                    elif option4 == 2:
                        employeeInfo = getEmployeeInfo()

                        employees.insertEmployee(
                            employeeInfo['name'],
                            employeeInfo['position'],
                            employeeInfo['age'],
                            employeeInfo['salary']
                        )

                        print(f"{employeeInfo['name']} is added successfully")
                        return

                    else:
                        print(f"There is no option such as {option4}")
                        return

                case 2:
                    name = input("Employee's name: ")
                    print(employees.searchEmployee(name))
                    return
                
                case 3:
                    name = input("Employee's name to delete: ")
                    deletedEmployee = employees.deleteEmployee(name)
                    print(f"{deletedEmployee.info['name']} is deleted")
                    return
                
                case 4:
                    print("Enter the data you want to change")
                    employeeInfo = getEmployeeInfo()

                    alteredEmployee = employees.alterEmployee(
                        employeeInfo["name"],
                        employeeInfo["position"],
                        employeeInfo["age"],
                        employeeInfo["salary"]
                    )
                    print(f"{employeeInfo['name']} is altered")
                    return
                
                case 5:
                    employees.printAllEmployees()
                    return 
                
                case default:
                    print(f"There is no option {option2}.")
                    return

        elif option1 == 2:
            print("---------------------\n")
            print("1. Insert Product")
            print("2. Seach for a Product")
            print("3. Sell Product")
            print("4. Print All Categories")
            print("5. Print All Brands for a Category")

            option3 = int(input("-> ").strip())
            match option3:
                case 1:
                    print("1. Enter a CSV File of Products")
                    print("2. Enter One Product")
                    option4 = int(input("-> "))

                    if option4 == 1:
                        fileName = input("File Name or Path: ")

                        if re.search(".+\.csv", fileName):
                            print("The file is either not a valid file name or it is not a csv file.")
                            return
                        
                        with open(fileName, 'r') as productsFile:
                            csvReader = csv.DictReader(productsFile)

                            for column in csvReader:
                                products.addProduct(column['name'], 
                                                    column['category'], 
                                                    column['brand'], 
                                                    float(column['price']), 
                                                    int(column['quantity'])
                                                    )

                        productsFile.close()
                        print(f"Products added successfully")
                        return
                        
                    elif option4 == 2:
                        
                        productInfo = getProductInfo()

                        products.addProduct(
                            productInfo["name"], 
                            productInfo["category"], 
                            productInfo["brand"], 
                            productInfo["price"], 
                            productInfo["quantity"]
                            )
                        
                        print(f"{productInfo['name']} added successfully")
                        return

                    else:
                        print(f"There is no option {option4}")
                        return
                case 2:
                    productInfo = getProductInfo()

                    print(products.searchProduct(
                        productInfo["name"],
                        productInfo["category"],
                        productInfo["brand"],
                        productInfo["price"],
                        productInfo["quantity"]
                    ))
                    return
                
                case 3:
                    productInfo = getProductInfo()

                    products.sell(
                        productInfo["name"],
                        productInfo["category"],
                        productInfo["brand"],
                        productInfo["quantity"]
                    )

                    print(f"{productInfo['name']} sold successfully")
                    print(f"Sale Receipt: {SalesLog.getRear()}")
                    return
                
                case 4:
                    categories.printCategories()
                    return
                case 5:
                    category = input("Category Name: ")
                    brandsList = categories.searchBST(category)
                    brandsList.trav()
                    return
                    
                case default:
                    print(f"There is no option {option3}.")
                    return

        else:
            print(f"There is no option {option1}.")
            return

    except (TypeError, Exception) as err:
        print("Unvalid input. Numbers are only excepted.")
        print(err)
        return

def getProductInfo() -> dict:
    try:
        name = input("Product's Name: ")
        category = input(f"{name}'s Category: ")
        brand = input(f"{name}'s Brand: ")
        price = float(input(f"{name}'s Price: "))
        quantity = int(input(f"Quantity of {name}"))

    except (TypeError) as err:
        print("Unvalid input. Numbers are only excepted.")
        print(err)
        return
    
    return {
        "name" : name,
        "category" : category,
        "brand" : brand,
        "price" : price,
        "quantity" : quantity
    }         

def getEmployeeInfo() -> dict:
    try:
        name = input(f"Employee's Name: ")
        position = input(f"{name}'s Position: ")
        age = int(input(f"{name}'s Age: "))
        salary = float(input(f"{name}'s Salary: "))

    except (TypeError) as err:
        print("Unvalid input. Numbers are only excepted.")
        print(err)
        return
    
    return {
        "name" : name,
        "position" : position,
        "age" : age,
        "salary" : salary
    }

if __name__ == "__main__":
    main()