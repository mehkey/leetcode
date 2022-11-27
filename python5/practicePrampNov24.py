"""

Input:  shiftArr of size N

Find the positon

Dumb the Linear search (Loop through the numbers)

O(N) time


Binary Search Approach

time: O(logN)

Space: O(1)

left pointer

right pointer

mid = (left+right) / 2

mid == num:
  return mid


special check

mid 

if arr[l] < arr[mid]:
  if arr[l] < num < arr[mid]:
    r = mid - 1
  else:
    l = mid + 1

9, 12, 17, 2, 4, 5  6 7 8
l             m         r

l          r

       m

       l. r

          m

          n

if arr[mid] < arr[right]:
  if arr[mid] < num < arr[r]:
    l = mid + 1
  else:
    r = mid - 1



if arr[l] < num < mid
r = mid - 1


move the left pointer
move the right pointer

l==r and num!=l:
  return -1
  







function shiftedArrSearch(shiftArr, num):
    pivot = findPivotPoint(shiftArr)

    if(pivot == 0 OR num < shiftArr[0]):
        return binarySearch(shiftArr, pivot, shiftArr.length - 1, num)
    
    return binarySearch(shiftArr, 0, pivot - 1, num)


function findPivotPoint(arr):
    begin = 0
    end = arr.length - 1

    while (begin <= end):
        mid = begin + floor((end - begin)/2)
        if (mid == 0 OR arr[mid] < arr[mid-1]):
            return mid
        if (arr[mid] > arr[0]):
            begin = mid + 1
        else:
            end = mid - 1

    return 0


function binarySearch(arr, begin, end, num):
    while (begin <= end):
        mid = begin + floor((end - begin)/2)
        if (arr[mid] < num):
            begin = mid + 1
        else if (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1

"""

def shifted_arr_search(arr, num):
  l = 0
  r = len(arr) - 1
  
  while l <= r:
    
    mid = (l + r) // 2  # l + (r - l) // 2
    
    if arr[mid] == num:
      return mid

    if arr[l] < arr[mid]:
      if arr[l] <= num <= arr[mid]:
        r = mid - 1
      else:
        l = mid + 1

    elif arr[mid] < arr[r]:
      if arr[mid] <= num <= arr[r]:
        l = mid + 1
      else:
        r = mid - 1

  return - 1
