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
from bpy.types import Operator, PropertyGroup
from bpy.props import BoolProperty, PointerProperty
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


def vse_opengl_render_handler(dummy):
    bpy.ops.render.opengl(animation=False, render_keyed_only=False, sequencer=True)


def vse_sync_changed_func(self, context):

    if context.scene.vse_mask.vse_sync:
        if not vse_opengl_render_handler in bpy.app.handlers.frame_change_post:
            bpy.app.handlers.frame_change_post.append(vse_opengl_render_handler)
    else:
        if vse_opengl_render_handler in bpy.app.handlers.frame_change_post:
            bpy.app.handlers.frame_change_post.remove(vse_opengl_render_handler)


class VSEMaskSettings(PropertyGroup):

    vse_sync : BoolProperty(
        name="Sync VSE",
        description="Keep Render Layer in sync with VSE frames",
        default = False,
        update = vse_sync_changed_func
        )

class VSEMASK_PT_panel_1(bpy.types.Panel):
    bl_label = "VSE Masking"
    bl_category = "VSE Masking"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        vse_mask = scene.vse_mask

        layout.prop(vse_mask, "vse_sync", text="Sync VSE")


def register():
    bpy.utils.register_class(VSEMASK_PT_panel_1)
    bpy.utils.register_class(VSEMaskSettings)
    bpy.types.Scene.vse_mask = PointerProperty(type=VSEMaskSettings)

def unregister():
    bpy.utils.unregister_class(VSEMASK_PT_panel_1)
    del bpy.types.Scene.vse_sync

if __name__ == "__main__":
    register()
