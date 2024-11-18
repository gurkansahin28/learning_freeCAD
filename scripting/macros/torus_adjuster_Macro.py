
"""
Created on Sun Nov 17 15:55:23 2024

@author: gurkan
"""

'''
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSlider.html

QSlider inherits a comprehensive set of signals:

Signal              Description
-------             -----------
valueChanged()      Emitted when the slider's value has changed. The tracking() determines whether this signal is emitted during user interaction.

sliderPressed()     Emitted when the user starts to drag the slider.

sliderMoved()       Emitted when the user drags the slider.

sliderReleased()    Emitted when the user releases the slider.

'''
from PySide import QtGui # type: ignore
from PySide2.QtCore import Qt
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
from datetime import datetime
from FreeCAD import Units # type: ignore 

#-------- CREATING DOCUMENT ------------------------------------
### PREPARING THE DOCUMENT NAME UNIQUE ###
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
specificDocName = f'Torus_{year}-{month}-{day}-{hour}-{minutes}-{seconds}'
# creating the document with specific unique name
doc = App.newDocument(specificDocName)
# defining default values for the object
defR1 = 10
defR2 = 2
defA1 = -180
defA2 = 180
defA3 = 360
# giving a name to the object to be created
specificObjName = 'MyTorus'
# Torus object from Part library
objFromLib = 'Part::Torus'
# adding a torus to the document with the given name
obj = doc.addObject(objFromLib, specificObjName)
doc.recompute()
# selecting the created torus
selectedObj = doc.getObject(specificObjName)
selectedObj.Radius1 = Units.Quantity(defR1, Units.Length).Value
selectedObj.Radius2 = Units.Quantity(defR2, Units.Length).Value
selectedObj.Angle1 = Units.Quantity(defA1, Units.Angle).Value
selectedObj.Angle2 = Units.Quantity(defA2, Units.Angle).Value
selectedObj.Angle3 = Units.Quantity(defA3, Units.Angle).Value
doc.recompute()

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()



