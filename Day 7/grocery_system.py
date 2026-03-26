items={"Rice": 60, "Wheat Flour":45,"Sugar":40,"Milk":25,"Eggs(12 pcs)":70,"Cooking Oil":130,"Tea Powder":90,"Salt":20,"Bread":30,"Soap":25}
print("---Welcome to grocery store---")

print("Here are the available products")
index= 1
print("Index\t  Product \t  Price(in rs)")
for i in items:
      print(index,"\t",i, "\t\t", items[i])
      index = index+1
     
