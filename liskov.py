class vehicle:
    def start_engine(self):
        pass
class bike(vehicle):
    def start_engine(self):
        print("kick start the bike engine")

class boat(vehicle):
    def start_engine(self):
        print("pull the cord to start the boat engine")

ktm=bike()
ktm.start_engine()
yamaha=boat()
yamaha.start_engine()