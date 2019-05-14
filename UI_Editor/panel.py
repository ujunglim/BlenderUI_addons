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
        
        layout.separator()

        #B
        box = layout.box()
        row1 = box.row(align = True)
        row1.label(text = "st")
        
        #Change Location UI
        
        rowLocation = layout.row()
        colLocation = rowLocation.column()
        colLocation.prop(context.scene, "Location")

        
        colLocationLock = rowLocation.column()
        colLocationLock.operator("view3d.lock_location", icon = "UNLOCKED")
        # colLocationLock.prop(context.scene,"LockLocation")

        #Change object Size
        rowSize = layout.row(align = True)
        rowSize.label(text = "Size")
        rowSize.prop(context.object, "Width")
        rowSize.prop(context.object, "Height")



        #Create Element
        layout.operator("view3d.create_element", text = "Create Element",icon = "ZOOMIN")

        #Add Material
        layout.operator("view3d.add_material",text = "Add Material", icon = "MATERIAL")

        rowMaterial = layout.row(align = True)
        rowMaterial.template_list("MATERIAL_UL_matslots", "", context.object, "material_slots", context.object, "active_material_index", rows=4)

        rowMaterialPreview = layout.row(align = True)
        rowMaterialPreview.template_preview(context.object.active_material)


        def active_node_mat(mat):
        # TODO, 2.4x has a pipeline section, for 2.5 we need to communicate
        # which settings from node-materials are used
            if mat is not None:
                mat_node = mat.active_node_material
                if mat_node:
                    return mat_node
                else:
                    return mat

            return None


        #diffuse 
        mat = active_node_mat(context.object.active_material)
        split = layout.split()
        row = split.row(align = True)
        row.prop(mat, "diffuse_color", text="")

        sub = row.row(align = True)
        sub.active = (not mat.use_shadeless)
        sub.prop(mat, "diffuse_intensity", text="Intensity")

        layout.separator()
        layout.separator()

        def context_tex_datablock(context):
            idblock = context.object.active_material
            if idblock:
                return active_node_mat(idblock)

            idblock = context.lamp
            if idblock:
                return idblock

            idblock = context.world
            if idblock:
                return idblock

            idblock = context.brush
            if idblock:
                return idblock

            idblock = context.line_style
            if idblock:
                return idblock

            if context.particle_system:
                idblock = context.particle_system.settings

            return idblock


        # def poll(cls, context):
        #     engine = context.scene.render.engine
        #     # if not (hasattr(context, "texture_slot") or hasattr(context, "texture_node")):
        #     #     return False
        #     return ((context.material or
        #             context.world or
        #             context.lamp or
        #             context.texture or
        #             context.line_style or
        #             context.particle_system or
        #             isinstance(context.space_data.pin_id, ParticleSettings) or
        #             context.texture_user) and
        #             (engine in cls.COMPAT_ENGINES))


        

        #Add Texture
        layout.operator("view3d.add_texture", text = "Add Texture", icon = "TEXTURE")

        # space = context.space_data
        idblock = context_tex_datablock(context)
        # pin_id = space.pin_id
        rowTexture = layout.row(align = True)
        rowTexture.template_list("TEXTURE_UL_texslots", "", idblock, "texture_slots", idblock, "active_texture_index", rows=2)


        
        # tex_collection = (pin_id is None) and (node is None) and (not isinstance(idblock, Brush))

        # if tex_collection:
        #     rowTexture = layout.row(align = True)
        #     rowTexture.template_list("TEXTURE_UL_texslots", "", idblock, "texture_slots", idblock, "active_texture_index", rows=2)

        #     col = row.column(align=True)
        #     col.operator("texture.slot_move", text="", icon='TRIA_UP').type = 'UP'
        #     col.operator("texture.slot_move", text="", icon='TRIA_DOWN').type = 'DOWN'
        #     col.menu("TEXTURE_MT_specials", icon='DOWNARROW_HLT', text="")

        # if tex_collection:
        #     layout.template_ID(idblock, "active_texture", new="texture.new")
        # elif node:
        #     layout.template_ID(node, "texture", new="texture.new")
        # elif idblock:
        #     layout.template_ID(idblock, "texture", new="texture.new")





        #Topview Camera
        layout.operator("view3d.topview_camera",text = "Topview Camera", icon ="SCENE" )

        
        # #Calculate Salary
        # layout.prop(context.scene,"ExpectSalary")
        # layout.prop(context.scene,"BaseSalary")
        # layout.prop(context.scene,"TaxRate")
        # layout.operator("view3d.calculate_salary",text = "Calculate Salary")
        # layout.prop(context.scene,"FinalSalary")



#================================================================
def panelRegister():
    bpy.utils.register_class(YJ_UI_PANEL)


def panelUnregister():
    bpy.utils.unregister_class(YJ_UI_PANEL)
        
        
        
        