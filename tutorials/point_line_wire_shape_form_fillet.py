'''
THE GOAL
--------
    This document aims to show a way to create a solid object by starting from draft.

THE CONTENT
-----------

A. IMPORTS
	1. Importing libraries and abbreviating them for coding convenience 
		a. importing FreeCAD as an alias
		b. importing FreeCADGui as an alias
		c. importing Draft module to create points, lines and the wire
		d. importing random module to obtain number for the RGB colors


B. FUNCTIONS
	1. Defining a specific function
		a. random float generator function
		b. a function texting a message to the report view
		c. function setting up the visualization


C. GLOBALS
	1. the point at Z axis


D. DOCUMENT
	1. a specific document name
	2. creating a document with the specific doc name
	3. computing the document


E. POINTS
	THe Left Side Point:
		1. defining the origin
		2. creating the left side point
		3. setting up the left side point color
		4. setting up the left side point size
		5. recomputing the document
		6. setting up the visualization
		7. texting a feedback message to the report view

	The Right Side Point:
		8. creating the right side point
		9. setting up the right side point color
		10. setting up the right side point size
		11. recomputing the document
		12. setting up the visualization
		13. texting a feedback message to the report view

	The Top Side Point:
		14. creating the top side point
		15. setting up the top side point color randomly by using the defined rnd function
		16. setting up the top side point size
		17. recomputing the document
		18. setting up the visualization
		19. texting a feedback message to the report view
		20. setting up the points for auto-grouping
		21. the operation for auto-grouping
		22. recomputing the document


F. LINES
	The Bottom Line:
		1. starting points for the bottom line 
		2. converting points into the left point vector
		3. ending point for the bottom line
		4. converting points into the right point vector
		5. creating the bottom line using vectors
		6. setting up the bottom line color randomly by using the defined rnd function
		7. recomputing the document
		8. texting a feedback message to the report view
		9. setting up the visualization
	The Right Line:
		10. ending points for the right line
		11. converting points to the top point vector
		12. creating the right line using vectors
		13. setting up the right line color randomly by using the defined rnd function
		14. recomputing the document
		15. texting a feedback message to the report view
		16. setting up the visualization
	The Left Line:
		17. creating the left line by using existing vectors
		18. setting up the left line color randomly by using the defined rnd function
		19. recomputing the document
		20. texting a feedback message to the report view
		21. setting up the visualization


G. WIRE and SHAPE
	1. defining a list to collect the vectors
	2. creating closed and faced wire
	3. Move the wire to a new position on the XY plane
	4. recomputing the document
	5. texting a feedback message to the report view
	6. setting up the visualization


H. FORM
	1. identifying the extrusion vector
	2. operating extrusion
	3. recomputing the document
	4. texting a feedback message to the report view
	5. setting up the visualization


I. BODY
	1. defining an object name
	2. defining a variable to mention the object from which features come
	3. creation of the body
	4. recomputing the document


J. LINKS
	1. selecting the object to link
	2. selecting the container object to which link
	3. adjusting the relative links
	4. applying the adjusted relative linked object to the container object
	5. recomputing the document


K. FILLET OPERATION
	1. creating the fillet operation
	2. selecting the extruded object to use the fillet base object
	3. setting up edges to apply the fillet operation
	4. setting up the rounding radius
	5. setting up all edges to be applied 
	6. hiding base object
	7. recomputing the document


L. RANDOMLY COLORIZING
	1. abbreviating the phrase to obtain coding convenience
	2. clearing the existing selection
	3. adding the object to the selection 
	4. applying the random color command
	5. clearing the existing selection

Last edited:
Thu Dec  5 10:50:49 PM +03 2024

FreeCAD Version: 1.0.0

license: CCO 1.0
https://creativecommons.org/publicdomain/zero/1.0/


author: gurkan
gurkansahin28@gmail.com
'''

### A. IMPORTS ----------------------------
## Importing libraries and abbreviating them for coding convenience 
# importing FreeCAD as an alias
import FreeCAD as App # type: ignore
# importing FreeCADGui as an alias
import FreeCADGui as Gui # type: ignore
# importing Draft module to create points, lines and the wire
import Draft # type: ignore
# importing random module to obtain number for the RGB colors
import random


