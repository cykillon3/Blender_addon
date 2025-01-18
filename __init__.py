bl_info = {
    "name" : "CY's VRC addon",
    "author" : "CYkillone",
    "version" : (1, 0),
    "blender" : (4, 30, 2),
    "location" : "View3D > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Avatar Optimization",
}


import os
import sys

# Gets the directory of the current script
addon_dir = os.path.dirname(os.path.abspath(__file__))

# Adds the directory to the sys.path if not already there
if addon_dir not in sys.path:
    sys.path.append(addon_dir)



import bpy

from cy_panels import Model_PT_Panel, Model_Options_PT_Panel, Import_Model_PT_Panel
#from . import cy_panels

classes = (Model_PT_Panel, Model_Options_PT_Panel, Import_Model_PT_Panel)
        
        
        
        
        
def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
if __name__== "__main__":
    register()