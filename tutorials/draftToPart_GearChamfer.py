"""
This document aims to follow a path 
beginnig from the simple Draft objects 
arriving to Part objects and features.

"""
# Importing FreeCAD and FreeCADGui as aliases
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
# Importing the required libraries 
import Draft # type: ignore
import Part # type: ignore
from BOPTools import BOPFeatures # type: ignore

# Creating a new document with the given name
docName = 'GearDoc'
doc = App.newDocument(docName)

# Defining a function to make arcs with given params
def specArc(r=2, x=2, y=2, z=0, start=180, end=270):
    '''
    Draws an arc of circle through given parameters.
    r -> radius of the arc
    x, y, z -> center of the arc
    start -> start angle of the arc
    end -> end angle of the arc
    '''
    pl = App.Placement()
    centerVectorA = App.Vector(x, y, z)
    pl.Base = centerVectorA
    arc = Draft.makeCircle(radius = r, placement = pl, face = False, \
    startangle = start, endangle = end, support = None)
    App.ActiveDocument.recompute()
    return arc


# global variables
r = 2
z = 0

## Arc of a1: convex
c = (2, 2, z) # center of the arc
s = 180 # start angle of the arc
e = 270 # end angle of the arc
a1 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

#input('Press Enter to draw a specific arc...')
## Arc of a2: concave
c = (4, 0, z)
s = 0
e = 180
a2 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a3: convex
c = (6, 2, z)
s = 270
e = 0
a3 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a4: concave
c = (8, 4, z)
s = -270
e = -90
a4 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a5: convex
c = (6, 6, z)
s = 0
e = 90
a5 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a6: concave
c = (4, 8, z)
s = -180
e = 0
a6 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a7: convex
c = (2, 6, z)
s = 90
e = 180
a7 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## Arc of a8: concave
c = (0, 4, z)
s = -90
e = -270
a8 = specArc(r=r, x=c[0], y=c[1], z=c[2], start=s, end=e)

## circle at the center
c = (4, 4, z)
s = 0
e = 360
hole = specArc(r=1, x=c[0], y=c[1], z=c[2], start=s, end=e)



wires = [a1, a2, a3, a4, a5, a6, a7, a8]
j = Draft.upgrade(wires, delete = True)
doc.recompute()

## Making circle face
doc = App.getDocument(docName)
obj = doc.getObject(hole.Name)
obj.MakeFace = True
doc.recompute()



## Making Face
doc = App.getDocument(docName)
obj = doc.getObject('Wire')
face = Part.Face(obj.Shape)
doc.recompute()




## Making hole Extrusion
doc = App.getDocument(docName)
extrusionVec = App.Vector(0, 0, 10)
cylFace = hole.Shape
solid = cylFace.extrude(extrusionVec)
featFromLib = 'Part::Feature'
objName = 'MyCylinder'
obj = doc.addObject(featFromLib, objName)
obj.Shape = solid
doc.getObject(hole.Name).Visibility = False
doc.recompute()




## Making Wire Extrusion
doc = App.getDocument(docName)
extrusionVec = App.Vector(0, 0, 10)
solid = face.extrude(extrusionVec)
featFromLib = 'Part::Feature'
objName = 'MyExtrusion'
obj = doc.addObject(featFromLib, objName)
obj.Shape = solid
doc.getObject('Wire').Visibility = False
doc.recompute()


## Making Cut operation
doc = App.getDocument(docName)
bp = BOPFeatures.BOPFeatures(doc)
fromWhichObj = doc.getObject('MyExtrusion')
whichObj = doc.getObject('MyCylinder')
cutObj = bp.make_cut([fromWhichObj.Name, whichObj.Name,])
doc.recompute()


## Chamfer
doc = App.getDocument(docName)
baseObj = doc.getObject(cutObj.Name)
chamfer = doc.addObject('Part::Chamfer', 'MyChamfer')
chamfer.Base = baseObj
size1, size2 = 0.3, 0.3
try:
    chamfer.Edges = [(edge, size1, size2) for edge in range(1, len(baseObj.Shape.Edges) + 1)]
    doc.recompute()
except Exception as e:
    print(f"Error: {e}")

baseObj.Visibility = False
