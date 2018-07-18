#so the whole idea behind this is that the dice roller understands the basic Dice notation
#i.e. (*n)d(*n) where n is a integer
#and follows basic bedmass notation after evaluating the rolls
#i.e. 2d6 + 2 evaluates the two rolls of d6 and then adds two to the final 

from random import randrange

def parsedie(dicenotation):
    parsed = dicenotation.split('d')
    return parsed

def rolldice(dicenotation):
    rolls = []
    for _ in range(int(parsedie(dicenotation)[0])):
        rolls.append(randrange(1,int(parsedie(dicenotation)[1])+1))
    return rolls

while True:
    dicenotation = input('>')
    if dicenotation == "exit":
        break
    else:
        try:
            print(rolldice(dicenotation))
        except Exception as e:
            print(e)