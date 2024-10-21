#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:52:44 2024

@author: gurkan
"""

>>> doc = App.newDocument("SupportedTypes")
>>> # App.setActiveDocument("SupportedTypes")
>>> # App.ActiveDocument=App.getDocument("SupportedTypes")
>>> # Gui.ActiveDocument=Gui.getDocument("SupportedTypes")
>>> doc.supportedTypes()
['App::DocumentObject', 'App::GeoFeature', 'App::FeatureTest', 'App::FeatureTestException', 
 'App::FeatureTestColumn', 'App::FeatureTestRow', 'App::FeatureTestAbsAddress', 
 'App::FeatureTestPlacement', 'App::FeatureTestAttribute', 
 'App::FeaturePython', 'App::GeometryPython', 'App::DocumentObjectGroup', 
 'App::DocumentObjectGroupPython', 'App::DocumentObjectFileIncluded', 
 'Image::ImagePlane', 'App::InventorObject', 'App::VRMLObject', 'App::Annotation', 
 'App::AnnotationLabel', 'App::MeasureDistance', 'App::MaterialObject', 
 'App::MaterialObjectPython', 'App::TextDocument', 'App::Placement', 
 'App::PlacementPython', 'App::OriginFeature', 'App::Plane', 'App::Line', 
 'App::Part', 'App::Origin', 'App::Link', 'App::LinkPython', 'App::LinkElement', 
 'App::LinkElementPython', 'App::LinkGroup', 'App::LinkGroupPython', 
 'Part::Feature', 'Part::FeatureExt', 'Part::BodyBase', 'Part::FeaturePython', 
 'Part::FeatureGeometrySet', 'Part::CustomFeature', 'Part::CustomFeaturePython', 
 'Part::Primitive', 'Part::Box', 'Part::Spline', 'Part::Boolean', 
 'Part::Common', 'Part::MultiCommon', 'Part::Cut', 'Part::Fuse', 'Part::MultiFuse', 
 'Part::Section', 'Part::FilletBase', 'Part::Fillet', 'Part::Chamfer', 
 'Part::Compound', 'Part::Compound2', 'Part::Extrusion', 'Part::Revolution', 
 'Part::Mirroring', 'Part::ImportStep', 'Part::ImportIges', 'Part::ImportBrep', 
 'Part::CurveNet', 'Part::Polygon', 'Part::Circle', 'Part::Ellipse', 'Part::Vertex', 
 'Part::Line', 'Part::Ellipsoid', 'Part::Plane', 'Part::Sphere', 'Part::Cylinder', 
 'Part::Prism', 'Part::RegularPolygon', 'Part::Cone', 'Part::Torus', 'Part::Helix', 
 'Part::Spiral', 'Part::Wedge', 'Part::Part2DObject', 'Part::Part2DObjectPython', 
 'Part::Face', 'Part::RuledSurface', 'Part::Loft', 'Part::Sweep', 'Part::Offset', 
 'Part::Offset2D', 'Part::Thickness', 'Part::Refine', 'Part::Reverse', 'Part::Datum', 
 'Sketcher::SketchObjectSF', 'Sketcher::SketchObject', 'Sketcher::SketchObjectPython']
>>> 
