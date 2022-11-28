def find_pairs_with_given_difference(arr, k):
  
  
  unique_numbers = set(arr)

  result = []

  for number in arr:
    #number is going to be the Y value in order to keep Y order

    #0,    0 + k.    0 + 1.     1
    #-1,   0 + k.    
    if number + k  in unique_numbers:
      result.append([number + k,number])

  return result


  
  
  


'''
{
key: val
}

SET
{

0,
-1,
-2,
2,
1
}

Approach

arr = [0, -1, -2, 2, 1]


The order of the elements inside the pairs is the greatest element is added first


The order of the pairs is given by the y element


Approach:

HM

Put all the elements in a SET.
The key of HM is the number in the array.


Loop throught the elements and see if there is a difference of k


Runtime :

O(N)

Spactime:

O(N)


Big O time earlier

Start with bruteforce



'''


