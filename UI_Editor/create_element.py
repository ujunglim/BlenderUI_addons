import bpy

class CreateElement(bpy.types.Operator):
    bl_idname = "view3d.create_element" 
    bl_label = "Create Element"
    
    def execute(self,context):
        bpy.ops.mesh.primitive_plane_add()
        return {"FINISHED"}


#================================================================
def createElementRegister():
    bpy.utils.register_class(CreateElement)


def createElementUnregister():
    bpy.utils.unregister_class(CreateElement)