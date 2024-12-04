import bpy
from . import mod_data as md

from . import mod_functions
from .mod_functions import *


def auto_weight_on_select(context):

    if bpy.context.selected_pose_bones == None:
        return

    if bpy.context.window_manager.cc_props.edit_mode == False:

        return

    ccp = bpy.context.window_manager.cc_props
    last_selected = ccp["map_editor"]["last_selected"]

    if bpy.context.active_object.name != ccp.source_rig_name:
        return

    if len(bpy.context.selected_pose_bones) > 1:
        return

    if len(bpy.context.selected_pose_bones) == 0:
        if last_selected == "":

            return

        if last_selected in ccp["remap_stored"]["rename"]:
            print("04: resetting last_selected:", last_selected)
            auto_weight_colors(bone=last_selected, state="reset")

        ccp["map_editor"]["last_selected"] = ""
        return

    if len(bpy.context.selected_pose_bones) > 1:

        if ccp["map_editor"]["last_selected"] != "":

            auto_weight_colors(bone=last_selected, state="reset")

            ccp["map_editor"]["last_selected"] = ""
        return

    if len(bpy.context.selected_pose_bones) == 1:
        bone = bpy.context.selected_pose_bones[0].name

    else:
        print("--- THIS ERROR SHOULD NOT HAPPEN ---")
        return

    if ccp["map_editor"]["last_selected"] == bone:

        return

    if bone in ccp["remap_stored"]["rename"]:

        if last_selected != "":

            if last_selected in ccp["remap_stored"]["rename"]:

                auto_weight_colors(bone=last_selected, state="reset")

        auto_weight_colors(bone=bone, state="active")

    else:
        if last_selected != "":
            if last_selected in ccp["remap_stored"]["rename"]:

                auto_weight_colors(bone=last_selected, state="reset")

    ccp["map_editor"]["last_selected"] = bone


def auto_weight_colors(bone="", state=""):
    if bone == "":
        print("auto_weight_colors reports: empty bone name")
        return False
    if state == "":
        print("auto_weight_colors reports: empty state name")
        return False

    obj = bpy.data.objects
    ccp = bpy.context.window_manager.cc_props

    bpy.app.handlers.depsgraph_update_post.remove(auto_weight_on_select)

    arm = bpy.context.active_object.name
    if state == "active":
        boneCollection = obj[arm].data.collections.get(md.cc_rename_selected_name)
        if boneCollection == None:            
            boneCollection = obj[arm].data.collections.new(md.cc_rename_selected_name)                 
            obj[arm].data.collections.new(md.cc_reskin_selected_name)
            
        boneObj = (bpy.data.objects[arm].pose.bones[bone];
        boneCollection.assign(boneObj)
        boneObj.palette = md.cc_rename_selected_color

        if bone in ccp["remap_stored"]["reskin"]:
            for child in ccp["remap_stored"]["reskin"][bone]:
                boneObj = bpy.data.objects[arm].pose.bones[child]
                bpy.data.objects[arm].data.collections[md.cc_reskin_selected_name].assign(boneObj)
                boneObj.palette = md.cc_reskin_selected_color

    elif state == "reset":
        bpy.data.objects[arm].data.collections[md.cc_rename_group].assign(bpy.data.objects[arm].pose.bones[bone])
        if bone in ccp["remap_stored"]["reskin"]:
            for child in ccp["remap_stored"]["reskin"][bone]:
                bpy.data.objects[arm].data.collections[md.cc_reskin_group].assign(bpy.data.objects[arm].pose.bones[child])

    print("auto_weight_colors reports: exiting with bone and state:", bone, state)

    bpy.app.handlers.depsgraph_update_post.append(auto_weight_on_select)

    return
