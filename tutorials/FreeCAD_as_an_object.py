#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
source: https://wiki.freecad.org/FreeCAD_API
Created on Sun Nov 10 23:56:24 2024

@author: gurkan
"""

import FreeCAD

print (FreeCAD.listDocuments())

mydoc = FreeCAD.activeDocument()



FreeCAD.ConfigDump()
'''Description: Prints a dictionary containing all the FreeCAD configuration environment.'''


FreeCAD.ConfigGet(['string'])
'''Description: Returns the value of the given key. 
If no key is given, the complete configuration is returned'''


FreeCAD.ConfigSet('string', 'string')
'''Description: Set the given key (first string) to the given value (second string).'''


FreeCAD.Version()
'''Description: Prints the FreeCAD version.'''


FreeCAD.activeDocument()
'''Description: Return the active document or None if there is no active document.'''
# Returns: A FreeCAD Document.


FreeCAD.addExportType('string', 'string')
'''Description: Adds a new export file type to FreeCAD. 
The first string must be formatted like this example: "Word Document (*.doc)". 
The second string is the name of a python script/module containing an export() function.'''


FreeCAD.addImportType('string', 'string')
'''Description: Adds a new import file type to FreeCAD, works the same way as addExportType, 
the handling python module must contain an open() and/or an import() function.'''

docName = 'NewDocument'
FreeCAD.closeDocument(docName)
'''Description: Closes the given document'''


FreeCAD.getDocument(docName)
'''Description: Returns a document or raise an exception if there is no document with the given name.'''


FreeCAD.getExportType('string')
'''Description: Returns the name of the module that can export the specified filetype.'''
# Returns: A string.

FreeCAD.getImportType('string')
'''Description: Returns the name of the module that can import the specified filetype.'''
# Returns: A string.


FreeCAD.listDocuments( )
'''Description: Returns a dictionary of names and object pointers of all documents.'''
# Returns: A dictionary of names and object pointers.


FreeCAD.newDocument(docName, hidden=False)
'''Description: Creates and returns a new document with a given name. 
The document name must be unique, which is checked automatically. 
If no name is supplied, the document will be named "Untitled". 
If hidden=True is passed, then FreeCAD in GUI mode won't display the document and 
won't show a tab for the document; 
this allows performing automatic operations on a temporary document 
(or create a document and save it) without disrupting the user interface.'''
# Returns: The newly created document.


FreeCAD.open('string')
'''Description: See openDocument'''

filepath = ''
FreeCAD.openDocument(filepath, hidden=False)
'''Description: Creates and returns a document and load a project file into the document. 
The string argument must point to an existing file. 
If the file doesn't exist or the file cannot be loaded an I/O exception is thrown. 
In this case the created document is kept, but will be empty. 
If hidden=True is passed, then FreeCAD in GUI mode won't display the document and 
won't show a tab for the document; 
this allows performing automatic operations on a document and 
close it without disrupting the user interface.'''
# Returns: The opened FreeCAD Document.

FreeCAD.setActiveDocument(docName)
'''Description: Set the active document by its name. '''
