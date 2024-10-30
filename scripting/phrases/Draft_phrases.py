
# Draft API
# wiki.freecad.org

import FreeCAD as App
import Draft

myRect = Draft.makeRectangle(4, 3)
myDistance = App.Vector(2, 2, 0)
Draft.move(myRect, myDistance)

Draft.move(App.Obj or List, Vector, [copymode])

Draft.rotate(App.Obj or List, angle, [center], [axis], [copymode])

Draft.scale(App.Obj or List, Vector, [center], [copymode])

myCutObj = Draft.cut(ObjOne, ObjTwo)

extrude = Draft.extrude(Obj, Vector)

fuse = Draft.fuse(ObjectOne, ObjectTwo)

Draft.makeLine(Vector, Vector)

Draft.makeWire(list of Part.Wire, [closed], [placement], [facemode])

Draft.makeCircle(radius, [placement], [facemode], [startangle], [endangle])

Draft.select(App.Obj)

Draft.getSelection()


