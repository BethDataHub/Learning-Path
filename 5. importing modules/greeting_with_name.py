import random
#from greeting import outro
from greeting import intro,outro

def get_your_name():
    names = ['Wiona','Hercules','Andor','Rogue','Gibson','Audrey','Waggs','Ollo','Tallis','Magic']
    num = random.randrange(0,10)
    yourName = names[num]

    return yourName

yourName = get_your_name()

intro(yourName,'Beth')
outro(yourName)