class Item: 
    def __init__(self,name: str,price: float,quantity: int): #name: str <--- means it has to be a str
        print(f"An instance created: {name}")
        #ASSERT STATEMENTS: USED TO CHECK IF THE VARIABLES MEET UR EXPECTATIONS
        #FOR THIS EXAMPLE IT IS USED TO VALIDATE THAT PRICE AND QUANTITY ARE >= TO ZERO 
        assert price >= 0, f"Error: Price {price} is not greater than zero!" #This error will pop out if you put a price below zero
        assert quantity >=0,f"Error: Quantity {quantity} is not greater than zero!" #This error will pop out if you put a quantity below zero 

        #ASSIGN SELF TO OBJECT
        self.name = name
        self.price = price 
        self.quantity = quantity
        


    def calculate_total_price(self):
        return self.price*self.quantity
        
        

item1= Item("Phone",100,1)
item1.total_price = item1.calculate_total_price()

item2 = Item("Laptop",1000,3)
item2.total_price = item2.calculate_total_price()
