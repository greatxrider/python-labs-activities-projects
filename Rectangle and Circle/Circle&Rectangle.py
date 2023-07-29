# Jeph Mari Daligdig
# Circle&Rectangle
from Class.circleClass import Circle
from Class.rectangleClass import Rectangle

def CreateRedCircle():
    RedCircle = Circle(10, "red")
    dir(RedCircle)
    RedCircle.radius
    RedCircle.color
    RedCircle.drawCircle()

def CreateBlueCircle():
    BlueCircle = Circle(10, "blue")
    dir(BlueCircle)
    BlueCircle.radius
    BlueCircle.color
    BlueCircle.drawCircle()

def CreateRectangle():
    SkinnyBlueRectangle = Rectangle(2, 3, "blue")
    SkinnyBlueRectangle.height
    SkinnyBlueRectangle.width
    SkinnyBlueRectangle.color
    SkinnyBlueRectangle.drawRectangle()

CreateBlueCircle()
CreateRedCircle()
CreateRectangle()