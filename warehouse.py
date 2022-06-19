from stock import Stock, Beer, Wine, Liquor

class Warehouse:

    def __init__(self) -> None:
        # product list
        self.beerlist = []
        self.winelist = []
        self.liquorlist = []
        self.totallist = []

    def add_stock(self):
        """Assign a type to this stock"""
        category = input('Enter type of product(wine, beer or liquor):').upper()
        if category == 'BEER':           
            data = Beer()
            # there is stock of BEER
            if len(self.beerlist) > 0:
                a = 0
                for item in self.beerlist:
                    if item.name == data.name and item.location == data.location:
                        item.number += data.number
                        a = 1
                        break
                if (a != 1):
                    self.beerlist.append(data)
            # there is no stock of BEER
            else:
                self.beerlist.append(data)

        elif category == 'WINE':
            data = Wine()
            # there is stock of WINE
            if len(self.winelist) > 0:
                a = 0
                for item in self.winelist:
                    if item.name == data.name and item.location == data.location:
                        item.number += data.number
                        a = 1
                        break
                if (a != 1):
                    self.winelist.append(data)
            # there is no stock of WINE
            else:
                self.winelist.append(data)

        elif category == 'LIQUOR':
            data = Liquor()
            # there is stock of LIQUOR
            if len(self.liquorlist) > 0:
                a = 0
                for item in self.liquorlist:
                    if item.name == data.name and item.location == data.location:
                        item.number += data.number
                        a = 1
                        break
                if (a != 1):
                    self.liquorlist.append(data)
            # there is no stock of LIQUOR
            else:
                self.liquorlist.append(data)
            
        else:
            print ('Please enter the right type') 


    def remove_stock(self):
        self.total_list = self.beerlist + self.winelist + self.liquorlist
        a = 0
        data = Stock()
        for item in self.total_list:
            if item.name == data.name and item.location == data.location:
                a = 1
                if item.number >= data.number:
                    item.number -= data.number
                    print ("Name: {0} | Rest of number: {1} | Warehouse: {2}".format(item.name, item.number, item.location))
                else:
                    print ("Name: {0} | Rest of number: {1} | Warehouse: {2}".format(item.name, item.number, item.location))
                    print ("There is no enough product to remove.")        
        if a != 1:
            print("There is no stock for this product!")

    def number_type(self):
        category = input('Enter type of product(wine, beer or liquor):').upper()
        if category == 'BEER':
            type_list = self.beerlist
        elif category == 'WINE':
            type_list = self.winelist
        elif category == 'LIQUOR':
            type_list = self.liquorlist

        number = 0
        for item in type_list:
            number += item.number
        print("The number of {0} is {1}".format(category, number))

    def search(self):
        self.total_list = self.beerlist + self.winelist + self.liquorlist
        a = 0
        self.name = input('Enter product name:').lower()
        for item in self.total_list:
            if item.name == self.name:
                a = 1
                print ("Name: {0} | Rest of number: {1} | Warehouse: {2}".format(item.name, item.number, item.location))                      
        if a != 1:
            print("There is no stock for this product!")

    def get_report(self):
        na = 0
        nb = 0
        print ("For BEER")
        for item in self.beerlist:
            if item.location == "A":
                na += item.number
            else:
                nb += item.number            
            print ("Name: {0} | Number: {1}".format(item.name, item.number))

        print ("For WINE")
        for item in self.winelist:
            if item.location == "A":
                na += item.number
            else:
                nb += item.number            
            print ("Name: {0} | Number: {1}".format(item.name, item.number))
        
        print ("For LIQUOR")
        for item in self.liquorlist:
            if item.location == "A":
                na += item.number
            else:
                nb += item.number            
            print ("Name: {0} | Number: {1}".format(item.name, item.number))
        print ("There are {0} produts in warehouse A, {1} products in warehouse B, in total {2} products".format(na, nb, (na+nb)))
