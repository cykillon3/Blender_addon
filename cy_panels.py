import bpy

from bpy.types import Panel


category_name = "CY"


class Model_PT_Panel(Panel):
    bl_label = "Model"
    bl_idname = "Model_PT_Panel_01"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = category_name
    
    def draw(self, context):
        
        layout = self.layout
        
        row = layout.row()
        
        row.label(text = "Add Objects", icon = "GHOST_ENABLED")
        
        row = layout.row()
        
        row.operator("mesh.primitive_cube_add", icon = "CUBE", text = "Add Cube")
        
        
class Model_Options_PT_Panel(Panel):
    bl_label = "Model Options"
    bl_idname = "Model_Options_PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = category_name
    
    
    def draw(self, context):
        
        layout = self.layout
        
        row = layout.row()
        
        row.label(text = "Add Objects", icon = "GHOST_ENABLED")
        
        row = layout.row()
        
        row.operator("mesh.primitive_cube_add", icon = "CUBE", text = "Add Cube")

class Import_Model_PT_Panel(Panel):
    bl_label = "Import Model"
    bl_idname = "Import_Model_PT_Panel_01"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = category_name
    
    
    
    def draw(self, context):
        
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Import Model", icon = "CUBE")
        
        row = layout.row()
        row.operator("import_scene.fbx", text = "Import FBX")
        
    

    