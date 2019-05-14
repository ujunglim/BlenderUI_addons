bl_info = {
    "name": "YuJung's Blender",
    "category": "3D View",
    "author": "Lim Yu Jung"
}


# allow module to be changed during a session (dev purposes)

if "bpy" in locals():
    import imp
    imp.reload(panel)
    imp.reload(properties)
    imp.reload(move)
    imp.reload(lock)
    imp.reload(create_element)
    imp.reload(add_material)
    imp.reload(add_texture)
    imp.reload(change_size)
    imp.reload(topview_camera)
else:
    from .panel import (panelRegister,panelUnregister)
    from .properties import (propertiesRegister,propertiesUnregister)
    from .move import Move
    from .lock import LockLocation
    from .create_element import CreateElement
    from .add_material import AddMaterial
    from .add_texture import AddTexture
    from .change_size import ChangeSize
    from .topview_camera import TopviewCamera
    

from sys import modules
import bpy,os
import math
import mathutils
from bpy.types import Header, Menu




#==================================================================

# class CalculateSalary(bpy.types.Operator):
#     bl_idname = "view3d.calculate_salary" 
#     bl_label = "Calculate Salary"

#     def execute(self,context):
#         expectSalary = context.scene.ExpectSalary
#         baseSalary = context.scene.BaseSalary
#         taxRate = context.scene.TaxRate
#         context.scene.FinalSalary = (expectSalary - baseSalary)*(1-taxRate) + baseSalary

#         return {"FINISHED"}

#================================================================
def register(): 
    bpy.utils.register_class(Move)
    bpy.utils.register_class(LockLocation)
    bpy.utils.register_class(CreateElement)
    bpy.utils.register_class(AddMaterial)
    bpy.utils.register_class(AddTexture)
    bpy.utils.register_class(ChangeSize)
    bpy.utils.register_class(TopviewCamera)

    
    #bpy.utils.register_class(CalculateSalary) 

    propertiesRegister()
    panelRegister()
    
def unregister():
    bpy.utils.unregister_class(TopviewCamera)
    bpy.utils.unregister_class(ChangeSize)
    bpy.utils.unregister_class(AddTexture)
    bpy.utils.unregister_class(AddMaterial)
    bpy.utils.unregister_class(CreateElement)
    bpy.utils.unregister_class(LockLocation)
    bpy.utils.unregister_class(Move)
    # bpy.utils.unregister_class(CalculateSalary)

    panelUnregister()
    propertiesUnregister()


    
if __name__ == "__main__":
    register()