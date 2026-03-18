class Item:
    def __init__(self,Name, Number,Best_Before_Date=0,Manufacturing_Date=0,Shelf_Life=0):
        self.Name = Name
        self.Number = Number
        self.ManufacturingDate = Manufacturing_Date
        self.BestBeforeDate = Best_Before_Date
        self.Shelf_Life = Shelf_Life


# 要把对象属性存储在dict里
class Fruit(Item):
    pass

class Drink(Item):
    pass