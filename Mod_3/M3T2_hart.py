def insertion_sort(numbers):
    x = 1
    for i in range(1, len(numbers)):
        j = i

        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        print(f'pass: {x}, where pointers are at {numbers[j-1]},{numbers[j]}')
        x+=1
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            print(f'swaping: {numbers[j]}, and {numbers[j-1]}')
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j -= 1
            print(numbers)
            
    
# Create a list of unsorted values    
counter = 0
numbers = []
print('please enter numbers into the list')
while counter < 8:
  user_input = int(input())
  numbers.append(user_input)
  counter += 1

# Print unsorted list
print('UNSORTED:', numbers)

# Call the insertion_sort function
insertion_sort(numbers)

# Print sorted list
print('SORTED:', numbers)