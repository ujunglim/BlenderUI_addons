import bpy

class ChangeSize(bpy.types.Operator):
    bl_idname = "view3d.size_plane"
    bl_label = "Change size"

    def execute(self,context):
        context.object.dimensions[0] = context.object.Width
        context.object.dimensions[1] = context.object.Height
        # print(context.object.Width)
        # print(context.object.dimensions[0])
        

        print(context.object.dimensions[0])
        print(context.object.dimensions[1])
        print(context.object.dimensions[2])

        # print(context.object.Height)
        # print(context.object.dimensions[1])
       

        return {"FINISHED"}



#================================================================
def changeSizeRegister(): 
    bpy.utils.register_class(ChangeSize)

def changeSizeUnregister(): 
    bpy.utils.unregister_class(ChangeSize)