'''
INTRO
-----
    By documenting a learning material, this document primely aims a macro that shows 
    how to change properties of a Torus object in FreeCAD scripting.

    The Open Source Softwares are crucial for the students 
    who are possible entrepreneurs. Thus, the second aim is 
    to support such materials for the K12 students and beyond.
    
LEARNING OUTCOMES
-----------------
    1. To see how which value changes the Torus appearance.  

CONTENT
-------
    A. IMPORST
        1. Importing required libraries as aliases
        2. Importing some specific parts from libraries
            a. Importing Units for value types of length and angle
            b. Importing QtGui for building the macro interface
            c. Importing Qt for assigning the Slider property
            d. Importing datetime for creating unique doc name

    B. SPECIFIC FUNCTIONS
        1. Setting up the Gui for visualization
        2. Creating a unique name for the new document
        3. The updater function for the Torus parameters 

    C. THE DOCUMENT
        1. Preparing a unique document name 
        2. Creating a document given unique name

D. GLOBAL VALUES
    1. Preparing default values for the Torus object
        a. Radius1: a distance from the torus center to the circle center
        b. Radius2: a distance from the circle center to its circumference
        c. Angle1: A slicer angle to slice the profile circle from the top (top arc)
        d. Angle2: A slicer angle to slice the profile circle from the bottom (bottom arc)
        e. Angle3: An angle for the profile circle to sweep

E. TORUS OBJECT

F. BUILDING INTERFACE
    1. Child Widget's Setup 
        a. Naming the user interface
        b. Creating the layout of the ui's items
        c. Slider 1 setup for the Radius 1
        d. Slider 2 setup for the Radius 2
        e. Slider 3 setup for the Angle 1
        f. Slider 4 setup for the Angle 2
        g. Slider 5 setup for the Angle 3
        
    2. Set the layout
    3. The updating function for the slider labels' values
    
G. DECLARING AN INSTANCE



FreeCAD Version: 
---------------
1.0.0

license: 
-------
CCO 1.0
https://creativecommons.org/publicdomain/zero/1.0/

Created on Sun Nov 17 15:55:23 2024

@author: gurkan
gurkansahin28@gmail.com



APPENDIX
--------

    1. Torus Properties
    -------------------
        Radius1 (Length): 
        -----------------
            The radius of the circular path of the torus.
            The default is 10mm.

        Radius2 (Length):
        ----------------
            The radius of the circular profile of the torus.
            The default is 2mm.

        Angle1 (Angle):
        --------------
            The start angle of the circular profile.
            Valid range: -180° <= value <= 180°. 
            The default is -180°.

        Angle2 (Angle):
        --------------
            The end angle the circular profile.
            Valid range: -180° <= value <= 180°.
            The default is 180°.
            If the total angle of the circular profile is smaller than 360°,
            the profile will have a pie-shape.

        Angle3 (Angle):
        -------------- 
            The angle of the circular path of the torus.
            Valid range: 0° < value <= 360°.
            The default is 360°.
            If it is smaller than 360° the resulting solid will be a segment of a torus.

    2. Default Values of The Torus
    ------------------------------
        Radius1: 10.00 mm
        Radius2: 2.00 mm
        Angle1: -180 deg    -180° <= value <= 180°
        Angle2: 180 deg     -180° <= value <= 180°
        Angle3: 360 deg     0° < value <= 360°


    3. QSlider
    ----------

        QSlider API Link:
        ----------------
            https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSlider.html


        QSlider's set of signals:
        ------------------------

            Signal              Description
            -------             -----------
            valueChanged()      Emitted when the slider's value has changed. The tracking() determines whether this signal is emitted during user interaction.

            sliderPressed()     Emitted when the user starts to drag the slider.

            sliderMoved()       Emitted when the user drags the slider.

            sliderReleased()    Emitted when the user releases the slider.

'''

