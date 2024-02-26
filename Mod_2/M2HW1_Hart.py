import time

# // CSC249
# // M2HW1 - Gold Attempt
# // Deqiadre Hart
# // 2/11/24


def binary_demo():
  nums = []
  print("Please enter a total of 10 number in ascending order")

  for index in range(10):
      print(f"Please enter number index {index}")
      user_num = int(input())
      # print(type(user_num))
      nums.append(user_num)
  print()

  print("Your numbers are: ")
  print(nums, "\n")


  print("What number would you like to find: ")
  target = int(input())
  # print(type(target))

  high_idx = len(nums)-1
  low_idx = 0
  

  while low_idx <= high_idx:
    mid_idx = (high_idx + low_idx)//2
    if nums[mid_idx] == target:
      print(f'I found your number at index: {mid_idx}')
      main()
    elif nums[mid_idx] > target:
      high_idx = mid_idx - 1
      print(high_idx)
      # time.sleep(5)
    else:
      low_idx = mid_idx + 1
      print(low_idx)
      # time.sleep(5)
  print("index not found")      
  main()



def binary_GNG():
  nums = list(range(101))
  count = 0
  high_idx = len(nums)-1
  low_idx = 0
  
  print("Choose a number from 0 to 99.")
  target = input()




  while low_idx <= high_idx and count < 5:
    
    mid_idx = (high_idx + low_idx)//2
    print(f"Is your number {nums[mid_idx]}. (< , >, = )?")
    user_input = input()

    if user_input == '=':
      print(f'I found your number')
      main()
    
    elif user_input == '<':
      high_idx = mid_idx - 1
      count+=1
      # print(high_idx)
      # time.sleep(5)
    elif user_input == '>':
      low_idx = mid_idx + 1
      # print(low_idx)
      # time.sleep(5)
      count+=1
  print("index not found in time")      
  main()
   

def main ():

  print (""" 
  Which game would you like to play
  1.Binary Search Demo
  2.Binary Guess the Number Game
  3.Quit     
         """)
  
  user_input = input()

  if user_input == "1":
    binary_demo()
  elif user_input == "2":
     binary_GNG()
  elif user_input == "3":
    print("Game over")
    input('Press ENTER to exit')
  else:
    print("Please enter a valid option")
    main()




main()
