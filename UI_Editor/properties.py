import bpy

    # bpy.types.Scene.ExpectSalary= bpy.props.IntProperty(
    #     name = "Salary", 
    #     description = "Expected salary",
    #     default = 6600,
    #     min = 0,
    #     max = 100000
    # )

    # bpy.types.Scene.BaseSalary= bpy.props.IntProperty(
    #     name = "BaseSalary",
    #     description = "Base salary",
    #     default = 5000,
    #     min = 0,
    #     max = 100000
    # )

    # bpy.types.Scene.TaxRate= bpy.props.FloatProperty(
    #     name = "Tax rate",
    #     description = "tax rate",
    #     default = 0.2,
    #     min = 0,
    #     max = 0.3
    # )

    # bpy.types.Scene.FinalSalary= bpy.props.FloatProperty(
    #     name = "Result",
    #     description = "Final Salary",
    #     default = 0,
    #     min = 0,
    #     max = 1000000
    # )

def propertiesRegister():
    
    bpy.types.Scene.Location= bpy.props.FloatVectorProperty(
        name = "Location",
        description = "Location of object",
        default =(0,0,0),
        min = -5,
        max = 10,
        update = lambda self,context: bpy.ops.view3d.move_cube(),
        subtype = "XYZ"
    )

    bpy.types.Scene.LockLocation= bpy.props.BoolVectorProperty(
        name = "Lock",
        description = "Lock editing of location in the interface",
        default = (False,False,False),
        update = lambda self,context: bpy.ops.view3d.lock_location(),
        subtype = "NONE",
        size = 3
    )


    bpy.types.Object.Width = bpy.props.FloatProperty(
        name = "Width",
        description = "Width of object",
        default = 1,
        min = 1,
        max = 100,
        update = lambda self,context: bpy.ops.view3d.size_plane(),
        subtype = 'NONE'
    )

    bpy.types.Object.Height = bpy.props.FloatProperty(
        name = "Height",
        description = "Height of object",
        default = 1,
        min = 1,
        max = 100,
        update = lambda self,context: bpy.ops.view3d.size_plane(),
        subtype = 'NONE'
    )

def propertiesUnregister():
    del bpy.types.Scene.Location
    del bpy.types.Object.Height
    del bpy.types.Object.Width
    # del bpy.types.Scene.ExpectSalary
    # del bpy.types.Scene.BaseSalary
    # del bpy.types.Scene.TaxRate
    # del bpy.types.Scene.FinalSalary
    