#--- BUILDING INTERFACE ----------------------------------------
class TorusUpdatersUI(QtGui.QWidget):
    def __init__(self):
        
        super().__init__()
        
        ### Child Widget's Setup #################
        # naming the widget
        self.setWindowTitle("Change Your Torus!")
        # Obtaining the parent application geometry
        parent = QtGui.QApplication.activeWindow()
        pGeometry = parent.geometry()
        pGeoX = pGeometry.x()
        pGeoY = pGeometry.y()
        # Setting the child application geometry
        factor = 50
        cGeoX = pGeoX + factor
        cGeoY = pGeoY + factor
        width = 300
        height = 200
        self.setGeometry(cGeoX, cGeoY, width, height)
        
        ### The Head of The Layout Setup ############
        # Creating the main layout
        layout = QtGui.QVBoxLayout()
        
        ### Radius1: The Begining of the Radius1 Setup ########
        defValueRadius1 = defR1
        minValueRadius1 = 1
        maxValueRadius1 = 15
        # A Label for Radius1
        # defining the label
        labelRadius1Text = f"Radius1: {defValueRadius1}"
        self.labelRadius1 = QtGui.QLabel(labelRadius1Text)
        # adding the label to the layout
        layout.addWidget(self.labelRadius1)
        
        # A Slider for Radius1
        # defining the slider 
        self.sliderRadius1 = QtGui.QSlider(Qt.Horizontal)
        self.sliderRadius1.setMinimum(minValueRadius1)
        self.sliderRadius1.setMaximum(maxValueRadius1)
        self.sliderRadius1.setValue(defValueRadius1)
        # connecting the function to slider behaviours
        self.sliderRadius1.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderRadius1)
        ### The End of the Radius1 Setup ##############
        
        
        ### Radius2: The Begining of the Radius2 Setup ########
        # A Label for Radius2
        # defining Radius2 Values
        defValueRadius2 = defR2
        minValueRadius2 = 1
        maxValueRadius2 = 15
        # defining the label
        labelRadius2Text = f"Radius2: {defValueRadius2}"
        self.labelRadius2 = QtGui.QLabel(labelRadius2Text)
        # adding the label to the layout
        layout.addWidget(self.labelRadius2)
        # A Slider for Radius2
        # defining the slider 
        self.sliderRadius2 = QtGui.QSlider(Qt.Horizontal)
        self.sliderRadius2.setMinimum(minValueRadius2)
        self.sliderRadius2.setMaximum(maxValueRadius2)
        self.sliderRadius2.setValue(defValueRadius2)
        # connecting the function to slider behaviours
        self.sliderRadius2.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderRadius2)
        ### The End of the Radius2 Setup ##############        
        
        
        
        ### Angle1: The Begining of the Angle1 Setup ########
        # defining the Angle1 values
        defValueAngle1 = defA1
        minValueAngle1 = -180
        maxValueAngle1 = 180        
        # A Label for Angle1
        # defining the label
        labelAngle1Text = f"Angle1: {defValueAngle1}"
        self.labelAngle1 = QtGui.QLabel(labelAngle1Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle1)
        
        # A Slider for Angle1
        # defining the slider 
        self.sliderAngle1 = QtGui.QSlider(Qt.Horizontal)
        self.sliderAngle1.setMinimum(minValueAngle1)
        self.sliderAngle1.setMaximum(maxValueAngle1)
        self.sliderAngle1.setValue(defValueAngle1)
        # connecting the function to slider behaviours
        self.sliderAngle1.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle1)
        ### The End of the Angle1 Setup ##############        


        ### Angle2: The Begining of the Angle2 Setup ########
        # defining the Angle1 values
        defValueAngle2 = defA2
        minValueAngle2 = -180
        maxValueAngle2 = 180        
        # A Label for Angle2
        # defining the label
        labelAngle2Text = f"Angle2: {defValueAngle2}"
        self.labelAngle2 = QtGui.QLabel(labelAngle2Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle2)
        
        # A Slider for Angle2
        # defining the slider 
        self.sliderAngle2 = QtGui.QSlider(Qt.Horizontal)
        self.sliderAngle2.setMinimum(minValueAngle2)
        self.sliderAngle2.setMaximum(maxValueAngle2)
        self.sliderAngle2.setValue(defValueAngle2)
        # connecting the function to slider behaviours
        self.sliderAngle2.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle2)
        ### The End of the Angle2 Setup ##############    



        ### Angle3: The Begining of the Angle3 Setup ########
        # defining the Angle3 values
        defValueAngle3 = defA3
        minValueAngle3 = 0
        maxValueAngle3 = 360
        # A Label for Angle3
        # defining the label
        labelAngle3Text = f"Angle3: {defValueAngle3}"
        self.labelAngle3 = QtGui.QLabel(labelAngle3Text)
        # adding the label to the layout
        layout.addWidget(self.labelAngle3)
        
        # A Slider for Angle3
        # defining the slider 
        self.sliderAngle3 = QtGui.QSlider(Qt.Horizontal)
        self.sliderAngle3.setMinimum(minValueAngle3)
        self.sliderAngle3.setMaximum(maxValueAngle3)
        self.sliderAngle3.setValue(defValueAngle3)
        # connecting the function to slider behaviours
        self.sliderAngle3.valueChanged.connect(self.updateLabelValues)
        # adding the slider to the layout
        layout.addWidget(self.sliderAngle3)
        ### The End of the Angle3 Setup ##############    


        
        # Set the layout
        self.setLayout(layout)
        ### The End of The Layout Setup ##################
    
    # the updating function for the slider labels' values
    def updateLabelValues(self, value):
        # getters
        radius1 = self.sliderRadius1.value()
        radius2 = self.sliderRadius2.value()
        angle1 = self.sliderAngle1.value()
        angle2 = self.sliderAngle2.value()
        angle3 = self.sliderAngle3.value()
        
        # setters for labels
        self.labelRadius1.setText(f"Radius1: {radius1}")
        self.labelRadius2.setText(f"Radius2: {radius2}")
        self.labelAngle1.setText(f"Angle1: {angle1}")
        self.labelAngle2.setText(f"Angle2: {angle2}")
        self.labelAngle3.setText(f"Angle3: {angle3}")
        
        # calling the updateMyTorus function
        updateMyTorus(radius1, radius2, angle1, angle2, angle3)
        
        

if __name__ == "__main__":
    myApp = QtGui.QApplication.instance()
########

    # Apply a dark theme
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
#########

    myWidget.show()
    myApp.exec_()
#--- THE END OF BUILDING INTERFACE ------------------------------------

def updateMyTorus(r1, r2, a1, a2, a3):
    selectedObj = doc.getObject(specificObjName)
    selectedObj.Radius1 = Units.Quantity(r1, Units.Length).Value
    selectedObj.Radius2 = Units.Quantity(r2, Units.Length).Value
    selectedObj.Angle1 = Units.Quantity(a1, Units.Angle).Value
    selectedObj.Angle2 = Units.Quantity(a2, Units.Angle).Value
    selectedObj.Angle3 = Units.Quantity(a3, Units.Angle).Value
    doc.recompute()
    pass
