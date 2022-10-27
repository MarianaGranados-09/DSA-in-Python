# Write a Python class, Flower, that has three instance variables of #type str, int, and float, that respectively represent the name of the #flower, its number of petals, and its price. Your class must include a #constructor method that initializes each variable to an appropriate #value, and your class should include methods for setting the value of #each type, and retrieving the value of each type

class Flower:
    def __init__(self, name, numberPetals, price):
        #creates a new flower instance
        self._name = None
        self._numberPetals = None
        self._price = None

        #setters
        self.set_name(name)
        self.set_numberPetals(numberPetals)
        self.set_price(price)

    def set_name(self,name):
        try:
            self._name = str(name)
        except:
            print('Invalid input, must be a string.')

    def set_numberPetals(self, numberPetals):
        try:
            self._numberPetals = int(numberPetals)
        except:
            print('Invalid number, must be an int')
    
    def set_price(self, price):
        try:
            self._price = float(price)
        except:
            print('Invalid price, must be an float')

    #getters:
    def get_name(self):
        return self._name
    
    def get_numberPetals(self):
        return self._numberPetals

    def get_price(self):
        return self._price

tulip = Flower("Tulip", 10, 30.23)
print(tulip.get_name(), tulip.get_price())

rose = Flower('rosita', 2, 1.22)
rose.set_name('rose')
rose.set_numberPetals(20)
rose.set_price(12.43)

print(rose.get_name())
