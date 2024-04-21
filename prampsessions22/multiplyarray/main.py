def array_of_array_products(arr):
  
  '''
  [8, 10, 2]
  
  O(N)
  
  O(N^2)
  
  [left side multiplication]
  
  [right side multiplication]
  '''
   
  
  
  N = (len(arr))
  
  #print(N)
  
  if N <= 1:
    return []
  
 # if N == 2:
  #  return arr
  

  # Two sum <-> Prefix Product/Sum
  left_mult = [1] * (N+1)
  
  right_mult = [1] * (N+1)
  
  #[1,8,80,160]
  for i in range(1,len(arr)+1):

    left_mult[i] = left_mult[i-1] * arr[i-1]
  
  #reverse = reversed(arr)
  
  for i in range(len(arr)-1,-1,-1):
    #print(i)
    right_mult[i] = right_mult[i+1] * arr[i]
  
  
  
  #print(left_mult)
  #print(right_mult)
  
  #result = [1] * (len(arr))

  result = []
  
  for i,n in enumerate(arr):
    
    result.append(left_mult[i] * right_mult[i+1])
  
  return result
  
  # millions of elements
  
  '''
  
  N is the size of the input array
  
  time: O(N)

  space:O(1)
  sum ( array ) :  O(1)

  space: O(N) = space.   K * N. .  K is a constant
  
  k = 1000.  k = 1
  


  if len(arr) <= 1:
    return []
  
  # inplace for result array
  result = [1] * len(arr)
  prefix = 1
  for indx in range(1, len(arr)):
    result[indx] *= prefix
    prefix *= arr[indx]
   
  postfix = 1
  for indx in range(len(arr) - 1, -1, -1):
    result[indx]
    
  '''