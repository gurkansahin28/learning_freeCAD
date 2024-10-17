import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part

docName = "RoundedRectangleDoc"
doc = App.newDocument(docName)

length = 50
width = 30

# Create the rectangle at the origin
rect = Draft.makeRectangle(length, width)

# Round the corners (apply fillet) by specifying the fillet radius
fillet_radius = 5  # Radius for rounding the corners
rect.FilletRadius = fillet_radius

doc.recompute()

# Convert the rectangle to a face so it can be extruded
face = Part.Face(Part.Wire(rect.Shape.Edges))

extrusion_height = 10
extruded_shape = face.extrude(App.Vector(0, 0, extrusion_height))

# Add the extruded shape to the FreeCAD document
extruded_obj = doc.addObject("Part::Feature", "ExtrudedRoundedRectangle")
extruded_obj.Shape = extruded_shape

doc.recompute()

Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
#App.closeDocument(docName)