### B. FUNCTIONS --------------------------
## Defining a specific function
# random float generator function
def rnd():
    '''Generate a random float upto 1.0.
    Args: It doesn't take any argument.
    Returns: It returns a float number.
    Example:
        redColor = rnd()
        greenColor = rnd()
        blueColor = rnd()
    '''
    r = random.random()
    return r

# a function texting a message to the report view
def txtRv(msg):
    '''Send the message to the report view.
    Args:
        msg (str): a message to text into report view.
    Returns: 
        It doesn't return anything.
    Example:
        txtRv('The process was successful.')'''
    App.Console.PrintMessage(f'\n{msg}')
    pass

# function setting up the visualization
def setVsl():
    '''Set Visual Adjustments. 
    But beforehand, the Draft WB to be auto-loaded.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            setVsl()
    '''
    # creating GuiView object to increase the readability
    GuiView = Gui.ActiveDocument.ActiveView
    # adjusting the view as isometric
    GuiView.viewIsometric()
    # displaying the crossing axes in the view
    GuiView.setAxisCross(True)
    # displaying all work in the view area
    GuiView.fitAll()
    # texting message in the report view
    txtRv(msg='\nVisualization was done.')
    pass


### C. GLOBALS --------------------------------
# the point at Z axis never change along the document
# for ensuring the XY plane
z = 0.0


### D. DOCUMENT ------------------------------
# a specific document name
docName = 'FromPointToForm'
# creating a document with the specific doc name
doc = App.newDocument(docName)
# computing the document
doc.recompute()


### E. POINTS --------------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to create left point!')
# defining the origin
x = 0.0
y = 0.0
# creating the left side point
leftPoint = Draft.makePoint(x, y, z)
# setting up the left side point color
leftPoint.ViewObject.PointColor = (0.9, 0.1, 0.2)
# setting up the left side point size
leftPoint.ViewObject.PointSize = 10
# recomputing the document
doc.recompute()
# setting up the visualization
setVsl()
# texting a feedback message to the report view
txtRv('The left point has been created...')


# pause to analyze the code and inform the learner by using input command
input('Press Enter to create right point!')
# the point at the X axis to create the second one 
x = 6.0
# creating the right side point
rightPoint = Draft.makePoint(x, y, z)
# setting up the right side point color
rightPoint.ViewObject.PointColor = (0.1, 0.9, 0.2)
# setting up the right side point size
rightPoint.ViewObject.PointSize = 15
# recomputing the document
doc.recompute()
# setting up the visualization
setVsl()
# texting a feedback message to the report view
txtRv('The right point has been created...')


# pause to analyze the code and inform the learner by using input command
input('Press Enter to create top point!')
# points for the top side
x = 3.0
y = 8.0
# creating the top side point
topPoint = Draft.makePoint(x, y, z)
# setting up the top side point color randomly by using the defined rnd function
topPoint.ViewObject.PointColor = (rnd(), rnd(), rnd())
# setting up the top side point size
topPoint.ViewObject.PointSize = 20
# recomputing the document
doc.recompute()
# setting up the visualization
setVsl()
# texting a feedback message to the report view
txtRv('The top point has been created...')

# setting up the points for auto-grouping
points = [leftPoint, rightPoint, topPoint]
# the operation for auto-grouping
Draft.autogroup(points)
# recomputing the document
doc.recompute()


### F. LINES -----------------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to create the bottom line!')
# starting points for the bottom line 
x = 0.0
y = 0.0
# converting points into the left point vector
leftPoint = App.Vector(x, y, z)
# ending point for the bottom line
x = 6.0
# converting points into the right point vector
rightPoint = App.Vector(x, y, z)
# creating the bottom line using vectors
bottomLine = Draft.makeLine(leftPoint, rightPoint)
# setting up the bottom line color randomly by using the defined rnd function
bottomLine.ViewObject.LineColor = (rnd(), rnd(), rnd())
# recomputing the document
doc.recompute()
# texting a feedback message to the report view
txtRv('The bottom line has been created...')
# setting up the visualization
setVsl()

