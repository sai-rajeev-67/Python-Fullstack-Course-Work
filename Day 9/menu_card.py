products=[['Laptop',56000],
         ['Mobile',20000],
         ['Charger',150],
         ['Mouse', 600],
         ['Earbuds',2500]
       ]
def view_prod():
    print("ProductName".ljust(15, " "), "Price")
    for i in products:
        print(i[0].ljust(15, " "), i[1])
def add_prod():
    product_name=input("Enter Product Name:")
    price=int(input("Enter Price:")

def del_prod():
    product_id=input("Enter Product Id:")
    print(f"{products[product_id] is deleted")
    products.pop(product_id)
while True:
    print("----------------------MENU----------------------------")
    print("1.View Product")
    print("2.Add Product")
    print("3.Delete Product")
    print("4.Exit")
