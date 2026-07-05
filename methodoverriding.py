class shape:
    def draw(self):
        print('drawing shape')
        
class circle(shape):
    def draw(self):
        print('drawing circle')
        
crc=circle()
cs=shape()
crc.draw()
cs.draw()