# pause to analyze the code and inform the learner by using input command
input('Press Enter to create the right line!')
# ending points for the right line
x = 3.0
y = 8.0
# converting points to the top point vector
topPoint = App.Vector(x, y, z)
# creating the right line using vectors
rightLine = Draft.makeLine(rightPoint, topPoint)
# setting up the right line color randomly by using the defined rnd function
rightLine.ViewObject.LineColor = (rnd(), rnd(), rnd())
# recomputing the document
doc.recompute()
# texting a feedback message to the report view
txtRv('The right line has been created...')
# setting up the visualization
setVsl()

# pause to analyze the code and inform the learner by using input command
input('Press Enter to create the left line!')
# creating the left line by using existing vectors
leftLine = Draft.makeLine(topPoint, leftPoint)
# setting up the left line color randomly by using the defined rnd function
leftLine.ViewObject.LineColor = (rnd(), rnd(), rnd())
# recomputing the document
doc.recompute()
# texting a feedback message to the report view
txtRv('The left line has been created...')
# setting up the visualization
setVsl()


### G. WIRE and SHAPE --------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to create a wire!')
# defining a list to collect the vectors
points = [leftPoint, rightPoint, topPoint]
# creating closed and faced wire
wire = Draft.makeWire(points, closed = True, face = True)

# pause to analyze the code and inform the learner by using input command
input('Press Enter to put the wire to and create a face in a different place!')
# Move the wire to a new position on the XY plane
wire.Placement.Base = App.Vector(3, 3, z)
# recomputing the document
doc.recompute()
# texting a feedback message to the report view
txtRv('The shape has been created and transported...')
# setting up the visualization
setVsl()


### H. FORM ------------------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to create a form!')
# identifying the extrusion vector
extVec = App.Vector(0, 0, 2)
# operating extrusion
ext = Draft.extrude(wire, extVec, solid = True)
# recomputing the document
doc.recompute()
# texting a feedback message to the report view
txtRv('The form has been created...')
# setting up the visualization
setVsl()


### I. BODY ------------------------------------
# pause to analyze the code and inform the learner by using input command
input('Press to create a Body!..')
# defining an object name
objName = 'MyBody'
# defining a variable to mention the object from which features come
objFromLib = 'PartDesign::Body'
# b. creation of the body
body = doc.addObject(objFromLib, objName)
# recomputing the document
doc.recompute()


### J. LINKS -------------------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to adjust relative links to the body!')
# selecting the object to link
whichObj = doc.getObject(ext.Name)
# selecting the container object to which link
toWhichObj = doc.getObject(body.Name)

# adjusting the relative links
whichObj.adjustRelativeLinks(toWhichObj)
# applying the adjusted relative linked object to the container object
toWhichObj.ViewObject.dropObject(whichObj, None, '', [])
# recomputing the document
doc.recompute()


### K. FILLET OPERATION --------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to start Fillet operation!')
# creating the fillet operation
objName = 'MyFillet'
objFromLib = 'PartDesign::Fillet'
fill = body.newObject(objFromLib, objName)
# selecting the extruded object to use the fillet base object
extObj = App.getDocument(docName).getObject('BaseFeature')
# setting up edges to apply the fillet operation
fill.Base = (extObj, [f"Edge{i}" for i in extObj.Shape.Edges])
# setting up the rounding radius
fill.Radius = 0.2
# setting up all edges to be applied 
fill.UseAllEdges = True
# hiding base object
extObj.Visibility = False
# recomputing the document
doc.recompute()


### L. RANDOMLY COLORIZING ------------------------
# pause to analyze the code and inform the learner by using input command
input('Press Enter to paint the object randomly!')
# abbreviating the phrase to obtain coding convenience
GuiSel = Gui.Selection
# clearing the existing selection
GuiSel.clearSelection()
# adding the object to the selection 
GuiSel.addSelection('FromPointToForm','MyBody','MyFillet')
# applying the random color command
Gui.runCommand('Std_RandomColor',0)
# clearing the existing selection
GuiSel.clearSelection()
