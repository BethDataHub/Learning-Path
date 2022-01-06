import random
#from greeting import outro
from greeting import intro,outro

def get_your_name():
    names = ['Wiona','Hercules','Andor','Rogue','Gibson','Audrey','Waggs','Ollo','Tallis','Magic']
    yourName = random.choice(names)
    return yourName

yourName = get_your_name()

intro(yourName,'Beth')
outro(yourName)