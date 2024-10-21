
import FreeCAD as App
import FreeCADGui as Gui

def makeShape(shape_type, **kwargs):
    # Check if a document is active, otherwise create a new one
    if not App.ActiveDocument:
        doc = App.newDocument()

    # Create a shape based on the provided shape_type
    if shape_type == 'cone':
        obj = App.ActiveDocument.addObject('Part::Cone', 'MyCone')
        obj.Radius1 = kwargs.get('radius1', 50)  # Base radius
        obj.Radius2 = kwargs.get('radius2', 0)   # Top radius
        obj.Height = kwargs.get('height', 100)
        obj.Angle = kwargs.get('angle', 360)
        
    elif shape_type == 'cylinder':
        obj = App.ActiveDocument.addObject('Part::Cylinder', 'MyCylinder')
        obj.Radius = kwargs.get('radius', 50)
        obj.Height = kwargs.get('height', 100)
        
    elif shape_type == 'box':
        obj = App.ActiveDocument.addObject('Part::Box', 'MyBox')
        obj.Length = kwargs.get('length', 100)
        obj.Width = kwargs.get('width', 50)
        obj.Height = kwargs.get('height', 50)
        
    elif shape_type == 'sphere':
        obj = App.ActiveDocument.addObject('Part::Sphere', 'MySphere')
        obj.Radius = kwargs.get('radius', 50)
        obj.Angle1 = kwargs.get('angle1', -90)  # Start angle (lower hemisphere)
        obj.Angle2 = kwargs.get('angle2', 90)   # End angle (upper hemisphere)
        obj.Angle3 = kwargs.get('angle3', 360)  # Sweeping angle

    else:
        print(f"Shape type '{shape_type}' is not recognized.")
        return None
    
    # Set the position of the object
    px = kwargs.get('px', 0)
    py = kwargs.get('py', 0)
    pz = kwargs.get('pz', 0)
    obj.Placement.Base = App.Vector(px, py, pz)

    # Recompute to apply changes and adjust the view
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView('ViewFit')
    Gui.activeDocument().activeView().viewAxometric()
    
    return obj  # Return the created object for further manipulation if needed

# Example usage:
# Creating a cone
makeShape('cone', radius1=50, radius2=20, height=80, px=10, py=20, pz=0)

# Creating a cylinder
makeShape('cylinder', radius=30, height=70, px=50, py=50, pz=0)

# Creating a box
makeShape('box', length=60, width=40, height=30, px=0, py=0, pz=10)

# Creating a sphere
makeShape('sphere', radius=40, angle1=-45, angle2=45, px=100, py=100, pz=0)
#############################################################################
