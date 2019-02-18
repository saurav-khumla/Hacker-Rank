import random
ran=random.randint(1,5)
print('secret number in between 1 to 5')
for guess in range  (1,10):
   print('guess the number')
   guessNo=int(input())
   if (guessNo>ran):
       print('guess is to high')
   elif(guessNo<ran):
       print('guess is to short')
   else:
       break
if(guessNo==ran):
 print('you guess my number after '+str(guess)+' guesses')
else:
    print('Nope! my number is '+str(ran))
