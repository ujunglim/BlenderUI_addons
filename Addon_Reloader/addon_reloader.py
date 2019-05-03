bl_info = {
    "name": "YuJung's Addon Reloader",
    "category": "3D View",
    "author": "Lim Yu Jung"
}

import tempfile
import os
import shutil
import glob
import bpy
import sys

class Reload_Addon(bpy.types.Operator):
    bl_idname = "view3d.reload_addon" 
    bl_label = "Reload Yujung's Addon"

    def execute(self,context):
        addon_folder = 'UI_Editor'

        source_path = os.path.abspath(bpy.data.filepath+ "/../../..")
        #source_path = 'd:/Workspace/BlenderUI_addons'

        files_mask = '*.py'
        add_files_names = []

        addon_path = os.path.join(source_path, addon_folder)

        files = glob.glob(os.path.join(addon_path, files_mask)) + [os.path.join(addon_path, file) for file in add_files_names]

        with tempfile.TemporaryDirectory() as temp_dir:

            addon_folder_to_files = os.path.join(temp_dir, addon_folder, addon_folder)

            os.makedirs(addon_folder_to_files)

            for file in files:
                shutil.copy(file, addon_folder_to_files)

            addon_folder_to_zip = os.path.join(temp_dir, addon_folder)

            shutil.make_archive(addon_folder_to_zip, 'zip', addon_folder_to_zip)

            addon_zip_path = addon_folder_to_zip + '.zip'

            bpy.ops.wm.addon_disable(module = addon_folder)
            bpy.ops.wm.addon_remove(module = addon_folder)

            for module in list(sys.modules.keys()):
                if hasattr(sys.modules[module], '__package__'):
                    if(sys.modules[module].__package__ == addon_folder):
                        del sys.modules[module]

            bpy.ops.wm.addon_install(filepath = addon_zip_path, overwrite = True)
            bpy.ops.wm.addon_enable(module = addon_folder)
        return {"FINISHED"}

class YJ_UI_reload_panel(bpy.types.Panel):
    bl_label = "Yujung's Reload Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_category = "Create"
    
    def draw(self,context):
        self.layout.operator("view3d.reload_addon",text = "Reload")

def register(): 
    bpy.utils.register_class(Reload_Addon)
    bpy.utils.register_class(YJ_UI_reload_panel)
    
def unregister():
    bpy.utils.unregister_class(YJ_UI_reload_panel)
    bpy.utils.unregister_class(Reload_Addon)

if __name__ == "__main__":
    register()