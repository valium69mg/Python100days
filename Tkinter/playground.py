def add(*args):
    add = 0
    for n in args:
        add+=n
    return add

#Keyword args
def calculate(**kwargs):
    if (kwargs["add"]):
        addition_args = kwargs["add"]
        addition = 0
        for n in addition_args:
            addition+=n
        return addition
    return 0

addition = calculate(add=(3,5,2))

class Car:
    def __init__(self,**kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="nissan",model="GTR")

