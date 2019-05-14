import bpy,os

class Move(bpy.types.Operator):
    bl_idname = "view3d.move_cube" 
    bl_label = "Move Cube"
    
    def execute(self,context):
        context.object.location = context.scene.Location
        print("move object")
        
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

        file = open(os.path.abspath(bpy.data.filepath+ "/../../Web_Page/UI/UI.js"), "w")
        file.write(code)
        file.close()
        
        return {"FINISHED"}



#================================================================
def moveRegister(): 
    bpy.utils.register_class(Move)

def moveUnregister(): 
    bpy.utils.unregister_class(Move)