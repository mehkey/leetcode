def buildTree(a):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = a[i]
    # creating parent node by adding left and right child
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]


# function to update a node of the tree
def updateTree(index, value):
    # set value at position index 
    tree[index + n] = value
    index+=n
    # after updating the child node,update parents
    i = index
    while i > 1: 
    #update parent by adding new left and right child
        tree[i//2] = tree[i] + tree[i+1]
        i =i//2


#function to find sum on different range 
def queryTree(l, r):
    sum = 0
    #to find the sum in the range [l,r)
    l += n
    r += n
    while l < r:
        if ((l & 1)>0):
            sum += tree[l]
            l += 1
        if ((r & 1)>0):
            r -= 1
            sum += tree[r]
        l =l// 2
        r =r// 2
    return sum


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7,8]
    n = len(A)
    buildTree(A)
    print(queryTree(1, 4))
    updateTree(2, 5)
    print(queryTree(1, 4))



from segment_tree import SegmentTree
 
 
# an array with some elements
arr = [14, 28, 55, 105, 78, 4, 24, 99, 48, 200]
 
# here we are fitting our array
# into segment tree where t is
# taken as object of segment tree
# t will be used for performing
# operations on that segmentTree
 
t = SegmentTree(arr)
 
# here we are finding value of
# maximum number in a range
a = t.query(0, 9, "max")
print("The maximum value of this range is : ", a)
 
# here we are finding value of
# minimum number in a range
a = t.query(0, 9, "min")
print("The minimum value of this range is : ", a)
 
# here we are finding value
# of sum of a range
a = t.query(0, 9, "sum")
print("The sum of this range is : ", a)
 
# here we are updating the value
# of a particular index
t.update(5, 0)
print("The updated array is : ", arr)
 
 
# here we are finding value of
# sum of a range
a = t.query(1, 5, "sum")
print("The sum of this range is : ", a)
 
# here we are updating the value
# of a particular index
t.update(4, 10)
print("The updated array is : ", arr)