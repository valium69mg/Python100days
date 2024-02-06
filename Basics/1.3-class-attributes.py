class Item: 
    pay_rate = 0.8 #The pay rate after 20% discount 
    def __init__(self,name: str,price: float,quantity: int): #Attributes
        print(f"An instance created: {name}")
        assert price >= 0, f"Error: Price {price} is not greater than zero!" 
        assert quantity >=0,f"Error: Quantity {quantity} is not greater than zero!" 

        #ASSIGN SELF TO OBJECT
        self.name = name
        self.price = price 
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    #Method to apply dicount
    def apply_discount(self):
        self.price = self.price * self.pay_rate #we use self to be able to apply any discount that we want per instance not just the pay_rate of the class
           
        
#Instance 1
item1= Item("Phone",100,1)
item1.total_price = item1.calculate_total_price()
print(item1.price)
#Instance 2 
item2 = Item("Laptop",1000,3)
item2.total_price = item2.calculate_total_price()
item2.apply_discount() #As we do not defined the pay_rate for this instance it will compute the results with the class pay_rate attribute
print(item2.price) 
#Instance 3
item3 = Item("TV",500,5)
item3.pay_rate = 0.7
item3.apply_discount() #We defined the pay_rate for this specific instance so it will take the attribute that we created for that instance and not the class attribute
print(item3.price)



"""
print(Item.__dict__) #All attributes for class level
print(item1.__dict__) #All attributes for instance level
"""