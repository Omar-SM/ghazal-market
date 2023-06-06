from Employees import Employee
from Inventory import Category, Brand, Product, SalesLog
import csv, re

employees = Employee()
categories = Category()
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
                                
                                with open(fileName, 'r') as employeesFile:
                                    csvReader = csv.reader(employeesFile)
                                    csvReader.__next__()

                                    for column in csvReader:
                                        employees.addEmployee(
                                            employees.root,
                                            column[0],
                                            column[1],
                                            column[2],
                                            column[3]
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

                            if deletedEmployee:
                                print(f"{deletedEmployee.info['name']} is deleted")
                                continue
                            
                            print("Employee not found!")
                            continue
                        
                        case 4:
                            print("Enter the data you want to change")
                            employeeInfo = getEmployeeInfo()

                            alteredEmployee = employees.alterEmployee(
                                employeeInfo["name"],
                                employeeInfo["position"],
                                employeeInfo["age"],
                                employeeInfo["salary"]
                            )

                            if alteredEmployee:
                                print(f"{alteredEmployee.info['name']} is altered. Position: {alteredEmployee.info['position']}, age: {alteredEmployee.info['age']}, salary: {alteredEmployee.info['salary']}.")
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
                                
                                with open(fileName, 'r') as productsFile:
                                    csvReader = csv.reader(productsFile)
                                    csvReader.__next__()

                                    for product in csvReader:
                                        categoryNode = categories.searchCategory(categories.root, product[1])
                                        brandNode = None
                                        product = None

                                        if not categoryNode:
                                            categoryNode = categories.addCategory(categories.root, product[1])

                                        else:
                                            brandNode = categoryNode.brand_head.searchBrand(product[2])
                                            if not brandNode:
                                                brandNode = categoryNode.brand_head.addBrand(product[2])
                                    
                                        product = brandNode.product_head.addProduct(
                                            productName=product[0],
                                            categoryName=product[1],
                                            brandName=product[2],
                                            price=product[3],
                                            quantity=product[4]
                                        )

                                    productsFile.close()
                                    print(f"All products are successfully added!")
                                    continue
                                
                            elif option4 == 2:
                                products = getProductInfo()

                                categoryNode = categories.searchCategory(categories.root, products["category"])
                                brandNode = None
                                product = None

                                if not categoryNode:
                                    categoryNode = categories.addCategory(categories.root, products["category"])
                                    print(f"{categoryNode.name} added")

                                if categoryNode.brand_head:
                                    brandNode = categoryNode.brand_head.searchBrand(products["brand"])
                                    if not brandNode:
                                        brandNode = categoryNode.brand_head.addBrand(products["brand"])
                                        print(f"{brandNode.name} added")

                                else:
                                    brand = categoryNode.brand_head = Brand()
                                    brandNode = brand.addBrand(products["brand"])
                        
                                product = brandNode.product_head.addProduct(
                                    productName=products["name"],
                                    categoryName=products["category"],
                                    brandName=products["brand"],
                                    price=products["price"],
                                    quantity=products["quantity"]
                                )

                                if product:
                                    print(f"{product['name']} is added")

                                else:
                                    print(f"There has been a problem adding this product")

                        case 2:
                            prodName = input(f"Enter product Name: ")
                            brandName = input(f"Enter {prodName}'s brand: ")
                            catgName = input(f"Enter {prodName}'s category: ")
                            categorySearchResults = categories.searchCategory(categories.root, catgName) 
                            if categorySearchResults:
                                brandSearchResults = categorySearchResults.brand_head.searchBrand(brandName)
                                if brandSearchResults:
                                    productSearhResults = brandSearchResults.product_head.searchProduct(prodName)
                                    if productSearhResults:
                                        print(f"Product has been found.")
                                        continue
                                    print(f"Product doesn't exists in this brand.")
                                    continue
                                print(f"Brand doesn't exists in this category.")
                                continue
                            print(f"Category doesn't exists.")
                            continue    

                        case 3:
                            pass

                        case 4:
                            categories.levelOrderTraversal(categories.root)
                            continue

                        case 5:
                            catgName = input("Enter Category Name: ")
                            categorySearchResults = categories.searchCategory(categories.root, catgName)
                            if categorySearchResults:
                                brands = categorySearchResults.brand_head
                                brands.printBrands()
                            else:
                                print(f"Category doesn't exist.")
                            continue

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
            print(err)
            continue

def getProductInfo() -> dict:
    try:
        name = input("Product's Name: ")
        category = input(f"{name}'s Category: ")
        brand = input(f"{name}'s Brand: ")
        price = float(input(f"{name}'s Price: "))
        quantity = int(input(f"Quantity of {name}: "))

    except (TypeError) as err:
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