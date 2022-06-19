
class Stock:
    def __init__(self) -> None:
        '''Identify the name, quantity, and in which warehouse the general stock stays'''
        self.name = input('Enter product name:').lower()
        a = int(input('Enter quantity:'))
        assert a > 0, "Please enter the right number"
        self.number = a
        b = input('In which warehouse it stays? Warehouse A or B? Enter "A" or "B":').upper()
        assert b in ['A','B'], "Please enter the right letter"
        self.location = b
    

# All these classes inherite all the attributes from Stock
# Define three types: Beer, Wine, Liquor 
class Beer(Stock):
    def __init__(self) -> None:
        super().__init__()
        self.types = 'BEER'

class Wine(Stock):
    def __init__(self) -> None:
        super().__init__()
        self.types = 'WINE'

class Liquor(Stock):
    def __init__(self) -> None:
        super().__init__()
        self.types = 'LIQUOR'






