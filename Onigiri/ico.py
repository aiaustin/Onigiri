import bpy
import os
from . import mod_settings
from .mod_settings import *

## https://docs.blender.org/api/current/bpy_types_enum_items/icon_items.html

script_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = script_dir + oni_settings["paths"]["icons"]

custom_icons = None
builtin_icons = None
map_icons = None

def load_icons():

    global custom_icons
    global map_icons
    global builtin_icons

    custom_icons = bpy.utils.previews.new()
    custom_icons.load("arrow_top_right", os.path.join(icons_dir, "arrow_top_right.png"), "IMAGE")
    custom_icons.load("arrow_bottom_right", os.path.join(icons_dir, "arrow_bottom_right.png"), "IMAGE")
    custom_icons.load("arrow_up", os.path.join(icons_dir, "arrow_up.png"), "IMAGE")
    custom_icons.load("arrow_right_green", os.path.join(icons_dir, "arrow_right_green.png"), "IMAGE")
    custom_icons.load("arrow_left_green", os.path.join(icons_dir, "arrow_left_green.png"), "IMAGE")
    custom_icons.load("configure", os.path.join(icons_dir, "configure.png"), "IMAGE")
    custom_icons.load("settings_general", os.path.join(icons_dir, "settings_general.png"), "IMAGE")
    custom_icons.load("settings_advanced", os.path.join(icons_dir, "settings_advanced.png"), "IMAGE")
    custom_icons.load("bone_source", os.path.join(icons_dir, "bone_source.png"), "IMAGE")
    custom_icons.load("bone_target", os.path.join(icons_dir, "bone_target.png"), "IMAGE")
    custom_icons.load("walking_green", os.path.join(icons_dir, "walking_green.png"), "IMAGE")
    custom_icons.load("walking_white", os.path.join(icons_dir, "walking_white.png"), "IMAGE")
    custom_icons.load(
        "walking_black", os.path.join(icons_dir, "walking_black.png"), "IMAGE"
    )
    custom_icons.load(
        "walking_blue", os.path.join(icons_dir, "walking_blue.png"), "IMAGE"
    )
    custom_icons.load(
        "walking_red", os.path.join(icons_dir, "walking_red.png"), "IMAGE"
    )
    custom_icons.load("follow", os.path.join(icons_dir, "follow.png"), "IMAGE")
    custom_icons.load("lead", os.path.join(icons_dir, "lead.png"), "IMAGE")

    custom_icons.load("map_bones", os.path.join(icons_dir, "map_bones.png"), "IMAGE")
    custom_icons.load(
        "map_bones_reverse", os.path.join(icons_dir, "map_bones_reverse.png"), "IMAGE"
    )
    custom_icons.load(
        "map_to_mbones", os.path.join(icons_dir, "map_to_mbones.png"), "IMAGE"
    )
    custom_icons.load(
        "map_to_template", os.path.join(icons_dir, "map_to_template.png"), "IMAGE"
    )
    custom_icons.load(
        "load_template", os.path.join(icons_dir, "load_template.png"), "IMAGE"
    )
    custom_icons.load("save", os.path.join(icons_dir, "save.png"), "IMAGE")
    custom_icons.load("save_dark", os.path.join(icons_dir, "save_dark.png"), "IMAGE")
    custom_icons.load("load", os.path.join(icons_dir, "load.png"), "IMAGE")
    custom_icons.load("reset", os.path.join(icons_dir, "reset.png"), "IMAGE")
    custom_icons.load(
        "reset_warning", os.path.join(icons_dir, "reset_warning.png"), "IMAGE"
    )
    custom_icons.load("fix_pose", os.path.join(icons_dir, "fix_pose.png"), "IMAGE")
    custom_icons.load("magnify", os.path.join(icons_dir, "magnify.png"), "IMAGE")
    custom_icons.load(
        "restore_bone", os.path.join(icons_dir, "restore_bone.png"), "IMAGE"
    )

    custom_icons.load("bone", os.path.join(icons_dir, "bone.png"), "IMAGE")
    custom_icons.load("bones", os.path.join(icons_dir, "bones.png"), "IMAGE")
    custom_icons.load("bones_blue", os.path.join(icons_dir, "bones_blue.png"), "IMAGE")
    custom_icons.load("bone_bent", os.path.join(icons_dir, "bone_bent.png"), "IMAGE")
    custom_icons.load("bone_fixed", os.path.join(icons_dir, "bone_fixed.png"), "IMAGE")
    custom_icons.load("bone_red", os.path.join(icons_dir, "bone_red.png"), "IMAGE")
    custom_icons.load("bone_blue", os.path.join(icons_dir, "bone_blue.png"), "IMAGE")
    custom_icons.load("bone_black", os.path.join(icons_dir, "bone_black.png"), "IMAGE")
    custom_icons.load("bone_green", os.path.join(icons_dir, "bone_green.png"), "IMAGE")
    custom_icons.load(
        "bone_yellow", os.path.join(icons_dir, "bone_yellow.png"), "IMAGE"
    )
    custom_icons.load("bone_mixed", os.path.join(icons_dir, "bone_mixed.png"), "IMAGE")
    custom_icons.load(
        "bone_black_red", os.path.join(icons_dir, "bone_black_red.png"), "IMAGE"
    )
    custom_icons.load(
        "bone_yellow_blue", os.path.join(icons_dir, "bone_yellow_blue.png"), "IMAGE"
    )
    custom_icons.load("joint", os.path.join(icons_dir, "joint.png"), "IMAGE")

    custom_icons.load(
        "view_anchor_bones", os.path.join(icons_dir, "view_anchor_bones.png"), "IMAGE"
    )
    custom_icons.load(
        "view_reskin_bones", os.path.join(icons_dir, "view_reskin_bones.png"), "IMAGE"
    )
    custom_icons.load(
        "view_output_bones", os.path.join(icons_dir, "view_output_bones.png"), "IMAGE"
    )

    custom_icons.load(
        "tail_to_head", os.path.join(icons_dir, "tail_to_head.png"), "IMAGE"
    )
    custom_icons.load("map", os.path.join(icons_dir, "map.png"), "IMAGE")
    custom_icons.load("create_rig", os.path.join(icons_dir, "create_rig.png"), "IMAGE")
    custom_icons.load(
        "create_neutral_rig", os.path.join(icons_dir, "create_neutral_rig.png"), "IMAGE"
    )
    custom_icons.load(
        "create_reference_rig",
        os.path.join(icons_dir, "create_reference_rig.png"),
        "IMAGE",
    )
    custom_icons.load(
        "export_animation", os.path.join(icons_dir, "export_animation.png"), "IMAGE"
    )

    custom_icons.load(
        "running_guy", os.path.join(icons_dir, "running_guy.png"), "IMAGE"
    )
    custom_icons.load(
        "running_guy_red", os.path.join(icons_dir, "running_guy_red.png"), "IMAGE"
    )
    custom_icons.load(
        "running_guy_enabled",
        os.path.join(icons_dir, "running_guy_enabled.png"),
        "IMAGE",
    )

    custom_icons.load(
        "rig_to_mesh", os.path.join(icons_dir, "rig_to_mesh.png"), "IMAGE"
    )
    custom_icons.load(
        "bones_to_mesh", os.path.join(icons_dir, "bones_to_mesh.png"), "IMAGE"
    )
    custom_icons.load(
        "remove_keys", os.path.join(icons_dir, "remove_keys.png"), "IMAGE"
    )
    custom_icons.load(
        "export_mesh", os.path.join(icons_dir, "export_mesh.png"), "IMAGE"
    )
    custom_icons.load("unlocked", os.path.join(icons_dir, "unlocked.png"), "IMAGE")
    custom_icons.load("lock_red", os.path.join(icons_dir, "lock_red.png"), "IMAGE")
    custom_icons.load("lock_green", os.path.join(icons_dir, "lock_green.png"), "IMAGE")
    custom_icons.load("lock_black", os.path.join(icons_dir, "lock_black.png"), "IMAGE")
    custom_icons.load(
        "locked_black", os.path.join(icons_dir, "locked_black.png"), "IMAGE"
    )
    custom_icons.load(
        "unlocked_black", os.path.join(icons_dir, "unlocked_black.png"), "IMAGE"
    )

    custom_icons.load(
        "create_reference_pose",
        os.path.join(icons_dir, "create_reference_pose.png"),
        "IMAGE",
    )
    custom_icons.load(
        "scale_animation", os.path.join(icons_dir, "scale_animation.png"), "IMAGE"
    )
    custom_icons.load(
        "remove_constraints", os.path.join(icons_dir, "remove_constraints.png"), "IMAGE"
    )
    custom_icons.load("control", os.path.join(icons_dir, "control.png"), "IMAGE")
    custom_icons.load("animation", os.path.join(icons_dir, "animation.png"), "IMAGE")
    custom_icons.load(
        "character_converter",
        os.path.join(icons_dir, "character_converter.png"),
        "IMAGE",
    )
    custom_icons.load(
        "connect_links", os.path.join(icons_dir, "connect_links.png"), "IMAGE"
    )
    custom_icons.load(
        "rename_to_targets", os.path.join(icons_dir, "rename_to_targets.png"), "IMAGE"
    )
    custom_icons.load(
        "remove_unused_bones",
        os.path.join(icons_dir, "remove_unused_bones.png"),
        "IMAGE",
    )
    custom_icons.load("no_bone", os.path.join(icons_dir, "no_bone.png"), "IMAGE")
    custom_icons.load(
        "add_missing_groups", os.path.join(icons_dir, "add_missing_groups.png"), "IMAGE"
    )
    custom_icons.load("apply_pose", os.path.join(icons_dir, "apply_pose.png"), "IMAGE")
    custom_icons.load(
        "custom_mapping", os.path.join(icons_dir, "custom_mapping.png"), "IMAGE"
    )

    custom_icons.load("x", os.path.join(icons_dir, "x.png"), "IMAGE")
    custom_icons.load("x_red", os.path.join(icons_dir, "x_red.png"), "IMAGE")
    custom_icons.load("x_blue", os.path.join(icons_dir, "x_blue.png"), "IMAGE")
    custom_icons.load("x_green", os.path.join(icons_dir, "x_green.png"), "IMAGE")
    custom_icons.load("x_black", os.path.join(icons_dir, "x_black.png"), "IMAGE")
    custom_icons.load("x_white", os.path.join(icons_dir, "x_white.png"), "IMAGE")
    custom_icons.load("x_mixed", os.path.join(icons_dir, "x_mixed.png"), "IMAGE")
    custom_icons.load("x_yellow", os.path.join(icons_dir, "x_yellow.png"), "IMAGE")
    custom_icons.load(
        "x_black_white", os.path.join(icons_dir, "x_black_white.png"), "IMAGE"
    )
    custom_icons.load(
        "x_white_black", os.path.join(icons_dir, "x_white_black.png"), "IMAGE"
    )

    custom_icons.load("info", os.path.join(icons_dir, "info.png"), "IMAGE")

    custom_icons.load("dot_red", os.path.join(icons_dir, "dot_red.png"), "IMAGE")
    custom_icons.load("dot_blue", os.path.join(icons_dir, "dot_blue.png"), "IMAGE")
    custom_icons.load("dot_white", os.path.join(icons_dir, "dot_white.png"), "IMAGE")
    custom_icons.load("dot_black", os.path.join(icons_dir, "dot_black.png"), "IMAGE")
    custom_icons.load("dot_green", os.path.join(icons_dir, "dot_green.png"), "IMAGE")
    custom_icons.load("dot_yellow", os.path.join(icons_dir, "dot_yellow.png"), "IMAGE")

    custom_icons.load("key_red", os.path.join(icons_dir, "key_red.png"), "IMAGE")
    custom_icons.load("key_blue", os.path.join(icons_dir, "key_blue.png"), "IMAGE")
    custom_icons.load("key_white", os.path.join(icons_dir, "key_white.png"), "IMAGE")
    custom_icons.load("key_black", os.path.join(icons_dir, "key_black.png"), "IMAGE")
    custom_icons.load("key_green", os.path.join(icons_dir, "key_green.png"), "IMAGE")
    custom_icons.load("key_yellow", os.path.join(icons_dir, "key_yellow.png"), "IMAGE")

    custom_icons.load("thumb_up", os.path.join(icons_dir, "thumb_up.png"), "IMAGE")
    custom_icons.load("thumb_down", os.path.join(icons_dir, "thumb_down.png"), "IMAGE")
    custom_icons.load(
        "thumb_up_green", os.path.join(icons_dir, "thumb_up_green.png"), "IMAGE"
    )
    custom_icons.load(
        "thumb_down_red", os.path.join(icons_dir, "thumb_down_red.png"), "IMAGE"
    )

    custom_icons.load(
        "integrity_check", os.path.join(icons_dir, "integrity_check.png"), "IMAGE"
    )
    custom_icons.load(
        "pose_library", os.path.join(icons_dir, "pose_library.png"), "IMAGE"
    )
    custom_icons.load("add", os.path.join(icons_dir, "add.png"), "IMAGE")
    custom_icons.load("subtract", os.path.join(icons_dir, "subtract.png"), "IMAGE")
    custom_icons.load("edit", os.path.join(icons_dir, "edit.png"), "IMAGE")
    custom_icons.load("edit_red", os.path.join(icons_dir, "edit_red.png"), "IMAGE")
    custom_icons.load("edit_rgb", os.path.join(icons_dir, "edit_rgb.png"), "IMAGE")
    custom_icons.load("edit_grey", os.path.join(icons_dir, "edit_grey.png"), "IMAGE")
    custom_icons.load("edit_white", os.path.join(icons_dir, "edit_white.png"), "IMAGE")
    custom_icons.load("selection", os.path.join(icons_dir, "selection.png"), "IMAGE")
    custom_icons.load("merge", os.path.join(icons_dir, "merge.png"), "IMAGE")
    custom_icons.load(
        "broken_link", os.path.join(icons_dir, "broken_link.png"), "IMAGE"
    )

    custom_icons.load("loop", os.path.join(icons_dir, "loop.png"), "IMAGE")
    custom_icons.load(
        "loop_enabled", os.path.join(icons_dir, "loop_enabled.png"), "IMAGE"
    )
    custom_icons.load("range", os.path.join(icons_dir, "range.png"), "IMAGE")
    custom_icons.load(
        "range_enabled", os.path.join(icons_dir, "range_enabled.png"), "IMAGE"
    )

    custom_icons.load("angle", os.path.join(icons_dir, "angle.png"), "IMAGE")
    custom_icons.load("roll", os.path.join(icons_dir, "roll.png"), "IMAGE")
    custom_icons.load("bake", os.path.join(icons_dir, "bake.png"), "IMAGE")
    custom_icons.load("store", os.path.join(icons_dir, "store.png"), "IMAGE")
    custom_icons.load("record", os.path.join(icons_dir, "record.png"), "IMAGE")
    custom_icons.load("tools", os.path.join(icons_dir, "tools.png"), "IMAGE")
    custom_icons.load("alert", os.path.join(icons_dir, "alert.png"), "IMAGE")
    custom_icons.load("head", os.path.join(icons_dir, "head.png"), "IMAGE")
    custom_icons.load("stabilize", os.path.join(icons_dir, "stabilize.png"), "IMAGE")
    custom_icons.load("prefix", os.path.join(icons_dir, "prefix.png"), "IMAGE")
    custom_icons.load(
        "prefix_remove", os.path.join(icons_dir, "prefix_remove.png"), "IMAGE"
    )
    custom_icons.load("reshape", os.path.join(icons_dir, "reshape.png"), "IMAGE")
    custom_icons.load(
        "assume_pose", os.path.join(icons_dir, "assume_pose.png"), "IMAGE"
    )
    custom_icons.load(
        "volume_bones", os.path.join(icons_dir, "volume_bones.png"), "IMAGE"
    )
    custom_icons.load(
        "spine_bones", os.path.join(icons_dir, "spine_bones.png"), "IMAGE"
    )
    custom_icons.load("all_bones", os.path.join(icons_dir, "all_bones.png"), "IMAGE")
    custom_icons.load("all_types", os.path.join(icons_dir, "all_types.png"), "IMAGE")
    custom_icons.load(
        "selected_bones", os.path.join(icons_dir, "selected_bones.png"), "IMAGE"
    )
    custom_icons.load("smooth", os.path.join(icons_dir, "smooth.png"), "IMAGE")
    custom_icons.load("undeform", os.path.join(icons_dir, "undeform.png"), "IMAGE")
    custom_icons.load(
        "check_white", os.path.join(icons_dir, "check_white.png"), "IMAGE"
    )
    custom_icons.load(
        "check_black", os.path.join(icons_dir, "check_black.png"), "IMAGE"
    )
    custom_icons.load("check_red", os.path.join(icons_dir, "check_red.png"), "IMAGE")
    custom_icons.load("check_blue", os.path.join(icons_dir, "check_blue.png"), "IMAGE")
    custom_icons.load(
        "check_green", os.path.join(icons_dir, "check_green.png"), "IMAGE"
    )
    custom_icons.load(
        "check_yellow", os.path.join(icons_dir, "check_yellow.png"), "IMAGE"
    )
    custom_icons.load("sl", os.path.join(icons_dir, "sl.png"), "IMAGE")
    custom_icons.load("skin", os.path.join(icons_dir, "skin.png"), "IMAGE")
    custom_icons.load(
        "menu_closed", os.path.join(icons_dir, "menu_closed.png"), "IMAGE"
    )
    custom_icons.load("menu_opened", os.path.join(icons_dir, "menu_opened.png"), "IMAGE")
    custom_icons.load("orientation", os.path.join(icons_dir, "orientation.png"), "IMAGE")
    custom_icons.load("off", os.path.join(icons_dir, "off.png"), "IMAGE")
    custom_icons.load("on", os.path.join(icons_dir, "on.png"), "IMAGE")
    custom_icons.load("choice_off", os.path.join(icons_dir, "choice_off.png"), "IMAGE")
    custom_icons.load("choice_on", os.path.join(icons_dir, "choice_on.png"), "IMAGE")
    custom_icons.load("choice_red", os.path.join(icons_dir, "choice_red.png"), "IMAGE")
    custom_icons.load(
        "choice_green", os.path.join(icons_dir, "choice_green.png"), "IMAGE"
    )
    custom_icons.load("sync", os.path.join(icons_dir, "sync.png"), "IMAGE")
    custom_icons.load("inherit", os.path.join(icons_dir, "inherit.png"), "IMAGE")
    custom_icons.load("linear", os.path.join(icons_dir, "linear.png"), "IMAGE")
    custom_icons.load("retarget", os.path.join(icons_dir, "retarget.png"), "IMAGE")
    custom_icons.load("proxy", os.path.join(icons_dir, "proxy.png"), "IMAGE")
    custom_icons.load("detach", os.path.join(icons_dir, "detach.png"), "IMAGE")
    custom_icons.load("anchor", os.path.join(icons_dir, "anchor.png"), "IMAGE")
    custom_icons.load("target", os.path.join(icons_dir, "target.png"), "IMAGE")
    custom_icons.load(
        "disable_map_pose", os.path.join(icons_dir, "disable_map_pose.png"), "IMAGE"
    )
    custom_icons.load("magic", os.path.join(icons_dir, "magic.png"), "IMAGE")
    custom_icons.load("hide_bones", os.path.join(icons_dir, "hide_bones.png"), "IMAGE")
    custom_icons.load(
        "hide_mapped_bones", os.path.join(icons_dir, "hide_mapped_bones.png"), "IMAGE"
    )
    custom_icons.load(
        "hide_anchor_branch_bones",
        os.path.join(icons_dir, "hide_anchor_branch_bones.png"),
        "IMAGE",
    )
    custom_icons.load(
        "isolation_mode", os.path.join(icons_dir, "isolation_mode.png"), "IMAGE"
    )
    custom_icons.load("isolate", os.path.join(icons_dir, "isolate.png"), "IMAGE")
    custom_icons.load(
        "reskin_bone", os.path.join(icons_dir, "reskin_bone.png"), "IMAGE"
    )
    custom_icons.load("glue", os.path.join(icons_dir, "glue.png"), "IMAGE")
    custom_icons.load("experiment", os.path.join(icons_dir, "experiment.png"), "IMAGE")
    custom_icons.load("curves", os.path.join(icons_dir, "curves.png"), "IMAGE")

    custom_icons.load("ease", os.path.join(icons_dir, "ease.png"), "IMAGE")
    custom_icons.load(
        "ease_enabled", os.path.join(icons_dir, "ease_enabled.png"), "IMAGE"
    )

    custom_icons.load("blank", os.path.join(icons_dir, "blank.png"), "IMAGE")
    custom_icons.load("eye", os.path.join(icons_dir, "eye.png"), "IMAGE")
    custom_icons.load("hammer", os.path.join(icons_dir, "hammer.png"), "IMAGE")
    custom_icons.load("calc", os.path.join(icons_dir, "calc.png"), "IMAGE")
    custom_icons.load("center", os.path.join(icons_dir, "center.png"), "IMAGE")
    custom_icons.load("sliders", os.path.join(icons_dir, "sliders.png"), "IMAGE")
    custom_icons.load("line_white", os.path.join(icons_dir, "line_white.png"), "IMAGE")
    custom_icons.load("line_black", os.path.join(icons_dir, "line_black.png"), "IMAGE")
    custom_icons.load("line_red", os.path.join(icons_dir, "line_red.png"), "IMAGE")
    custom_icons.load(
        "line_yellow", os.path.join(icons_dir, "line_yellow.png"), "IMAGE"
    )
    custom_icons.load("line_blue", os.path.join(icons_dir, "line_blue.png"), "IMAGE")
    custom_icons.load("line_green", os.path.join(icons_dir, "line_green.png"), "IMAGE")
    custom_icons.load(
        "line_thin_white", os.path.join(icons_dir, "line_thin_white.png"), "IMAGE"
    )
    custom_icons.load(
        "line_thin_black", os.path.join(icons_dir, "line_thin_black.png"), "IMAGE"
    )
    custom_icons.load("star_red", os.path.join(icons_dir, "star_red.png"), "IMAGE")
    custom_icons.load("star_black", os.path.join(icons_dir, "star_black.png"), "IMAGE")
    custom_icons.load("star_green", os.path.join(icons_dir, "star_green.png"), "IMAGE")
    custom_icons.load(
        "star_yellow", os.path.join(icons_dir, "star_yellow.png"), "IMAGE"
    )
    custom_icons.load("default", os.path.join(icons_dir, "default.png"), "IMAGE")
    custom_icons.load("neutral", os.path.join(icons_dir, "neutral.png"), "IMAGE")
    custom_icons.load(
        "shape_shifter", os.path.join(icons_dir, "shape_shifter.png"), "IMAGE"
    )
    custom_icons.load(
        "shape_shifter_green",
        os.path.join(icons_dir, "shape_shifter_green.png"),
        "IMAGE",
    )
    custom_icons.load(
        "shape_shifter_red", os.path.join(icons_dir, "shape_shifter_red.png"), "IMAGE"
    )
    custom_icons.load(
        "shape_shifter_navy", os.path.join(icons_dir, "shape_shifter_navy.png"), "IMAGE"
    )
    custom_icons.load(
        "shape_shifter_white",
        os.path.join(icons_dir, "shape_shifter_white.png"),
        "IMAGE",
    )
    custom_icons.load("peak", os.path.join(icons_dir, "peak_black.png"), "IMAGE")
    custom_icons.load("peak_black", os.path.join(icons_dir, "peak_black.png"), "IMAGE")
    custom_icons.load("peak_blue", os.path.join(icons_dir, "peak_blue.png"), "IMAGE")
    custom_icons.load("peak_green", os.path.join(icons_dir, "peak_green.png"), "IMAGE")
    custom_icons.load(
        "peak_orange", os.path.join(icons_dir, "peak_orange.png"), "IMAGE"
    )
    custom_icons.load("peak_red", os.path.join(icons_dir, "peak_red.png"), "IMAGE")
    custom_icons.load("peak_white", os.path.join(icons_dir, "peak_white.png"), "IMAGE")
    custom_icons.load(
        "peak_yellow", os.path.join(icons_dir, "peak_yellow.png"), "IMAGE"
    )
    custom_icons.load(
        "avastar_to_oni", os.path.join(icons_dir, "avastar_to_oni.png"), "IMAGE"
    )
    custom_icons.load("safe", os.path.join(icons_dir, "safe.png"), "IMAGE")
    custom_icons.load("match", os.path.join(icons_dir, "match.png"), "IMAGE")
    custom_icons.load("fitmesh", os.path.join(icons_dir, "fitmesh.png"), "IMAGE")
    custom_icons.load(
        "animation_start", os.path.join(icons_dir, "animation_start.png"), "IMAGE"
    )
    custom_icons.load("split", os.path.join(icons_dir, "split.png"), "IMAGE")
    custom_icons.load("mesh", os.path.join(icons_dir, "mesh.png"), "IMAGE")
    custom_icons.load("volume", os.path.join(icons_dir, "volume.png"), "IMAGE")

    custom_icons.load("rotate", os.path.join(icons_dir, "rotate.png"), "IMAGE")
    custom_icons.load("location", os.path.join(icons_dir, "location.png"), "IMAGE")
    custom_icons.load(
        "location_red", os.path.join(icons_dir, "location_red.png"), "IMAGE"
    )
    custom_icons.load(
        "location_blue", os.path.join(icons_dir, "location_blue.png"), "IMAGE"
    )
    custom_icons.load(
        "location_white", os.path.join(icons_dir, "location_white.png"), "IMAGE"
    )
    custom_icons.load(
        "location_enabled", os.path.join(icons_dir, "location_enabled.png"), "IMAGE"
    )
    custom_icons.load("rotation", os.path.join(icons_dir, "rotation.png"), "IMAGE")
    custom_icons.load(
        "rotation_red", os.path.join(icons_dir, "rotation_red.png"), "IMAGE"
    )
    custom_icons.load(
        "rotation_blue", os.path.join(icons_dir, "rotation_blue.png"), "IMAGE"
    )
    custom_icons.load(
        "rotation_white", os.path.join(icons_dir, "rotation_white.png"), "IMAGE"
    )

    custom_icons.load(
        "rotation_enabled", os.path.join(icons_dir, "rotation_enabled.png"), "IMAGE"
    )
    custom_icons.load("scale", os.path.join(icons_dir, "scale.png"), "IMAGE")
    custom_icons.load(
        "scale_enabled", os.path.join(icons_dir, "scale_enabled.png"), "IMAGE"
    )
    custom_icons.load(
        "scale_special", os.path.join(icons_dir, "scale_special.png"), "IMAGE"
    )
    custom_icons.load("transform", os.path.join(icons_dir, "transform.png"), "IMAGE")
    custom_icons.load(
        "transform_enabled", os.path.join(icons_dir, "transform_enabled.png"), "IMAGE"
    )

    custom_icons.load("transfer", os.path.join(icons_dir, "transfer.png"), "IMAGE")
    custom_icons.load(
        "properties_black", os.path.join(icons_dir, "properties_black.png"), "IMAGE"
    )
    custom_icons.load(
        "properties_white", os.path.join(icons_dir, "properties_white.png"), "IMAGE"
    )
    custom_icons.load("freeze", os.path.join(icons_dir, "freeze.png"), "IMAGE")
    custom_icons.load("thaw", os.path.join(icons_dir, "thaw.png"), "IMAGE")
    custom_icons.load("clean", os.path.join(icons_dir, "clean.png"), "IMAGE")
    custom_icons.load("fill", os.path.join(icons_dir, "fill.png"), "IMAGE")
    custom_icons.load("empty", os.path.join(icons_dir, "empty.png"), "IMAGE")
    custom_icons.load("cut", os.path.join(icons_dir, "cut.png"), "IMAGE")
    custom_icons.load("copy", os.path.join(icons_dir, "copy.png"), "IMAGE")
    custom_icons.load("paste", os.path.join(icons_dir, "paste.png"), "IMAGE")
    custom_icons.load("insert", os.path.join(icons_dir, "insert.png"), "IMAGE")
    custom_icons.load("play", os.path.join(icons_dir, "play.png"), "IMAGE")
    custom_icons.load("play_red", os.path.join(icons_dir, "play_red.png"), "IMAGE")
    custom_icons.load("play_blue", os.path.join(icons_dir, "play_blue.png"), "IMAGE")
    custom_icons.load("play_green", os.path.join(icons_dir, "play_green.png"), "IMAGE")
    custom_icons.load("play_white", os.path.join(icons_dir, "play_white.png"), "IMAGE")
    custom_icons.load(
        "play_yellow", os.path.join(icons_dir, "play_yellow.png"), "IMAGE"
    )
    custom_icons.load(
        "play_orange", os.path.join(icons_dir, "play_orange.png"), "IMAGE"
    )
    custom_icons.load("progress", os.path.join(icons_dir, "progress.png"), "IMAGE")
    custom_icons.load("flag", os.path.join(icons_dir, "flag.png"), "IMAGE")
    custom_icons.load("flag_on", os.path.join(icons_dir, "flag_on.png"), "IMAGE")
    custom_icons.load("flag_all", os.path.join(icons_dir, "flag_all.png"), "IMAGE")
    custom_icons.load("flag_none", os.path.join(icons_dir, "flag_none.png"), "IMAGE")
    custom_icons.load("deviation", os.path.join(icons_dir, "deviation.png"), "IMAGE")
    custom_icons.load("tolerance", os.path.join(icons_dir, "tolerance.png"), "IMAGE")
    custom_icons.load("sample", os.path.join(icons_dir, "sample.png"), "IMAGE")
    custom_icons.load("hand_love", os.path.join(icons_dir, "hand_love.png"), "IMAGE")
    custom_icons.load("full", os.path.join(icons_dir, "full.png"), "IMAGE")
    custom_icons.load("time", os.path.join(icons_dir, "time.png"), "IMAGE")
    custom_icons.load("hourglass", os.path.join(icons_dir, "hourglass.png"), "IMAGE")

    custom_icons.load("symmetric", os.path.join(icons_dir, "symmetric.png"), "IMAGE")

    custom_icons.load("paint", os.path.join(icons_dir, "paint.png"), "IMAGE")
    custom_icons.load(
        "paint_enabled", os.path.join(icons_dir, "paint_enabled.png"), "IMAGE"
    )
    custom_icons.load(
        "paint_disabled", os.path.join(icons_dir, "paint_disabled.png"), "IMAGE"
    )

    custom_icons.load("back_face", os.path.join(icons_dir, "back_face.png"), "IMAGE")
    custom_icons.load(
        "back_face_enabled", os.path.join(icons_dir, "back_face_enabled.png"), "IMAGE"
    )
    custom_icons.load(
        "back_face_disabled", os.path.join(icons_dir, "back_face_disabled.png"), "IMAGE"
    )

    custom_icons.load("link", os.path.join(icons_dir, "link.png"), "IMAGE")

    custom_icons.load("opensim", os.path.join(icons_dir, "opensim.png"), "IMAGE")
    custom_icons.load("controller", os.path.join(icons_dir, "controller.png"), "IMAGE")
    custom_icons.load("start", os.path.join(icons_dir, "start.png"), "IMAGE")

    custom_icons.load("action", os.path.join(icons_dir, "action.png"), "IMAGE")
    custom_icons.load("camera", os.path.join(icons_dir, "camera.png"), "IMAGE")
    custom_icons.load("camera_on", os.path.join(icons_dir, "camera_on.png"), "IMAGE")
    custom_icons.load("director", os.path.join(icons_dir, "director.png"), "IMAGE")
    custom_icons.load("to_actor", os.path.join(icons_dir, "to_actor.png"), "IMAGE")
    custom_icons.load(
        "director_blue", os.path.join(icons_dir, "director_blue.png"), "IMAGE"
    )
    custom_icons.load(
        "director_green", os.path.join(icons_dir, "director_green.png"), "IMAGE"
    )

    custom_icons.load("script", os.path.join(icons_dir, "script.png"), "IMAGE")
    custom_icons.load("code", os.path.join(icons_dir, "code.png"), "IMAGE")
    custom_icons.load(
        "code_disabled", os.path.join(icons_dir, "code_disabled.png"), "IMAGE"
    )

    custom_icons.load("nuke", os.path.join(icons_dir, "nuke.png"), "IMAGE")

    custom_icons.load("next", os.path.join(icons_dir, "next.png"), "IMAGE")
    custom_icons.load(
        "next_red_blue", os.path.join(icons_dir, "next_red_blue.png"), "IMAGE"
    )

    custom_icons.load(
        "select_ends", os.path.join(icons_dir, "select_ends.png"), "IMAGE"
    )
    custom_icons.load(
        "select_volumes", os.path.join(icons_dir, "select_volumes.png"), "IMAGE"
    )
    custom_icons.load(
        "select_attach", os.path.join(icons_dir, "select_attach.png"), "IMAGE"
    )
    custom_icons.load(
        "deselect_non_ends", os.path.join(icons_dir, "deselect_non_ends.png"), "IMAGE"
    )

    custom_icons.load("ik", os.path.join(icons_dir, "ik.png"), "IMAGE")
    custom_icons.load("object", os.path.join(icons_dir, "object.png"), "IMAGE")
    custom_icons.load("object_black", os.path.join(icons_dir, "object.png"), "IMAGE")
    custom_icons.load(
        "object_white", os.path.join(icons_dir, "object_white.png"), "IMAGE"
    )
    custom_icons.load("object_red", os.path.join(icons_dir, "object_red.png"), "IMAGE")
    custom_icons.load("dynamic", os.path.join(icons_dir, "dynamic.png"), "IMAGE")

    custom_icons.load("more", os.path.join(icons_dir, "more.png"), "IMAGE")
    custom_icons.load("global", os.path.join(icons_dir, "global.png"), "IMAGE")
    custom_icons.load("pull", os.path.join(icons_dir, "pull.png"), "IMAGE")
    custom_icons.load("master", os.path.join(icons_dir, "master.png"), "IMAGE")
    custom_icons.load("puppet", os.path.join(icons_dir, "puppet.png"), "IMAGE")
    custom_icons.load(
        "align_bones", os.path.join(icons_dir, "align_bones.png"), "IMAGE"
    )
    custom_icons.load("project", os.path.join(icons_dir, "project.png"), "IMAGE")
    custom_icons.load("pin", os.path.join(icons_dir, "pin.png"), "IMAGE")
    custom_icons.load(
        "inverse_motion", os.path.join(icons_dir, "inverse_motion.png"), "IMAGE"
    )

    custom_icons.load("nametag", os.path.join(icons_dir, "nametag.png"), "IMAGE")

    custom_icons.load("axis_x", os.path.join(icons_dir, "axis_x.png"), "IMAGE")
    custom_icons.load("axis_y", os.path.join(icons_dir, "axis_y.png"), "IMAGE")
    custom_icons.load("axis_z", os.path.join(icons_dir, "axis_z.png"), "IMAGE")

    custom_icons.load("unknown", os.path.join(icons_dir, "unknown.png"), "IMAGE")
    custom_icons.load("ragdoll", os.path.join(icons_dir, "ragdoll.png"), "IMAGE")

    
    icon_items = bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.items()    
    builtin_icons = {tup[1].identifier : tup[1].value for tup in icon_items}

    map_icons = {
        "panel_opened": "TRIA_DOWN",
        "panel_closed": "TRIA_RIGHT",
        "star_green": "ARMATURE_DATA",
        "axis_y" : "AXIS_FRONT",
        "axis": "EMPTY_AXIS",
        "tools": "TOOL_SETTINGS",
        "star": "SOLO_ON",
        "kit": "OUTLINER_OB_ARMATURE",
        "rotate": "ORIENTATION_GIMBAL",
        "clean": "BRUSH_DATA",
        "time": "PREVIEW_RANGE",
        "reset": "FILE_REFRESH",
        "load": "FILE_FOLDER"
    }

def unload_icons():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)    

## https://blender.stackexchange.com/questions/224015/is-there-a-way-to-get-icon-value-for-the-uilist-using-icon-name-from-enum

def get_icon_id(name):
    global custom_icons
    global builtin_icons
    icon_name = map_icons.get(name)    
    if icon_name is None:
        icon = custom_icons[name]
        if icon:
            return icon.icon_id
        else:
            return builtin_icons[icon_name]
    else:
        return builtin_icons[icon_name]


def get_panel_icon_id(opened):
    if opened:
        return get_icon_id("panel_opened")
    else:
        return get_icon_id("panel_closed")