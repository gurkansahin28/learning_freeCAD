
import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft

docName = 'CreationCones'
doc = App.newDocument(docName)

App.setActiveDocument("CreationCones")
App.ActiveDocument=App.getDocument("CreationCones")
Gui.ActiveDocument=Gui.getDocument("CreationCones")

r_bottom = 0
r_top = 5
height = 10
cone = Part.makeCone(r_bottom, r_top, height)
coneObj = doc.addObject('Part::Feature', 'MyCone')
coneObj.Shape = cone
doc.recompute()

coneOther = doc.addObject('Part::Cone', 'MyOtherCone')
coneOther.Radius1 = r_bottom
coneOther.Radius2 = r_top
coneOther.Height = height
coneOther.Placement.Base = App.Vector(3, 3, 0)
doc.recompute()

Gui.activeDocument().activeView().viewTrimetric()
Gui.SendMsgToActiveView("ViewFit")

# intersection: common
from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_common(["MyCone", "MyOtherCone", ])

# undo
Gui.runCommand('Std_Undo',0)

# union
from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_fuse(["MyCone", "MyOtherCone", ])

# undo
Gui.runCommand('Std_Undo',0)

# difference
from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_cut(["MyCone", "MyOtherCone", ])

# undo
Gui.runCommand('Std_Undo',0)

from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_section(["MyCone", "MyOtherCone", ])

# undo
Gui.runCommand('Std_Undo',0)

# App.setActiveDocument("")
# App.ActiveDocument=None
# Gui.ActiveDocument=None
