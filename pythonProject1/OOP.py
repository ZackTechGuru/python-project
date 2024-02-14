class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
    def onyesha(self):
        print(f"My favorite Fruit is {self.name}" 
              f" and they goes for Ksh {self.price} a piece" 
              f" and they are {self.color} in color.")
myobj = Fruits("Oranges", 50, "Yellow")
myobj.onyesha()
myobj2 = Fruits("Apples", 30, "Green")
myobj2.onyesha()

