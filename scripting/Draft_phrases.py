import FreeCAD as App
import Draft

myRect = Draft.makeRectangle(4, 3)
myDistance = App.Vector(2, 2, 0)
Draft.move(myRect, myDistance)

myCutObj = Draft.cut(ObjOne, ObjTwo)

