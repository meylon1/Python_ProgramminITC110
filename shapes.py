#SNOWMAN
#ASSIGNMENT3

from graphics import *


win = GraphWin("snowman" , 350 , 220 )
center = Point(72 ,78)
circ = Circle(center, 20)
circ.setFill("white")
circ.setOutline("white")
circ.draw(win)

center = Point(72 ,118)
circ1 = Circle(center, 30)
circ1.setFill("white")
circ1.setOutline("white")
circ1.draw(win)

center = Point(72 ,178)
circ2 = Circle(center, 40)
circ2.setFill("white")
circ2.setOutline("white")
circ2.draw(win)

center = Point(63 ,73)
circ3 = Circle(center, 2)
circ3.setFill("black")  
circ3.draw(win)

center = Point(79 ,73)
circ4 = Circle(center, 2)
circ4.setFill("black")
circ4.draw(win)

center = Point(72 ,100)
circ5 = Circle(center, 2)
circ5.setFill("blue")
circ5.draw(win)

center = Point(72 ,115)
circ6 = Circle(center, 2)
circ6.setFill("blue")
circ6.draw(win)

center = Point(72 ,130)
circ7 = Circle(center, 2)
circ7.setFill("blue")
circ7.draw(win)

rect = Rectangle(Point( 62 , 40),Point(80 ,60))
rect.setFill("black")
rect.draw(win)

rect1 = Rectangle(Point( 45 , 60),Point(95 ,56))
rect1.setFill("black")
rect1.draw(win)

rect3 = Rectangle(Point( 155 , 160),Point(165 ,190))
rect3.setFill("brown")
rect3.draw(win)

line = Line(Point( 15 , 140), Point(50 ,100))
line.draw(win)

line1 = Line(Point( 92, 97), Point(129, 135))
line1.draw(win)


aPolygon = Polygon(Point(160,115) , Point(122,160) ,Point(198,160))
pointList = aPolygon.getPoints()
aPolygon.setFill("green")
aPolygon.setOutline("green")
aPolygon.draw(win)

aPolygon1 = Polygon(Point(160, 69) , Point(145,90) ,Point(175,90))
pointList1 = aPolygon.getPoints()
aPolygon1.setFill("green")
aPolygon1.setOutline("green")
aPolygon1.draw(win)

aPolygon2 = Polygon(Point(160,90) , Point(135,120) ,Point(185,120))
pointList2 = aPolygon.getPoints()
aPolygon2.setFill("green")
aPolygon2.setOutline("green")
aPolygon2.draw(win)

aPolygon3 = Polygon(Point(72,80) , Point(68,75) ,Point(75,78))
pointList3 = aPolygon.getPoints()
aPolygon3.setFill("orange")
aPolygon3.draw(win)

center = Point(160 ,66)
circ3 = Circle(center, 3)
circ3.setFill("yellow")  
circ3.draw(win)

center = Point(135 ,123)
circ4 = Circle(center, 3)
circ4.setFill("yellow")  
circ4.draw(win)

center = Point(183 ,120)
circ5 = Circle(center, 3)
circ5.setFill("yellow")  
circ5.draw(win)

center = Point(160 ,130)
circ6 = Circle(center, 3)
circ6.setFill("red")  
circ6.draw(win)

center = Point(120 ,160)
circ7 = Circle(center, 3)
circ7.setFill("yellow")  
circ7.draw(win)

center = Point(195 ,160)
circ8 = Circle(center, 3)
circ8.setFill("yellow")  
circ8.draw(win)

mouth = Oval(Point(60 , 83), Point(85 ,86))
mouth.setFill("yellow")
mouth.draw(win)

win.setBackground("light blue")







   
