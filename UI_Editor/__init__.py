bl_info = {
    "name": "YuJung's Blender",
    "category": "3D View",
    "author": "Lim Yu Jung"
}

import bpy,os
import math
import mathutils
from bpy.types import Header, Menu

    
class YJ_UI_PANEL(bpy.types.Panel):
    bl_label = "Make YuJung UI"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_category = "Create"
    
    def updateMove(self,context):
        bpy.ops.view3d.move_cube()
    
    bpy.types.Scene.Location= bpy.props.IntVectorProperty(
        name = "Location",
        description = "Location of object",
        default =(5,5,5),
        min = -5,
        max = 10,
        update = updateMove,
        subtype = "XYZ"
    )
    
    def draw(self,context):
        layout = self.layout
        row = layout.row(align = True)
        row.label(text = "uu")
        row.label(text = "stephen")
      
        row = layout.row()
        row.label(text = "bbb")
        
        #A
        box = layout.box()
        row = box.row(align = True)
        row.label(text = "add")
        
        layout.separator()

        #B
        box = layout.box()
        row = box.row(align = True)
        row.label(text = "st")
        
        #Change Location UI
        col = layout.column()
        col.prop(context.scene, "Location")
        
        
class Move(bpy.types.Operator):
    bl_idname = "view3d.move_cube" 
    bl_label = "Move Cube"
    
    def execute(self,context):
        context.object.location = context.scene.Location

        code = """
        function createUI()
        {
            var advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("UI");
                        
            var button = BABYLON.GUI.Button.CreateImageOnlyButton("but", "textures/grass.png");
            button.width = 0.2;
            button.height = "40px";
            button.color = "white";
            button.background = "green";
            advancedTexture.addControl(button);
            
            button = BABYLON.GUI.Button.CreateImageOnlyButton("but", "textures/grass.png");
            button.top = "0px";
            button.left = "0px";
            button.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
            button.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;
            button.width = 0.2;
            button.height = "40px";
            button.color = "white";
            button.background = "green";
            advancedTexture.addControl(button);
        }
        """

        file = open(os.path.abspath(bpy.data.filepath+ "/../UI/UI.js"), "w")
        file.write(code)
        file.close()
        
        return {"FINISHED"}
    

def register():
    bpy.utils.register_class(YJ_UI_PANEL)
    bpy.utils.register_class(Move)

def unregister():
    bpy.utils.unregister_class(YJ_UI_PANEL)
    bpy.utils.unregister_class(Move)
    
    
if __name__ == "__main__":
    register()