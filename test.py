from warehouse import Warehouse
from stock import Stock, Beer, Wine, Liquor

w = Warehouse()
w.add_stock()
# add 3 estrella to A 
w.add_stock()
# add 2 estrella to B

w.get_report()

w.remove_stock()
# remove 2 estrella from A
w.remove_stock()
# remove 5 estrella from A
w.remove_stock()
# remove cider from A
w.remove_stock()
# remove 2 estrella from B

w.number_type()
# type BEER
w.number_type()
# type WINE

w.search()
# estrella
w.search()
# cider

w.add_stock()
# add 2 estrella to B
w.search()
# estrella