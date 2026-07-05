class vehicle:
    def start(self):
        print('The vehicle is starting')
        
class bike(vehicle):
    def ride(self):
        print('the vehicle is now going on')
        
honda=bike()
honda.start()
honda.ride()
