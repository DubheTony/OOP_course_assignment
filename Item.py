class Item:
    def __init__(self,Name, Number,Best_Before_Date=0,Manufacturing_Date=0,Shelf_Life=0):
        self.Name = Name
        self.Number = Number
        self.ManufacturingDate = Manufacturing_Date
        self.BestBeforeDate = Best_Before_Date
        self.Shelf_Life = Shelf_Life