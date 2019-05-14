import bpy

class AddTexture(bpy.types.Operator):
    bl_idname = "view3d.add_texture" 
    bl_label = "Add Texture"
    
    def execute(self,context):
        bpy.ops.texture.new()
        print("ADD Texture........................")
        return {"FINISHED"}


#================================================================
def addTextureRegister(): 
    bpy.utils.register_class(AddTexture)


def addTexutreUnregister(): 
    bpy.utils.unregister_class(AddTexture)