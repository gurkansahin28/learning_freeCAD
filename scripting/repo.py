# https://wiki.freecad.org/Draft_Line
####################################


# The Draft Line command creates a straight line.
# A Draft Line is in fact a Draft Wire with only two points.

import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
####################################

# The Draft Wire command creates a polyline, a sequence of several connected line segments.
# The command can also be used to join Draft Lines and Draft Wires.

import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()

####################################
# The Draft Fillet command creates a fillet, a rounded corner, or a chamfer, a straight edge, between two selected edges. 
# In version 0.21 and below the command only works properly if both selected edges are straight.

import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

edge1 = Draft.make_line(p1, p2)
edge2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([edge1, edge2], radius=500)

doc.recompute()
####################################

# The Draft Arc command creates a circular arc on the current working plane from a center, a radius, a start angle and an aperture angle. The radius and the angles can be defined by picking points.

# A Draft Arc is in fact a Draft Circle with a DataFirst Angle that is not the same as its DataLast Angle.

import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()


####################################


####################################

