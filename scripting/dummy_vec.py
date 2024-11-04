
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)

##############################################################################

import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print(sel[0].Placement)
print(sel[0].getGlobalPlacement())   # return the GlobalPlacement
print(sel[0].getParentGeoFeatureGroup()) # return the GeoFeatureGroup, ex:  Body or a Part.
print("____________________")

###########################################################################

doc = FreeCAD.newDocument()
>>> box = doc.addObject("Part::Box", "myBox")
>>> doc.recompute()
1
>>> box.Height = 5
>>> myvec = FreeCAD.Vector(2, 0, 0)
>>> myvec.x
2.0
>>> myvec.y
0.0
>>> othervec = FreeCAD.Vector(0, 3, 0)
>>> sumvec = myvec.add(othervec)
>>> box.Placement
Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
>>> box.Placement.Base
Vector (0.0, 0.0, 0.0)

>>> myVec = FreeCAD.Vector(5, 2, 0)
>>> box.Placement.Base = myVec
>>> vo = box.ViewObject
>>> vo.Transparency = 80
>>> vo.hide()
>>> vo.show()
>>> 
