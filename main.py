from Employees import Employee
from Inventory import Category, Brand, Product, SalesLog
import csv, re

employees = Employee()
categories = Category()
brands = Brand()
products = Product()
salesLog = SalesLog()

def main():
    while True:
        print(f"Enter the number of the option you choose. -1 to return, 0 to exit the code")
        print(f"1. Employee")
        print(f"2. Product Inventory")
        try:
            option1 = int(input("-> ").strip())
            if option1 == 1:
                while True:
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

                                # if re.search(".+\.csv", fileName):
                                #     print("The file is either not a valid file name or it is not a csv file.")
                                #     return
                                
                                with open(fileName, 'r') as employeesFile:
                                    csvReader = csv.DictReader(employeesFile, delimiter=',')

                                    for column in csvReader:
                                        employees.addEmployee(
                                            employees.root,
                                            column['name'],
                                            column['position'],
                                            column['age'],
                                            column['salary']
                                        )

                                    employeesFile.close()
                                    print("All Employees are uploaded successfully")
                                    continue

                            elif option4 == 2:
                                employeeInfo = getEmployeeInfo()

                                employees.addEmployee(
                                    employees.root,
                                    employeeInfo['name'],
                                    employeeInfo['position'],
                                    employeeInfo['age'],
                                    employeeInfo['salary']
                                )

                                print(f"{employeeInfo['name']} is added successfully")
                                continue

                            else:
                                print(f"There is no option such as {option4}")
                                continue

                        case 2:
                            name = input("Employee's name: ")

                            employee = employees.searchEmployee(name, employees.root)

                            if employee:
                                print(f"{employee.info['name']} has been found")
                            else:
                                print("Employee Not Found")
                            continue
                        
                        case 3:
                            name = input("Employee's name to delete: ")
                            deletedEmployee = employees.deleteEmployee(name, employees.root)
                            print(f"{deletedEmployee.info['name']} is deleted")
                            continue
                        
                        case 4:
                            print("Enter the data you want to change")
                            employeeInfo = getEmployeeInfo()

                            alteredEmployee = employees.alterEmployee(
                                employees.root,
                                employeeInfo["name"],
                                employeeInfo["position"],
                                employeeInfo["age"],
                                employeeInfo["salary"]
                            )

                            if alteredEmployee:
                                print(f"{alteredEmployee['name']} is altered")
                            else:
                                print("Employee not found")
                            continue
                        
                        case 5:
                            employees.printAllEmployees(employees.root)
                            continue
                        
                        case -1:
                            break

                        case 0:
                            exit(0)

                        case default:
                            print(f"There is no such option as {option2}. Try again")
                            continue

            elif option1 == 2:
                while True:
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

                                # if re.search(".+\.csv", fileName):
                                #     print("The file is either not a valid file name or it is not a csv file.")
                                #     return
                                
                                with open(fileName, 'r') as productsFile:
                                    csvReader = csv.DictReader(productsFile)

                                    for column in csvReader:
                                        products.addProduct(
                                            column['name'], 
                                            categories,
                                            column['category'], 
                                            brands,
                                            column['brand'], 
                                            float(column['price']), 
                                            int(column['quantity'])
                                        )

                                productsFile.close()
                                print(f"Products added successfully")
                                continue
                                
                            elif option4 == 2:
                                
                                productInfo = getProductInfo()

                                products.addProduct(
                                        productInfo['name'], 
                                        categories,
                                        productInfo['category'], 
                                        brands,
                                        productInfo['brand'], 
                                        float(productInfo['price']), 
                                        int(productInfo['quantity'])
                                    )
                                
                                print(f"{productInfo['name']} added successfully")
                                continue

                            else:
                                print(f"There is no option {option4}. Try again!")
                                continue
                        case 2:
                            productInfo = getProductInfo()

                            product = products.searchProduct(
                                productInfo["name"],
                                categories,
                                productInfo["category"],
                                brands,
                                productInfo["brand"],
                            )

                            if product:
                                print(f"Product {product.data['name']} found")
                            else:
                                print("Product hasn't been found.")
                            continue

                        case 3:
                            name = input("Product's Name: ")
                            category = input(f"{name}'s Category: ")
                            brand = input(f"{name}'s Brand: ")
                            quantity = int(input(f"Quantity to sell: {name}"))

                            product = products.sellProduct(
                                    categories,
                                    category,
                                    brands,
                                    brand,
                                    name,
                                    quantity,
                                    salesLog
                                )

                            if product:
                                print(f"{productInfo['name']} sold successfully")
                                print(f"Sale Receipt: {salesLog.getRear()}")
                            else:
                                print("Product hasn't been found.")
                            continue
                        
                        case 4:
                            categories.levelOrderTraversal(categories.root)
                            continue

                        case 5:
                            category = input("Category Name: ")
                            categorySelected = categories.searchCategory(categories.root, category.strip())
                            if categorySelected:
                                brandsList = categorySelected.brand_head
                                brandsList.printBrands()
                                continue
                            print("There is no such Category")

                        case -1:
                            break

                        case 0:
                            exit(0)
                            
                        case default:
                            print(f"There is no option {option3}. Try again")
                            continue
                    
            elif option1 == 0:
                exit(0)

            else:
                continue

        except (TypeError) as err:
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