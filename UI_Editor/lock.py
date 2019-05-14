import bpy

class LockLocation(bpy.types.Operator):
    bl_idname = "view3d.lock_location" 
    bl_label = "Lock location"
    
    def execute(self,context):
        # context.object.location = context.scene.Location
        print("lock location..........................")
        
      
        return {"FINISHED"}



#================================================================
def moveRegister(): 
    bpy.utils.register_class(Move)

def moveUnregister(): 
    bpy.utils.unregister_class(Move)