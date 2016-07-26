for i in range(20):
            number=37
            guess=int(raw_input ('pick a number between 1 and 1000'))
            if number==guess:
                print  'YAY YOU WIN'
                break
            else:
                if guess > number :
                    print 'guess a lower number'
                else:
                    print 'guess a higher number'
                print 'guess again'
if number !=guess :                  
                 print 'sorry you lose :(   the number was '
                 print number
           
  
