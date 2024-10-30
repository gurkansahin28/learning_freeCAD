import FreeCAD as App

docName = 'DummyDoc'
doc = App.newDocument(docName)
doc.addObject('Part::Box', 'MyBox')

sectionObject = doc.addObject('Part::Feature', 'Section')

doc.getObject('MyBox')
doc.getObjectsByLabel('MyBox')
doc.recompute()

App.ActiveDocument
App.ActiveDocument.Name
App.ActiveDocument.recompute()

App.Vector(x, y, z)
myVector = App.Vector(x, y, z)

App.closeDocument(docName)


