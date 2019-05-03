import bpy
    # bpy.types.Scene.Size = bpy.props.IntProperty(
    #     name = "Size",
    #     description = "Size of object",
    #     default = 0,
    #     min = 0,
    #     max = 10,
    #     subtype = 'NONE'
    # )

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
    bpy.types.Scene.width = bpy.props.IntProperty(
        name = "Width",
        description = "Size of object",
        default = 0,
        min = 0,
        max = 10,
        subtype = 'NONE'
    )

    bpy.types.Scene.height = bpy.props.IntProperty(
        name = "Height",
        description = "Size of object",
        default = 0,
        min = 0,
        max = 10,
        subtype = 'NONE'
    )
    
    bpy.types.Scene.Location= bpy.props.IntVectorProperty(
        name = "Location",
        description = "Location of object",
        default =(5,5,5),
        min = -5,
        max = 10,
        update = lambda self,context: bpy.ops.view3d.move_cube(),
        subtype = "XYZ"
    )

def propertiesUnregister():
    del bpy.types.Scene.Location
    del bpy.types.Scene.height
    del bpy.types.Scene.width
    # del bpy.types.Scene.ExpectSalary
    # del bpy.types.Scene.BaseSalary
    # del bpy.types.Scene.TaxRate
    # del bpy.types.Scene.FinalSalary
    