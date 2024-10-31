import FreeCAD

for obj in FreeCAD.ActiveDocument.Objects:
    if hasattr(obj,"Shape"):
        print("Object Label: ", obj.Label, ", Shape type: ", obj.Shape.TypeId, ", Object: ", obj)
