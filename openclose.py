class tax:
    def taxrate(self):
        return 0

class entertainment(tax):
    def taxrate(self):
        return 0.1
    
class food(tax):
    def taxrate(self):
        return 0.05
    
class alchol(tax):
    def taxrate(self):
        return 0.2
    
f1ticket=entertainment()
f2ticket=food()
f3ticket=alchol()
print(f1ticket.taxrate())
print(f2ticket.taxrate())
print(f3ticket.taxrate())
