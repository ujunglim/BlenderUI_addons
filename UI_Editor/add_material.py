import bpy

class AddMaterial(bpy.types.Operator):
    bl_idname = "view3d.add_material" 
    bl_label = "Add Material"
    
    def execute(self,context):
        bpy.ops.material.new()
        print(1111)
        return {"FINISHED"}


#================================================================
def addMaterialRegister(): 
    bpy.utils.register_class(AddMaterial)


def addMaterialUnregister(): 
    bpy.utils.unregister_class(AddMaterial)