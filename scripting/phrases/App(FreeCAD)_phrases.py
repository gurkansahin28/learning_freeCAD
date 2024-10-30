import FreeCAD as App

docName = 'DummyDoc'
doc = App.newDocument(docName)
doc.addObject('Part::Box', 'MyBox')

App.newDocument([String], [hidden = False])

sectionObject = doc.addObject('Part::Feature', 'Section')

doc.getObject('MyBox')
doc.getObjectsByLabel('MyBox')
doc.recompute()

App.ActiveDocument
App.activeDocument()
App.getDocument(docName)
App.listDocuments()
App.setActiveDocument(docName)
App.ActiveDocument = App.getDocument("BooleanOperationToolsDoc")
App.openDocument(filepath, [hidden = False])

App.ActiveDocument.Name
App.ActiveDocument.recompute()
myDoc = FreeCAD.activeDocument()

App.Vector(x, y, z)
myVector = App.Vector(x, y, z)

App.closeDocument(docName)