### A. IMPORST
## 1. Importing required libraries as aliases
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
## 2. Importing some specific parts from libraries
# a. Importing Units for value types of length and angle
from FreeCAD import Units # type: ignore 
# b. Importing QtGui for building the macro interface
from PySide import QtGui # type: ignore
# c. Importing Qt for assigning the Slider property
from PySide.QtCore import Qt # type: ignore
# d. Importing datetime for creating unique doc name
from datetime import datetime

### B. SPECIFIC FUNCTIONS
## 1. Setting up the Gui for visualization
def setVisual():
    GuiView = Gui.ActiveDocument.ActiveView
    GuiView.viewIsometric()
    GuiView.setAxisCross(True)
    GuiView.fitAll()
    #Gui.runCommand('Draft_ToggleGrid', 0)
    '''Above line works when Draft workbench auto-loaded.'''
    pass

## 2. Creating a unique name for the new document
def uniqueDocName(topic='Doc'):
    ## Obtaining the date time information
    # Now
    now = datetime.now()
    # extracting the year as two-digit year
    year = now.strftime('%y')
    # extracting the month from the now
    month = now.month
    # extracting the day from the now
    day = now.day
    # extracting the hour from the now
    hour = now.strftime('%H')
    # extracting the minute from the now
    minutes = now.minute
    # extracting the seconds from the now
    seconds = now.strftime('%S')
    # preparing the docName
    specificDocName = f'{topic}_{year}-{month}-{day}_{hour}-{minutes}-{seconds}'
    # returning a string as a specific unique name
    return specificDocName

## 3. The updater function for the Torus parameters 
def updateMyTorus(objName, r1, r2, a1, a2, a3):
    # the getter for the given object name selecting from the document
    torus = doc.getObject(objName)
    # the distance from object center to the profil circle center
    torus.Radius1 = Units.Quantity(r1, Units.Length).Value
    # the distance of the profile circle between its center and circumference
    torus.Radius2 = Units.Quantity(r2, Units.Length).Value
    # the first slicer angle starting from inside of the torus then top, bottom and to the beginning 
    torus.Angle1 = Units.Quantity(a1, Units.Angle).Value
    # the second slicer angle starting from inside of the torus then bottom, top and to the beginning
    torus.Angle2 = Units.Quantity(a2, Units.Angle).Value
    # the third slicer angle for the profile circle to sweep
    torus.Angle3 = Units.Quantity(a3, Units.Angle).Value
    doc.recompute()
    pass

### C. THE DOCUMENT
## 1. Preparing a unique document name 
docName = uniqueDocName(topic='Torus')
## 2. Creating a document given unique name
doc = App.newDocument(docName)

### D. GLOBAL VALUES
## 1. Preparing default values for the Torus object
# a. Radius1: a distance from the torus center to the circle center
defR1 = 10 # the default value for Radius 1
# b. Radius2: a distance from the circle center to its circumference
defR2 = 2 # the default vaule for Radius 2
# c. Angle1: A slicer angle to slice the profile circle from the top (top arc)
defA1 = -180 # the default value for Angle 1: -180° <= value <= 180°
# d. Angle2: A slicer angle to slice the profile circle from the bottom (bottom arc)
defA2 = 180 # the default value for Angle 2: -180° <= value <= 180°
# e. Angle3: An angle for the profile circle to sweep
defA3 = 360 # the default value for Angle 3: 0° < value <= 360°

### E. TORUS OBJECT
# giving a name to the object to be created
objName = 'MyTorus'
# Torus object from Part library
objFromLib = 'Part::Torus'
# adding a torus to the document with the given name
obj = doc.addObject(objFromLib, objName)
doc.recompute()
#Preparing the Gui for visualizing
setVisual()


