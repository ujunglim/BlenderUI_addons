import bpy

class ChangeSize(bpy.types.Operator):
    bl_idname = "view3d.size_plane"
    bl_label = "Size Plane"

    def execute(self,context):
        context.object.size  = context.scene.Size
        print(9999)

        return {"FINISHED"}



#================================================================
def changeSizeRegister(): 
    bpy.utils.register_class(ChangeSize)

def changeSizeUnregister(): 
    bpy.utils.unregister_class(ChangeSize)