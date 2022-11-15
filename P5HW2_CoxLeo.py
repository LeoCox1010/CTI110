# CTI 110
# P5HW - Math Quiz 
# Leo Cox
# 11/15/22

import random

def get_random_number():
  #CHANGE TO 100!!
  roll = random.randint(1, 100)
  return roll


def add_numbers():
  print("Add two numbers")
  first = get_random_number()
  second = get_random_number()
  print(first, "+", second, "= ?")
  guess = 999
  answer = first + second

  count = 0
  
  while guess != answer: 
    guess=(int(input()))
    count+=1
    if guess > answer:
        print("That's too high.") 
    elif guess < answer:
        print("That's too low.")
    else:
        
    
      if guess == answer:
        print("Correct!")
        print("You got it in", count, "guesses")
      else:
        print("Incorrect.")
    


    #repeat until correct

def subtract_numbers():
  print("Subtract numbers")
  first = get_random_number()
  second = get_random_number()
  print(first, "-", second, "= ?")
  guess = 999
  answer = first - second

  count=0
  
  while guess != answer:
    guess=int(input())
    count+=1
    if guess > answer:
        print("That's too high.") 
    elif guess < answer:
        print("That's too low.")
    else:
      
        if guess == answer:
          print("Correct!")
          print("You got it in", count, "guesses")
        else:
          print("Incorrect.")


def main():
  #menu goes here
  keepGoing = True
  while keepGoing:
    print("Main Menu")
    print("-"*20)
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Quit")
    print("Please choose an option.")
    choice = int(input())
    if choice == 1:
      add_numbers()
    elif choice == 2:
      subtract_numbers()
    elif choice == 3: 
      keepGoing = False
      print("Bye!")
    else:
      print("Please choose 1, 2, or 3.")








#start program
main()