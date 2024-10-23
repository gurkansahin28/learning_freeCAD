Python 3.11.9 (main, Nov 10 2011, 15:00:00) [GCC 13.2.0] on linux
Type 'help', 'copyright', 'credits' or 'license' for more information.
>>> # Gui.runCommand('Std_Workbench',14)
>>> # Gui.runCommand('Std_ViewStatusBar',1)
>>> # Gui.runCommand('Std_Workbench',1)
>>> # Gui.runCommand('Std_Workbench',7)
>>> # Gui.runCommand('Std_Workbench',12)
>>> # Gui.runCommand('Std_Workbench',14)
>>> import FreeCAD as App
>>> import FreeCADGui as Gui
>>> import Sketcher
>>> 
>>> # Create a new document
>>> doc = App.newDocument("ArcBetweenLinesDoc")
>>> # App.setActiveDocument("ArcBetweenLinesDoc")
>>> # App.ActiveDocument=App.getDocument("ArcBetweenLinesDoc")
>>> # Gui.ActiveDocument=Gui.getDocument("ArcBetweenLinesDoc")
>>> 
>>> # Add a sketch in the XY plane
>>> sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
>>> sketch.Support = (None, '')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: Expects sequence of items of type DocObj, (DocObj,SubName), or (DocObj, (SubName,...))
>>> sketch.MapMode = 'FlatFace'
>>> 
>>> # Define the two parallel lines
>>> line1 = sketch.addGeometry(Part.LineSegment(App.Vector(0, 0, 0), App.Vector(0, 50, 0)), False)  # Vertical line on the left
>>> line2 = sketch.addGeometry(Part.LineSegment(App.Vector(30, 0, 0), App.Vector(30, 50, 0)), False)  # Vertical line on the right
>>> 
>>> # Define the arc
>>> center = App.Vector(15, 25, 0)  # Center of the arc between the lines
>>> radius = 15  # Radius of the arc
>>> start_angle = 0  # Starting from the right side (0 degrees)
>>> end_angle = 90  # Ending at the top (90 degrees)
>>> 
>>> # Add the arc to the sketch (center, start, end)
>>> arc = sketch.addGeometry(Part.ArcOfCircle(Part.Circle(center, App.Vector(0, 0, 1), radius), start_angle, end_angle), False)
>>> 
>>> # Recompute to apply changes
>>> doc.recompute()
1
>>> 
>>> # Optional: adjust the view to see the result
>>> Gui.activeDocument().activeView().viewAxometric()
>>> Gui.SendMsgToActiveView("ViewFit")
>>> # Gui.runCommand('Std_OrthographicCamera',1)
>>> 
