
import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft

docName = 'CreationBoxes'
doc = App.newDocument(docName)

App.setActiveDocument("CreationBoxes")
App.ActiveDocument=App.getDocument("CreationBoxes")
Gui.ActiveDocument=Gui.getDocument("CreationBoxes")
