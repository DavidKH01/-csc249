# // CSC249
# // M3HW1 - silver Attempt
# // Deqiadre Hart
# // 2/25/24

def buble_sort(arr):
    x = 0
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                x += 1
                print(f'swap count: {x}')
                print(f'swapping: {arr[j+1], arr[j]}', "\n")
    print(f'sorted: {arr}, total swaps: {x}')



my_list = []  
print("How many items would you like in your list")
list_len = int(input())
print()

for i in range(list_len):
  print("Enter a number: ")
  x = int(input())
  my_list.append(x)
print(f'unsorted: {my_list}', "\n")
        

print(f'unsorted: {my_list}') 
buble_sort(my_list)


