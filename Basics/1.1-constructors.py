class Item: 
    def __init__(self,name,price,quantity): #This excecutes as soon as an instance of the class is created 
        print(f"An instance created: {name}")
        self.name = name
        self.price = price 
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity
        
        

item1= Item("Phone",100,5)
item1.total_price = item1.calculate_total_price()

item2 = Item("Laptop",1000,3)
item2.total_price = item2.calculate_total_price()
