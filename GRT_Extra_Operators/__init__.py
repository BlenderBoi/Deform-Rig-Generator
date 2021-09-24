import bpy
from . import GRT_Constraint_To_Armature
from . import GRT_Constraint_Toogle
from . import GRT_Remove_Animation_Data
from . import GRT_Remove_BBone
from . import GRT_Remove_Bone_Shape
from . import GRT_Remove_Custom_Property
from . import GRT_Remove_Non_Deform_Bone
from . import GRT_Batch_Rename_Actions

from . import GRT_Clear_All_Bones_Constraints
from . import GRT_Move_All_Bones_To_Layer
from . import GRT_Unlock_Bones_Transform
from . import GRT_Flatten_Hierarchy
from . import GRT_Disconnect_All_Bones

modules = [GRT_Disconnect_All_Bones, GRT_Flatten_Hierarchy, GRT_Unlock_Bones_Transform, GRT_Move_All_Bones_To_Layer, GRT_Clear_All_Bones_Constraints, GRT_Batch_Rename_Actions, GRT_Constraint_To_Armature, GRT_Constraint_Toogle, GRT_Remove_Animation_Data, GRT_Remove_BBone, GRT_Remove_Bone_Shape, GRT_Remove_Custom_Property, GRT_Remove_Non_Deform_Bone]

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
