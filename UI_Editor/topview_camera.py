import bpy

class TopviewCamera(bpy.types.Operator):
    bl_idname = "view3d.topview_camera" 
    bl_label = "Topview Camera"
    
    def execute(self,context):
        bpy.ops.view3d.viewnumpad(type = 'TOP')
        return {"FINISHED"}


#================================================================
def TopviewCameraRegister():
    bpy.utils.register_class(TopviewCamera)


def TopviewCameraUnregister():
    bpy.utils.unregister_class(TopviewCamera)