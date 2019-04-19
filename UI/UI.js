
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
            button.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
            button.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;
            button.width = 0.2;
            button.height = "40px";
            button.color = "white";
            button.background = "green";
            advancedTexture.addControl(button);
        button.left = '0px';button.top = '0px';
}