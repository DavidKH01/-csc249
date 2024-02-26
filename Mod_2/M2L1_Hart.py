my_nums = [1,10,11,7,2,22,6,60]

max_val = my_nums[0] 

for x in range(len(my_nums)):
  if my_nums[x] > max_val:
    max_val = my_nums[x]
print(max_val)
