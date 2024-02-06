import csv 



class Item: 
    pay_rate = 0.8 
    all = []
    def __init__(self,name: str,price: float,quantity: int): #Attributes
        print(f"An instance created: {name}")
        assert price >= 0, f"Error: Price {price} is not greater than zero!" 
        assert quantity >=0,f"Error: Quantity {quantity} is not greater than zero!" 

        #ASSIGN SELF TO OBJECT
        self.name = name
        self.price = price 
        self.quantity = quantity

    
        # Actions to execute
        Item.all.append(self) #This is to add an instance to the list of all instances 

    def calculate_total_price(self):
        return self.price*self.quantity
    
    #Method to apply dicount
    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    @classmethod #Now this method below will be a class method not an instance/object method 
    def instantiate_from_csv(cls): #Class Method
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            ) 

    def __repr__(self): #To list all instance in a more friendly way that print(Item.all)
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

           
        6

Item.instantiate_from_csv()
