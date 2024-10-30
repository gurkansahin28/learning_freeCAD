import FreeCAD as App

docName = 'DummyDoc'
doc = App.newDocument(docName)
doc.addObject('Part::Box', 'MyBox')

App.newDocument(docName, hidden = False)

sectionObject = doc.addObject('Part::Feature', 'Section')

doc.getObject('MyBox')
doc.getObjectsByLabel('MyBox')
doc.recompute()

App.ActiveDocument
App.activeDocument()
App.getDocument(docName)
App.listDocuments()
App.setActiveDocument(docName)
App.ActiveDocument = App.getDocument(docName)
App.openDocument(filepath, hidden = False)

App.ActiveDocument.Name
App.ActiveDocument.recompute()
myDoc = FreeCAD.activeDocument()

App.Vector(x, y, z)
myVector = App.Vector(x, y, z)

App.closeDocument(docName)

#------------------------------------------
obj.Placement.Base = App.Vector(15,20,0)
obj.Placement.Rotation = App.Rotation(App.Vector(15,20,0), 45)
#-------------------------------------------


