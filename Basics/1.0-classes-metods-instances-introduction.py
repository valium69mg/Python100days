class Item: 
    def calculate_total_price(self,x,y):
        return x*y
        
        

item1= Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
item1.total_price = item1.calculate_total_price(item1.price,item1.quantity)

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
item2.total_price = item2.calculate_total_price(item2.price,item2.quantity)



print("El precio total del item1: {}".format(item1.total_price))
print("El precio total del item2 es: {}".format(item2.total_price))

