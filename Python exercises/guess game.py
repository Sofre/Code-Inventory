
import random
import math

def close(guess_num,guessed_num):
   value = math.isclose(guess_num,guessed_num,rel_tol=0.5,abs_tol=0.4)
   return value


secret_number = random.randint(1,100)
looper = True
print(secret_number)


while(looper):
    x = input("Keep guessing!  ")
    guess = int (x) 
    if(guess == secret_number):
        print("You have guessed it! ")
        break
    if(close(guess,secret_number)==True):
        print("You are close")
        continue
    else:
        continue


     

      