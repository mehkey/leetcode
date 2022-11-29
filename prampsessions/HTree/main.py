
"""

Create a H-tree


HTree Object

-> Center postion X,Y
-> Width of the Tree
-> Composite Design Pattern
    -> Structural Design 
    -> each object has a list of subojects


drawHTree(hTree)

drawHTree(root)

    drawHTree(childTree)

drawLine(X0,Y0,X1,Y1)



N = depth of the when called DrawTree()

1
4
4*4

O(4^N)

Space complexity

Space complexity is the same

O(4^N)

There is a way to do it in O(N)

O(N)


"""

CENTER_LENGTH:int = 10.0
  
class Position:
  def __init__(self,X:int,Y:int)->None:
    self.x = X
    self.y = Y

class HTree:
  
  def __init__(self,
               centerPosition:Position,
               length: int
              ) -> None:

    self.centerPosition = centerPosition
    self.length = length
    
  
  def addChildNodes(self,depth:int) -> None:
    
    if depth == 0:
      return

    new_length = self.length / sqrt(2)
    half = self.length /2
    center = self.centerPosition

    new_centers = [[center.x - half, center.y - half],
    [center.x + half, center.y - half],
    [center.x + half, center.y + half],
    [center.x + half, center.y + half]]
    
    self.childTrees: List[HTree] = [None] * 4

    for i,new_center in enumerate(new_centers):

      newTree = HTree(Position(new_center[0],new_center[1]), new_length)

      self.childTrees[i] = newTree

      newTree.addChildNodes(depth - 1)

  def drawTree(self):
    
    #we have the center of the tree
    center:Position = self.centerPosition
    half:int = self.length/2

    #Create the line for center bar
    drawLine(center, Position(center.x+half,center.y) )
    drawLine(center, Position(center.x-half,center.y) )

    #Create the line for right bar
    drawLine(Position(center.x+half,center.y+half), Position(center.x-half,center.y-half) )

    #Create the line for left bar
    drawLine(Position(center.x-half,center.y-half), Position(center.x-half,center.y+half) )

    for child in self.childTrees:
      child.drawTree()


class TreeDrawer:
  
  def drawTree(depth:int):
    
    #root
    root = HTree(Position(0,0),CENTER_LENGTH)

    root.addChildNodes(depth-1)
    
    root.drawTree()

t = TreeDrawer()
t.drawTree(4)

def drawLine(position0: Position,position1: Position):
    pass



#print "Practice makes Perfect!"   
