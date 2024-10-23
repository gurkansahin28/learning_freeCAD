import FreeCAD as App
import FreeCADGui as Gui
import Sketcher

# Create a new document
doc = App.newDocument("ArcBetweenLinesDoc")

# Add a sketch in the XY plane
sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
sketch.Support = (None, '')
sketch.MapMode = 'FlatFace'

# Vectors
V1 = App.Vector(0, 0, 0)
V2 = App.Vector(0, 8, 0)

V3 = App. Vector(2, 10, 0)
V4 = App.Vector(10, 10, 0)

# Define the two perpendicular lines from segments
lineSegment1 = Part.LineSegment(V1, V2)
lineSegment2 = Part.LineSegment(V3, V4)

line1 = sketch.addGeometry(lineSegment1, False)
line2 = sketch.addGeometry(lineSegment2, False)


# Define the arc
center = App.Vector(2, 8, 0)  # Center of the arc between the lines
radius = 2 # Radius of the arc
start_angle = 0  # Starting from the right side (0 degrees)
end_angle = 90  # Ending at the top (90 degrees)

# Add the arc to the sketch (center, start, end)
arc = sketch.addGeometry(Part.ArcOfCircle(Part.Circle(center, App.Vector(0, 0, 1), radius), start_angle, end_angle), False)

# Recompute to apply changes
doc.recompute()

# Optional: adjust the view to see the result
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")