import bpy

class YJ_UI_PANEL(bpy.types.Panel):
    bl_label = "Make YuJung UI"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_category = "Create"
    
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

        #Create Element
        layout.operator("view3d.create_element",text = "Create Element")

        layout.separator()
        # #Calculate Salary
        # layout.prop(context.scene,"ExpectSalary")
        # layout.prop(context.scene,"BaseSalary")
        # layout.prop(context.scene,"TaxRate")
        # layout.operator("view3d.calculate_salary",text = "Calculate Salary")
        # layout.prop(context.scene,"FinalSalary")

        #Add Material
        #layout.operator("view3d.add_material",text = "Add Material")

        #Change object Size
        layout.separator()
        row.label(text = "Change Size")
        row = layout.row(align = True)
        row.prop(context.scene, "size")



#================================================================
def panelRegister():
    bpy.utils.register_class(YJ_UI_PANEL)


def panelUnregister():
    bpy.utils.unregister_class(YJ_UI_PANEL)
        
        
        
        