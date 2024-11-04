>>> dir()
['App', 'Crt', 'Err', 'FCADLogger', 'FreeCAD', 'FreeCADGui', 'GeneratePackageIcon', 'Gui', 
 'IntEnum', 'Log', 'Msg', 'Ntf', 'NumberFormat', 'PathCommandGroup', 'PropertyType', 
 'ResolveMode', 'ReturnType', 'ScaleType', 'Scheme', 'Start', 'StartPage', 'Tnf', 
 'WebGui', 'WebPage', 'WebView', 'Workbench', 'Wrn', 
 '_SoGroup_init', '_SoGroup_init_orig', '__annotations__', '__builtins__', 
 '__doc__', '__loader__', '__name__', '__package__', '__spec__', 
 'cmake', 'coin', 'datetime', 'inspect', 'os', 'removeFromPath', 
 'setupSearchPaths', 'sys', 'traceback', 'webView']
>>> 

>>> dir(Part)
['Arc', 'ArcOfCircle', 'ArcOfConic', 'ArcOfEllipse', 'ArcOfHyperbola', 'ArcOfParabola', 'AttachEngine',
 'BRepFeat', 'BRepOffsetAPI', 'BSplineCurve', 'BSplineSurface', 'BezierCurve', 'BezierSurface', 'BodyBase',
 'ChFi2d', 'Circle', 'CompSolid', 'Compound', 'Cone', 'Conic', 'Cylinder',
 'Edge', 'Ellipse', 'Face',
 'Feature',
 'Geom2d', 'GeomPlate', 'GeometryBoolExtension', 'GeometryDoubleExtension', 'GeometryIntExtension', 'GeometryStringExtension',
 'HLRBRep', 'Hyperbola',
 'Line', 'LineSegment',
 'OCCConstructionError', 'OCCDimensionError', 'OCCDomainError', 'OCCError', 'OCCRangeError', 'OCC_VERSION', 'OffsetCurve', 'OffsetSurface',
 'Parabola', 'Part2DObject', 'Plane', 'PlateSurface', 'Point', 'Precision', 'RectangularTrimmedSurface',
 'Shape', 'ShapeFix', 'ShapeUpgrade', 'Shell', 'Solid', 'Sphere', 'SurfaceOfExtrusion', 'SurfaceOfRevolution',
 'Toroid',
 'Vertex',
 'Wire',
 '__doc__', '__file__', '__fromPythonOCC__', '__loader__',
 '__name__', '__package__', '__sortEdges__',
 '__spec__', '__toPythonOCC__',
 'cast_to_shape', 'clearShapeCache',
 'export', 'exportUnits',
 'getFacets', 'getShape', 'getSortedClusters',
 'insert', 'joinSubname',
 'makeBox', 'makeCircle', 'makeCompound', 'makeCone', 'makeCylinder',
 'makeFace', 'makeFilledFace', 'makeFilledSurface', 'makeHelix',
 'makeLine', 'makeLoft', 'makeLongHelix', 'makePlane', 'makePolygon',
 'makeRevolution', 'makeRuledSurface', 'makeShell', 'makeShellFromWires',
 'makeSolid', 'makeSphere', 'makeSplitShape', 'makeSweepSurface',
 'makeThread', 'makeTorus', 'makeTube', 'makeWedge', 'makeWireString',
 'open', 'read', 'setStaticValue', 'show', 'sortEdges', 'splitSubname']
>>> 
#################################################################################

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

