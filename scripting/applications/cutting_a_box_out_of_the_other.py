import FreeCAD as App
import FreeCADGui as Gui

from pathlib import Path
from BOPTools import BOPFeatures


docName = "CuttingAboxOutOfTheOther"
doc = App.newDocument(docName)

#the following code block, to take the image of activeView 
imageWidth = 500
imageHeight = imageWidth

### adjustments for the view image to save #######################
imagesDir = Path("/home/gurkan/Documents/freeCAD_learning/scripting/screenShots")
imagesDir.mkdir(parents=True, exist_ok=True)
pathToImage = imagesDir / docName
pathToImageSuffixed = pathToImage.with_suffix(".png")
pathToImageString = str(pathToImageSuffixed)

### adjustment values for the boxes ##################
length = 10
width = 20
height = 30
extractionFactor = 5

### adjusting the Extractor Box ################################
extractorBox = doc.addObject("Part::Box", "ExtractorBox")
extractorBox.Length = length
extractorBox.Width = width
extractorBox.Height = height
doc.recompute()

### adjusting the Extracted Box ###############################
extractedBox = doc.addObject("Part::Box", "ExtractedBox")
extractedBox.Length = length - extractionFactor
extractedBox.Width = width - extractionFactor
extractedBox.Height = height
doc.recompute()

### implementation of the extraction (cut) ##################
bp = BOPFeatures.BOPFeatures(doc)
bp.make_cut(["ExtractorBox", "ExtractedBox", ])
doc.recompute()

### adjustments for the pose of activeView ###################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)

### saving the activeView into the defined path #################
Gui.activeDocument().activeView().saveImage(pathToImageString, imageWidth, imageHeight,'Current')
#exit()
# App.closeDocument(docName)
