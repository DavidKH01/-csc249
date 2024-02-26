def playGame ():

  print (""" 
  Which game would you like to play
  1.Prime-Time
  2.Double or nothing
  3.Guess my hand
  4.Exit         
         """)
  
  user_input = input()

  if user_input == "1":
    prime_time()
  elif user_input == "2":
    print("Sorry, under Development")
    input('Press ENTER to exit')
  elif user_input == "3":
    print("Sorry, under development")
    input('Press ENTER to exit')
  elif user_input == "4":
    print("Game over")
    input('Press ENTER to exit')
  else:
    print("Please enter a valid option")
    playGame()



def prime_time():
    used_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    counter = 0

    print("There are 25 prime numbers between 0 and 100 not including 0.")
    print("Objective: List 7 prime numbers between 0 to 100 to win")

    while counter < 7:
        prime_input = int(input("Enter a prime number: "))
        print(prime_input)

        if prime_input not in used_numbers:
            print("Game Over")
            input('Press ENTER to exit')
            return
        else:
            counter += 1
            used_numbers.remove(prime_input)

    print("You Won")
    input('Press ENTER to exit')


playGame()


