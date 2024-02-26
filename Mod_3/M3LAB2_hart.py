def merge (arr,ll,rr):
  i,j,k = 0,0,0
  len_l = len(ll)
  len_r = len(rr)

  while i < len_l and j < len_r:
    if ll[i] <= rr[j]:
      arr[k] = ll[i]
      k+=1
      i+=1
    else:
      arr[k] = rr[j]
      k+=1
      j+=1

  while i < len_l:
    arr[k] = ll[i]
    k+=1
    i+=1

  while j < len_r:
    arr[k] = rr[j]
    k+=1
    j+=1

  





def merge_sort(my_arr):
  a = len(my_arr)
  if a < 2:
    return my_arr
  mid = a//2
  arr_l = my_arr[0:mid]
  arr_2 = my_arr[mid:]

  merge_sort(arr_l)
  merge_sort(arr_2)
  merge(my_arr, arr_l,arr_2)
  




a_list = []  
print("How many items would you like in your list")
list_len = int(input())
print()

for i in range(list_len):
  print("Enter a number: ")
  x = int(input())
  a_list.append(x)

merge_sort(a_list)
print(a_list)
