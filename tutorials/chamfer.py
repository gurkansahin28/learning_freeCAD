#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:26:55 2024

@author: gurkan
"""

import Part
import FreeCAD as App
import FreeCADGui as Gui

# creating a document via a name and label
docName = 'ChamferDoc'
doc = App.newDocument(docName)
doc.Label = docName

# creating a box from the Part library
objFromLib = 'Part::Box'
objName = 'Box'
box = App.ActiveDocument.addObject(objFromLib, objName)
doc.recompute()

### Chamfer Operations
## declearing doc, baseObj, fillets, library and object name
doc = App.getDocument(docName)
baseObj = doc.getObject('Box')
__fillets__ = []
objFromLib = 'Part::Chamfer'
objName = 'Chamfer'
# adding chamfer object to the document
chamfer = doc.addObject(objFromLib, objName)
chamfer.Base = baseObj
# creating and stroring chamfer values for the edges
for edge in range(1, 13):
    __fillets__.append((edge, 1.00, 1.00))
# applying the edge related chamfer values
chamfer.Edges = __fillets__
del __fillets__
baseObj.Visibility = False
doc.recompute()
