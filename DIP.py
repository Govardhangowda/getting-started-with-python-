class appliance:
    def on(self):
        pass
    def off(self):
        pass                

class TV(appliance):
    def on(self):
        print("Turning on the TV")
    def off(self):
        print("Turning off the TV")

class AC(appliance):
    def on(self):
        print("Turning on the AC")
    def off(self):
        print("Turning off the AC") 

class remote:
    def __init__(self, appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.on()

    def turn_off(self):
        self.appliance.off()

tv = TV()
ac = AC()   
tv_remote = remote(tv)
ac_remote = remote(ac)  
tv_remote.turn_on()  
ac_remote.turn_on()
tv_remote.turn_off()
ac_remote.turn_off()