### F. BUILDING INTERFACE
class TorusUpdatersUI(QtGui.QWidget):
    '''A class for a simple interface to control torus properties interactively.
    After obtaining the parent Application position, it appears and
    contains five sliders to control the Torus object properties.
    Each slider is connected to the event of changing value.'''
    # From outline of the widget to the its inside
    def __init__(self): # the constructor of the class
        # Reaching inherited class constructor and start it
        super().__init__() # starts QtGui.QWidget constructor
        
        ## 1. Child Widget's Setup 
        # a. Naming the user interface
        self.setWindowTitle("Change Your Torus!") # child widget's title name
        # Obtaining the parent application geometry
        parent = QtGui.QApplication.activeWindow() # getter for the FreeCAD app window
        pGeometry = parent.geometry() # the getter for the parent geo bundle
        pGeoX = pGeometry.x() # the getter for the X axis of the parent
        pGeoY = pGeometry.y() # the getter for the Y axis of the parent
        # Setting the child application geometry
        factor = 50 # the variable for shifting amount as pixel
        cGeoX = pGeoX + factor # setting the child widget's X position 
        cGeoY = pGeoY + factor # setting the child widget's Y position
        width = 300 # the variable for the child widget's width
        height = 200 # the variable for the child widget's height
        # attending values of the child widget's properties to the ui geo
        self.setGeometry(cGeoX, cGeoY, width, height)
        
        # b. Creating the layout of the ui's items
        layout = QtGui.QVBoxLayout() # Vertical Layout of the items
        
        # c. Slider 1 setup for the Radius 1
        defValueRadius1 = defR1 # reaching the global variable of Radius1
        minValueRadius1 = 1 # determining the minimum value
        maxValueRadius1 = 15 # determining the maximum value
        # defining the label
        labelRadius1Text = f"Radius1: {defValueRadius1}"
        self.labelRadius1 = QtGui.QLabel(labelRadius1Text)
        # adding the label to the layout
        layout.addWidget(self.labelRadius1)
        # defining the slider 
        self.sliderRadius1 = QtGui.QSlider(Qt.Horizontal) # to slide horizontally
        self.sliderRadius1.setMinimum(minValueRadius1) # setting min value
        self.sliderRadius1.setMaximum(maxValueRadius1) # setting max value
        self.sliderRadius1.setValue(defValueRadius1) # setting appearance value
        # connecting the function to slider behaviours
        self.sliderRadius1.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderRadius1)
        
        
        # d. Slider 2 setup for the Radius 2
        defValueRadius2 = defR2 # reaching the global variable of Radius2
        minValueRadius2 = 1 # determining the minimum value
        maxValueRadius2 = 15 # determining the maximum value
        # defining the label
        labelRadius2Text = f"Radius2: {defValueRadius2}"
        self.labelRadius2 = QtGui.QLabel(labelRadius2Text)
        # adding the label to the layout
        layout.addWidget(self.labelRadius2)
        # defining the slider 
        self.sliderRadius2 = QtGui.QSlider(Qt.Horizontal) # to slide horizontally
        self.sliderRadius2.setMinimum(minValueRadius2) # setting min value
        self.sliderRadius2.setMaximum(maxValueRadius2) # setting max value
        self.sliderRadius2.setValue(defValueRadius2) # setting the appearance value
        # connecting the function to slider behaviours
        self.sliderRadius2.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderRadius2)
        
        
        # e. Slider 3 setup for the Angle 1
        # defining the Angle1 values
        defValueAngle1 = defA1 # reaching the global variable of Angle 1
        minValueAngle1 = -180 # setting min value
        maxValueAngle1 = 180 # setting max value
        # defining the label
        labelAngle1Text = f"Angle1: {defValueAngle1}"
        self.labelAngle1 = QtGui.QLabel(labelAngle1Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle1)
        # defining the slider 
        self.sliderAngle1 = QtGui.QSlider(Qt.Horizontal) # to slide horizontally
        self.sliderAngle1.setMinimum(minValueAngle1) # setting min value
        self.sliderAngle1.setMaximum(maxValueAngle1) # setting min value
        self.sliderAngle1.setValue(defValueAngle1) # setting the appearance value
        # connecting the function to slider behaviours
        self.sliderAngle1.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle1)      


        # f. Slider 4 setup for the Angle 2
        # defining the Angle1 values
        defValueAngle2 = defA2 # reaching the global variable of Angle 2
        minValueAngle2 = -180 # setting min value
        maxValueAngle2 = 180 # setting max value
        # defining the label
        labelAngle2Text = f"Angle2: {defValueAngle2}"
        self.labelAngle2 = QtGui.QLabel(labelAngle2Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle2)
        # defining the slider 
        self.sliderAngle2 = QtGui.QSlider(Qt.Horizontal) # to slide horizontally
        self.sliderAngle2.setMinimum(minValueAngle2) # setting min value
        self.sliderAngle2.setMaximum(maxValueAngle2) # setting max value
        self.sliderAngle2.setValue(defValueAngle2) # setting the appearance value
        # connecting the function to slider behaviours
        self.sliderAngle2.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle2)


        # g. Slider 5 setup for the Angle 3
        # defining the Angle3 values
        defValueAngle3 = defA3 # reaching the global variable of Angle 3
        minValueAngle3 = 0 # setting min value
        maxValueAngle3 = 360 # setting max value
        # defining the label
        labelAngle3Text = f"Angle3: {defValueAngle3}"
        self.labelAngle3 = QtGui.QLabel(labelAngle3Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle3)
        # defining the slider 
        self.sliderAngle3 = QtGui.QSlider(Qt.Horizontal)
        self.sliderAngle3.setMinimum(minValueAngle3)
        self.sliderAngle3.setMaximum(maxValueAngle3)
        self.sliderAngle3.setValue(defValueAngle3)
        # connecting the function to slider behaviours
        self.sliderAngle3.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle3)
        

        ## 2. Set the layout
        self.setLayout(layout)
        ### The End of The User Interface
    
    ## 3. The updating function for the slider labels' values
    def updateLabelValues(self, value):
        '''This function updates the label values 
        by obtaining the sliders' position values.'''
        # getters
        radius1 = self.sliderRadius1.value() # getting existing value of Radius1
        radius2 = self.sliderRadius2.value() # getting existing value of Radius2
        angle1 = self.sliderAngle1.value() # getting existing value of Angle1
        angle2 = self.sliderAngle2.value() # getting existing value of Angle2
        angle3 = self.sliderAngle3.value() # getting existing value of Angle3
        
        # setters for labels
        self.labelRadius1.setText(f"Radius1: {radius1}") # setting the label of Radius1
        self.labelRadius2.setText(f"Radius2: {radius2}") # setting the label of Radius2
        self.labelAngle1.setText(f"Angle1: {angle1}") # setting the label of Angle1
        self.labelAngle2.setText(f"Angle2: {angle2}") # setting the label of Angle2
        self.labelAngle3.setText(f"Angle3: {angle3}") # setting the label of Angle3
        
        # calling the updateMyTorus function
        '''Whenever the updateLabelValues function triggers, 
        the updateMyTorus function will be triggered.'''
        updateMyTorus(objName, radius1, radius2, angle1, angle2, angle3)
        
        
### G. DECLARING AN INSTANCE
if __name__ == "__main__":
    '''As in the Singleton design pattern there must be only one Application.
    The rest of it could be its instance.'''
    myApp = QtGui.QApplication.instance()

    # Apply a dark theme css to the user interface (the child widget)
    myWidget = TorusUpdatersUI()
    myWidget.setStyleSheet("""
        QWidget {
            background-color: #2e2e2e;
            color: #ffffff;
        }        
        QSlider::groove:horizontal {
            background: #555;
            height: 6px; /* Adjust groove height */
            border-radius: 4px; /* Groove rounded edges */
        }
        QSlider::handle:horizontal {
            background: #aaa;
            border: 2px solid #777;
            border-radius: 5px; /* Ensure it's circular */
            width: 10px; /* Match width and height for a perfect circle */
            height: 10px;
            margin: -6px 0; /* Align handle properly with groove */
        }
        QLabel {
            font-size: 14px;
        }
    """)
    # Showing the user interface widget for the action
    myWidget.show()
    #myApp.exec()


