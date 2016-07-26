import random

for i in range(20):
        a = random.randint(30,40);
        number = 37
        if a==number:
                print  'YAY YOU WIN'
                break
        else:
                if number >a :
                    print 'guess a lower number'
                else:
                    print 'guess a higher number'
                print 'guess again'
if number !=a :                  
                 print 'sorry you lose :(   the number was '
                 print number
