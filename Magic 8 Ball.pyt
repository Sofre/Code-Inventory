#https://github.com/Sofre/RAND-CODE/tree/main - GitHub

import time
#   Imported time class for run-time manipulation --> #time
import random
#   Imported random class for random generatior functions --> #random
import sys
#   Imported system function for system manipulation functions --> #sys


#   The main function of the game
#   Random function --> consists of callbacks and a anwser 
def Random(anwsers):
   loading_bar(50)
   print()
   print(anwsers[random.randint(0,len(anwsers)-1)])
   
     
#   A loading bar -->  For the Random() function is called
def loading_bar(points):
  for counter_points in range(points+1):
    percent  = (counter_points/points)   * 100
    bar = 'X' * counter_points + '-'*(points-counter_points)
    sys.stdout.write(f'\r Loading: |{bar}| {percent:.2f}%')
    sys.stdout.flush()
    time.sleep(0.1)

#   Animation for the starting logo --> Uses a counter to print each character in a timed fashion
def animation(words):
 for counter in words:
    #time.sleep(1)
    print(counter)

    
    
#   Replay function --> For the replay option
def replay():
    anwser=input("Would you like to try again?")
    match anwser:
       case 'yes':
          return main()
       case 'no':
           print(" Goodbye, Thank you for playing ")
           exit 
          
    
          


#   Animation words --> consists of characters for the animation function
animation_words = ("M","A","G","I","C","  ","8","  ","B","A","L","L")
magic_8_ball_art = r"""
        _____  
      .'     '.  
     /  _   _  \ 
    |  (o) (o)  | 
    |     (_)   | 
    |  \_____/  | 
     \         /  
      '._____.'
"""



#   Random anwsers --> random anwsers for the game
random_anwsers = (
"A change in the wind will bring unexpected joy to your life.",

"The stars align for a new adventure—embrace the unknown!",

"An old friend will re-enter your life, bringing wisdom and laughter.",

"Your intuition is a powerful guide; trust it to lead you to success.",

"A surprise opportunity will present itself—be ready to seize it!",

"Harmony is on the horizon; nurture your relationships for peace.",

"Financial growth is in your future; stay open to new ventures.",

"Creativity will flow through you—capture your ideas before they escape!",

"A small act of kindness will lead to big rewards; don't underestimate it.",

"The universe whispers that you are exactly where you need to be.",

"Be cautious of distractions; focus on what truly matters.",

"A secret talent will emerge—explore new hobbies to uncover it!",

"A travel opportunity will soon knock on your door; pack your bags!",

"Your past experiences will serve as a foundation for future growth.",

"A piece of wisdom from a mentor will illuminate your path ahead.",

"Love is in the air; an unexpected romance may blossom.",

"Embrace change; it will lead you to new horizons.",

"Your dreams hold the key to your desires—pay attention to them.",

"A decision looms on the horizon; trust your heart to guide you.",

"Joyful moments await you; take time to savor the little things.",
)


#   Main
def main():
  user = input("Hello,   ask me a question and i shall anwser! ")
  print()
  time.sleep(1)
  Random(random_anwsers)
  replay()




#   LoadUp Animation 
animation(animation_words)
print(magic_8_ball_art)
time.sleep(2)
print()
#   Main Non-Linear Compile
main()



   


      

