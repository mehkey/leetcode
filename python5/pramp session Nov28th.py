


DASHBOARD
SWAP ROLES
IT'S YOUR PEER'S TURN TO INTERVIEW YOU. WHEN DONE, CLICK ON THE SWAP ROLES BUTTON ON THE LEFT
END SESSION
QUESTION
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer


Content

Code

Video
Python
Plain Text
C
C#
C++
Clojure
Go
HTML/CSS/JS
Haskell
Java
JavaScript
PHP
Python
Ruby
Swift
Reset
1
def find_pairs_with_given_difference(arr, k):
2
  
3
  
4
  unique_numbers = set(arr)
5
​
6
  result = []
7
​
8
  for number in arr:
9
    #number is going to be the Y value in order to keep Y order
10
​
11
    #0,    0 + k.    0 + 1.     1
12
    #-1,   0 + k.    
13
    if number + k  in unique_numbers:
14
      result.append([number + k,number])
15
​
16
  return result
17
​
18
​
19
  
20
  
21
  
22
​
23
​
CONSOLE
Ready to Run Code
RUN CODE
RUN TESTS
Reconnecting your peer...
You
Peer
Legend



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


