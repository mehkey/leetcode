

# H-Tree Construction
An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

Here are some examples of H-trees at different levels of depth:

altdepth = 1

altdepth = 2

altdepth = 3

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

'''
Constraints:

[time limit] 5000ms

[input] double x

[input] double y

[input] double length

[input] double depth

0 ≤ depth ≤ 10
'''

A pash





##JAVA Version

'''
 static void drawLine(double x1, double y1, double x2, double y2){
    System.out.println(x1+" "+y1+" "+x2+" "+y2);
  }
  
  static void drawHTree(double x, double y, double length , double depth){
    if(depth==0) return ;
    double xL = x-length/2;
    double yL = y-length/2;
    
    drawLine(x+xL, y , x-xL , y);
    drawLine(x+xL , y+yL ,  x+xL, y-yL);
     drawLine(x-xL , y+yL ,  x-xL, y-yL);
    
    drawHTree(x+xL,y+yL, length/Math.sqrt(2), depth-1);
    drawHTree( x+xL, y-yL, length/Math.sqrt(2), depth-1) ;
    drawHTree(x-xL,y+yL ,  length/Math.sqrt(2), depth-1) ;
    drawHTree(x-xL, y-yL, length/Math.sqrt(2), depth-1) ;
      
  }

'''

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






