
"""

We want to sort the array

[1,2,3,4,5]


arr = [5,4,3,2,1]
flip(arr)

1,2,3,4,5

2,3,4,5,1



Steps

Find the largest element, put it at position 0
Call flip(arr, pos)



arr = [2,4,3,5,1]

5 is at pos 4
flip(arr,pos = 4)

Put 5 in the right place
flip(arr, pos = 5)




O(N * (N+N) )  O(N^2)

O(1)

"""

def pancake_sort(arr):

  # O(N)
  for i in range(len(arr)-1,-1,-1):

    #i is where we want to put the max number
    max_value,max_position = find_max_val_and_pos(arr,i)

    if arr[i] != max_value:
      flip(arr, max_position)
      flip(arr, i)

  return arr

def flip(arr,k):
  #we flip the array in place up to position K
  
  for i in range((k+1)//2):

    arr[i], arr[k-i] = arr[k-i], arr[i]

def find_max_val_and_pos(arr,i):
  
  max_value = -1
  max_position = -1
  # O(N)

  for j in range(0,i+1):
    #j is the index to find the max number
    if max_value < arr[j]:
      max_value = arr[j]
      max_position = j

  return [max_value,max_position]
