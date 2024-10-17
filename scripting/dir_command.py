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

###########################################################################3

