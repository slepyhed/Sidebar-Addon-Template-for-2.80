# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import bpy

#use the next line to import classes from other files
#from . import other_classes

gui_active_panel = None

bl_info = {
    "name": "Template",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > New Tab",
    "description": "A blank template for addons",
    "warning": "",
    'wiki_url': "https://github.com/",
    'tracker_url': 'https://github.com/',
    "category": "Animation"
}

def start_doing():
    #do setup things here
    scn = bpy.context.scene

class ButtonLibraryOff(bpy.types.Operator):
    bl_label = 'Library'
    bl_idname = 'control.button_library_off'
    bl_description = 'Close library panel'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        global gui_active_panel
        gui_active_panel = None
        return {'FINISHED'}


class ButtonLibraryOn(bpy.types.Operator):
    bl_label = 'Library'
    bl_idname = 'control.button_library_on'
    bl_description = 'Open library panel'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        global gui_active_panel
        gui_active_panel = 'library'
        return {'FINISHED'}


class Finalize(bpy.types.Operator):

    bl_label = 'Finalize'
    bl_idname = 'control.finalize'
    bl_description = 'Finalize all the things'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        scn = bpy.context.scene
        #finalize something
        print("Finalized")
        return {'FINISHED'}


class ResetParameters(bpy.types.Operator):
    """Reset all morphings."""
    bl_label = 'Reset'
    bl_idname = 'control.reset_allproperties'
    bl_description = 'Reset all parameters'
    bl_context = 'objectmode'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        #reset something
        print("Reset")
        return {'FINISHED'}

class VIEW3D_PT_tools_Template(bpy.types.Panel):

    bl_label = "Version {0}.{1}.{2}".format(bl_info["version"][0], bl_info["version"][1], bl_info["version"][2])
    bl_idname = "TEMPLATE_PT_Template_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = 'objectmode'
    bl_category = "Template"



    def draw(self, context):

        global mblab_humanoid, gui_status, gui_err_msg, gui_active_panel
        scn = bpy.context.scene
        icon_expand = "DISCLOSURE_TRI_RIGHT"
        icon_collapse = "DISCLOSURE_TRI_DOWN"

        self.layout.operator("control.reset_allproperties", icon="RECOVER_LAST")


        if gui_active_panel != "library":
            self.layout.operator('control.button_library_on', icon=icon_expand)
        else:
            self.layout.operator('control.button_library_off', icon=icon_collapse)
            box = self.layout.box()
            box.label(text="Library")
            #add library things here

        self.layout.operator("control.finalize", icon='FREEZE')

        self.layout.label(text="FOOTER AREA")
        self.layout.label(
            text="put an important tip here", icon="INFO")




classes = (
    ButtonLibraryOff,
    ButtonLibraryOn,
    Finalize,
    ResetParameters,
    VIEW3D_PT_tools_Template,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
