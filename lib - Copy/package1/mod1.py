import time
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def detail(self):
        return f"Name: {self.name}, score: {self.score}"
 
def timing():
    while True:
        time1 = time.strftime("%I:%M:%S:%p")
        print(time1,end="\r",flush = True)
        time.sleep(1)