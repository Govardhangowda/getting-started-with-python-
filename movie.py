class movies:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
        
    def displayinfo(self):
        print(f'The Movie is :{self.title} and  rating is {self.rating}')
        
mv1=movies('the dictator','4.5')
mv2=movies('the social network','4.8')
mv1.displayinfo()
mv2.displayinfo()
        
