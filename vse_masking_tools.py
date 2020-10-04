bl_info = {
    "name": "VSE Masking Tools",
    "author": "John C. Quillan",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "FIXME",
    "description": "Syncs VSE to Images editor redner",
    "warning": "",
    "doc_url": "",
    "category": "VSE Masking",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


# Registration

# def add_object_button(self, context):
#     self.layout.operator(
#         OBJECT_OT_add_object.bl_idname,
#         text="Add Object",
#         icon='PLUGIN')




# This allows you to right click on a button and link to documentation
# def add_object_manual_map():
#     url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
#     url_manual_mapping = (
#         ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
#     )
#     return url_manual_prefix, url_manual_mapping

class VSEMASK_PT_panel_1(bpy.types.Panel):
    bl_label = "VSE Masking"
    bl_category = "VSE Masking"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is panel 1.")


def register():
    bpy.utils.register_class(VSEMASK_PT_panel_1)

def unregister():
    bpy.utils.unregister_class(VSEMASK_PT_panel_1)

if __name__ == "__main__":
    register()
