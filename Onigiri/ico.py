import bpy
import os
from . import mod_settings
from .mod_settings import *

use_prop_icons = False
use_oper_icons = False

## https://docs.blender.org/api/current/bpy_types_enum_items/icon_items.html
## https://iamvector.com/all-icons


import bpy.utils.previews

# Globals for custom icon previews
custom_icons = None

def is_light_theme():
    prefs = bpy.context.preferences
    #theme = prefs.themes['Default'] if 'Default' in prefs.themes else prefs.themes[0]
    #color = theme.user_interface.wcol_tooltip.inner
    #r, g, b, a = color

    theme = bpy.context.preferences.themes[0]
    ui = theme.user_interface.wcol_regular
    color = ui.inner
    r, g, b, a = color
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    return brightness > 0.5

script_dir = os.path.dirname(os.path.abspath(__file__))

custom_icons = None
builtin_icons = None
map_icons = None
modern_icons = []

used_icons = None
loaded_icons = {}

def load_icons():

    global custom_icons
    global map_icons
    global builtin_icons
    global modern_icons

    global used_icons
    global loaded_icons

    icons_dir = script_dir + oni_settings["paths"]["icons"]
    if is_light_theme():
        theme_icons_dir = os.path.join(icons_dir, 'light')
    else:
        theme_icons_dir = os.path.join(icons_dir, 'dark')

    def load(name, image_name):
        if (image_name == ""):
            custom_icons.load(name, "", "IMAGE")
            return

        if image_name.endswith(".svg"):
            filename = os.path.join(theme_icons_dir, image_name)
        else:
            filename = os.path.join(icons_dir, image_name)

        if os.path.exists(filename):
            if name not in used_icons or name in map_icons:
                if image_name.endswith(".png"):
                    print("Unused icon loaded: " + image_name)
                else:
                    modern_icons.append(name)

            custom_icons.load(name, filename, "IMAGE")
            loaded_icons[image_name] = name
        else:
            print("Failed to load: " + name)

    custom_icons = bpy.utils.previews.new()

    used_icons = {
        "blank",
        "click",
        "panel_opened",
        "panel_closed",
        "load",
        "delete",
        "copy",
        "convert",
        "volume_bones",
        "rotate",
        "project",
        "second-life",
        "alert",
        "save",
        "disable_map_pose",
        "code_disabled",
        "reset",
        "map",
        "loop",
        "line_thin_white",
        "walking_black",
        "walking_blue",
        "walking_red",
        "overwrite",
        "prefix_remove",
        "x_red",
        "magic",
        "x_black",
        "nuke",
        "match",
        "controller",
        "bone_black",
        "play_red",
        "play_green",
        "action",
        "bone_red",
        "bone_blue",
        "run",
        "follow",
        "view_anchor_bones",
        "view_reskin_bones",
        "view_output_bones",
        "bone_green",
        "clean",
        "to_actor",
        "bone_mixed",
        "bone_yellow_blue",
        "target",
        "director",
        "sync",
        "bone_black_red",
        "map_bones",
        "map_bones_reverse",
        "lead",
        "safe",
        "integrity_check",
        "next_red_blue",
        "bone_bent",
        "select_ends",
        "deselect_non_ends",
        "select_volumes",
        "select_attach",
        "link",
        "bones",
        "bones_blue",
        "edit",
        "script",
        "save_default",
        "reset_all",
        "preset",
        "symmetric",
        "scale",
        "anchor",
        "full",
        "joint",
        "location",
        "rotation",
        "dot_green",
        "dot_yellow",
        "dot_red",
        "dot_black",
        #"data",
        "export",
        "old",
        "dot_white",
        "split",
        "sliders",
        "default",
        "rig_to_mesh",
        "bones_to_mesh",
        "center",
        "cut",
        "mesh",
        "smooth",
        "selection",
        "assume_pose",
        "apply_pose",
        "proxy",
        "transfer",
        "tools",
        "calc",
        "add",
        "subtract",
        "paint",
        "paint_disabled",
        #"arrow_right_green",
        "fitmesh",
        "no_bone",
        "star_green",
        "axis_y",
        "axis",
        "kit",
        "x_mixed",
        "fix_pose",
        "detach",
        "retarget",
        "shape_shifter",
        "glue",
        "all_bones",
        "stabilize",
        "animation_start",
        "export_mesh",
        "experiment",
        "bake",
        "export_animation",
        "arrow_up",
        "store",
        "thumb_up",
        "thumb_down",
        "x",
        "prefix",
        "constraint",
        "locked_black",
        "unlocked_black",
        "build",
        "sample",
        "align_bones",
        "freeze",
        "apply",
        "all_types",
        "y",
        "z",
        "time",
        "code",
        "merge",
        "hourglass",
        "linear",
        "deviation",
        "key_blue",
        "key_red",
        "rotation_blue",
        "location_blue",
        "rotation_red",
        "location_red",
        "pen",
        "bone",
        #"hand_love",
        "undeform",
        "scale_animation",
        "dot_blue",
        #"arrow_left_green",
        "remove_keys",
        "cancel",
        "insert",
        "isolate",
        "progress",
        "record",
        "blank",
        "paste",
        #"flag_none",
        #"flag_all",
        #"avastar_to_oni",
        #"save_dark",
        "fill",
        "empty",
        "camera_on",
        "key_black",
        "range",
        "hammer",
        "fix",
        "checked",
        "unchecked",
        "animation",
        "eye",
        "shape",
        "tail_to_head",
        "bone_fixed",
        "magnify",
        "restore",
        "skeleton",
        "roll",
        "check_green",
        "broken_link",
        "remove_constraints",
        "axis_side",
        "transform",
        "control",
        "angle",
        "lock_black",
        "info",
        "ik",
        "inverse_motion",
        "dynamic",
        "range_enabled",
        "object",
        "more",
        "x_green",
        "puppet",
        "thaw",
        "back_face_enabled",
        "back_face_disabled",
        "master",
        "loop_enabled",
        "object_red",
        "peak_white",
        "peak_yellow",
        "peak_red",
        "peak_black",
        "shape_shifter_navy",
        "unlock",
        "lock",
        "unknown",
        "camera",
        "scale_enabled",
        "rotation_enabled",
        "location_enabled",
        "running_guy_enabled",
        "star_black",
        "flag",
        "flag_red",
        "ease",
        "ease_enabled",
        "reset_warning"
    }

    map_icons = {
        "checked": "CHECKBOX_HLT",
        "unchecked": "CHECKBOX_DEHLT",
        "mesh": "MONKEY",
        "menu": "COLLAPSEMENU",
        "panel_opened": "DISCLOSURE_TRI_DOWN",
        "panel_closed": "DISCLOSURE_TRI_RIGHT",
        "duplicate": "DUPLICATE",
        "copy": "COPYDOWN",
        "star_green": "ARMATURE_DATA",
        "axis_y" : "AXIS_FRONT",
        "axis": "EMPTY_AXIS",
        "tools": "TOOL_SETTINGS",
        "star": "SOLO_ON",
        "kit": "OUTLINER_OB_ARMATURE",
        "rotate": "ORIENTATION_GIMBAL",
        "clean": "BRUSH_DATA",
        "restore": "LOOP_BACK",
        "time": "PREVIEW_RANGE", #SORTTIME
        "range": "ACTION_TWEAK",
        "build": "MOD_BUILD",
        "refresh": "FILE_REFRESH",
        #"reset": "DECORATE_OVERRIDE",
        "reset_all": "CON_ROTLIKE",
        "target": "CON_OBJECTSOLVER", #PIVOT_BOUNDBOX or OBJECT_DATAMODE
        "reset": "LOOP_BACK",
        "folder": "FILE_FOLDER",
        "x_red": "CANCEL",
        "cancel": "CANCEL",
        "export": "EXPORT",
        "load": "IMPORT",
        "save": "EXPORT",
        "store": "EXPORT",
        "first": "TRIA_LEFT_BAR",
        "last": "TRIA_RIGHT_BAR",
        "bone": "BONE_DATA",
        "bones": "GROUP_BONE",
        "delete": "TRASH",
        "edit": "GREASEPENCIL",
        "overwrite": "MOD_LINEART",
        "apply": "NLA_PUSHDOWN", #SHADERFX
        "done": "CHECKMARK",
        "cube" :"CUBE",
        "constraint": "CONSTRAINT",
        "invert": "MOD_MASK",
        "tag": "BOOKMARKS",
        "lock": "DECORATE_LOCKED",
        "unlock": "DECORATE_UNLOCKED",
        "code": "CONSOLE",
        "camera": "OUTLINER_DATA_CAMERA",
        "action": "SEQUENCE",
        "join": "RESTRICT_INSTANCED_OFF",
        "reverse": "UV_SYNC_SELECT",
        "location": "TRACKER",
        "rotation": "ORIENTATION_GIMBAL", #FORCE_MAGNETIC
        "scale": "AREA_SWAP", #FULLSCREEN_EXIT
        "selection": "SELECT_SET",
        "keys": "KEYINGSET",
        "dot": "RADIOBUT_ON",
        "dot_off": "RADIOBUT_OFF",
        "point": "DOT",
        "x": "EVENT_X",
        "y": "EVENT_Y",
        "z": "EVENT_Z",
        "plus": "PLUS",
        "add": "PLUS",
        "prefix":"EVENT_P", #SYNTAX_OFF
        "fix": "MODIFIER",
        "axis_side": "AXIS_SIDE",
        #"data": "ASSET_MANAGER",
        "choice_on": "CHECKBOX_HLT",
        "choice_off": "CHECKBOX_DEHLT",
        "loop": "DECORATE_OVERRIDE",
        "pin": "PINNED",
        "alert": "ERROR",
        "error": "ERROR",
        "info": "INFO",
        "pin_off": "UNPINNED",
        "old": "SCREEN_BACK",
        "image": "IMAGE_DATA",
        "map": "VIEW_ORTHO",
        "visibility": "VIS_SEL_11",
        "eye": "HIDE_OFF",
        "pen": "GREASEPENCIL",
        "mirror": "MOD_MIRROR",
        "symmetric": "MOD_MIRROR",
        "convert": "CON_FOLLOWPATH",
        "move": "TRACKING_FORWARDS_SINGLE",
        "preset": "PRESET",
        "save_default": "FILE_CACHE",
        "save_preset": "PRESET_NEW",
        "script": "SCRIPT",
        "nuke": "TRASH",
        "split": "AREA_SWAP",
        "magnify": "VIEWZOOM",
        "settings": "SETTINGS",
        "configure": "PREFERENCES",
        "smooth": "MOD_SMOOTH",
        "link": "LINK_BLEND",
        "broken_link": "UNLINKED",
        "detach": "UNLINKED",
        "attach": "APPEND_BLEND",
        "skeleton": "ARMATURE_DATA",
        "bake": "TRIA_DOWN_BAR",
        "sync": "UV_SYNC_SELECT",
        "isolate": "SPLIT_VERTICAL",
        "transfer": "MOD_DATA_TRANSFER",
        "mod_time": "MOD_TIME",
        "deform": "MOD_SIMPLEDEFORM",
        "shape": "SHAPEKEY_DATA",
        "match": "CON_SIZELIKE",
        "angle": "FACE_CORNER",
        "ik": "CON_SPLINEIK",
        "object": "CUBE",
        "more": "COLLAPSEMENU",
        "freeze": "FREEZE",
        "paste": "PASTEDOWN",
        "ease": "FORCE_CURVE",
        "default": "PRESET_NEW",
        "camera_on": "OUTLINER_OB_CAMERA",
        "paint": "BRUSHES_ALL",
        "hourglass": "PREVIEW_RANGE",
        "sliders": "OPTIONS",
        "record": "RECORD_ON",
        "sample": "GEOMETRY_NODES",
        "animation": "RENDER_ANIMATION",
        "arrow_up": "INDIRECT_ONLY_ON",
        "center": "ANCHOR_CENTER",
        "calc": "DRIVER_TRANSFORM",
        "hand": "HAND", #VIEW_PAN
        "align_bones": "NLA_PUSHDOWN",
        "magic": "SHADERFX",
        "puppet": "MESH_MONKEY",
        "insert": "NODE_INSERT_ON",
        "progress": "SORTSIZE",
        "reference": "TRACKING_REFINE_FORWARDS",
        "subtract": "SELECT_SUBTRACT",
        "transform": "MOD_SIMPLEDEFORM",
        "safe": "FAKE_USER_ON",
        "bone_fixed": "PINNED",
        "stabilize": "OUTLINER_OB_MESH", #RIGID_BODY_CONSTRAINT
        "bone_bent": "MOD_SIMPLEDEFORM",
        "check_all": "ZOOM_ALL", #BORDERMOVE
        "run": "PLAY",
        "weight": "MOD_VERTEX_WEIGHT",
        "remove_keys": "KEY_DEHLT",
        "merge": "AREA_JOIN_LEFT",
        "unknown": "QUESTION"
    }

    load("blank", "")

    load("bone", "bone.svg")
    load("bone_red", "bone_red.svg")
    load("bone_blue", "bone_blue.svg")
    load("bone_black", "bone_black.svg")
    load("bone_green", "bone_green.svg")

    load("dot_red", "dot_red.svg")
    load("dot_blue", "dot_blue.svg")
    load("dot_white", "dot_white.svg")
    load("dot_black", "dot_black.svg")
    load("dot_green", "dot_green.svg")
    load("dot_yellow", "dot_yellow.svg")

    load("click", "click.svg")
    load("cut", "cut.svg")
    load("loop", "loop.svg")
    load("anchor", "anchor.svg")
    load("roll", "roll.svg")
    load("second-life", "second-life.svg")
    load("hammer", "hammer.svg")
    load("joint", "joint.svg")
    load("flag", "flag.svg")
    load("flag_red", "flag_red.svg")

    #load("skeleton", "skeleton.svg")

    ## https://www.svgrepo.com/svg/321379/skeleton-inside


    #load("arrow_top_right", "arrow_top_right.png")
    #load("arrow_bottom_right", "arrow_bottom_right.png")
    #load("arrow_up", "arrow_up.png")
    #load("arrow_right_green", "arrow_right_green.png")
    #load("arrow_left_green", "arrow_left_green.png")
    #load("configure", "configure.png")
    #load("settings_general", "settings_general.png")
    #load("settings_advanced", "settings_advanced.png")
    #load("bone_source", "bone_source.png")
    #load("bone_target", "bone_target.png")
    #load("walking_green", "walking_green.png")
    #load("walking_white", "walking_white.png")
    load("walking_black", "walking_black.png")
    load("walking_blue", "walking_blue.png")
    load("walking_red", "walking_red.png")
    load("follow", "follow.png")
    load("lead", "lead.png")

    load("map_bones", "map_bones.png")
    load("map_bones_reverse", "map_bones_reverse.png")
    #load("map_to_mbones", "map_to_mbones.png")
    #load("map_to_template", "map_to_template.png")
    #load("load_template", "load_template.png")
    #load("save", "save.png")
    #load("save_dark", "save_dark.png")
    #load("load", "load.png")
    #load("reset", "reset.png")
    load("reset_warning", "reset_warning.png")
    load("fix_pose", "fix_pose.png")
    #load("magnify", "magnify.png")
    #load("restore_bone", "restore_bone.png")

    #load("bone_fixed", "bone_fixed.png")
    #load("bones", "bones.png")
    load("bones_blue", "bones_blue.png")
    #load("bone_bent", "bone_bent.png")
    #load("bone_yellow", "bone_yellow.png")
    load("bone_mixed", "bone_mixed.png")
    load("bone_black_red", "bone_black_red.png")
    load("bone_yellow_blue", "bone_yellow_blue.png")

    load("view_anchor_bones", "view_anchor_bones.png")
    load("view_reskin_bones", "view_reskin_bones.png")
    load("view_output_bones", "view_output_bones.png")

    load("tail_to_head", "tail_to_head.png")
    #load("map", "map.png")
    #load("create_rig", "create_rig.png")
    #load("create_neutral_rig", "create_neutral_rig.png")
    #load("create_reference_rig", "create_reference_rig.png")
    load("export_animation", "export_animation.png")
    load("running_guy", "running_guy.png")
    #load("running_guy_red", "running_guy_red.png")
    load("running_guy_enabled", "running_guy_enabled.png"),
    load("rig_to_mesh", "rig_to_mesh.png")
    load("bones_to_mesh", "bones_to_mesh.png")
    #load("remove_keys", "remove_keys.png")
    load("export_mesh", "export_mesh.png")
    #load("unlocked", "unlocked.png")
    #load("lock_red", "lock_red.png")
    #load("lock_green", "lock_green.png")
    load("lock_black", "lock_black.png")
    load("locked_black", "locked_black.png")
    load("unlocked_black", "unlocked_black.png")
    #load("create_reference_pose", "create_reference_pose.png")
    load("scale_animation", "scale_animation.png")
    load("remove_constraints", "remove_constraints.png")
    load("control", "control.png")
    #load("animation", "animation.png")
    #load("character_converter", "character_converter.png")
    #load("connect_links", "connect_links.png")
    #load("rename_to_targets", "rename_to_targets.png")
    #load("remove_unused_bones","remove_unused_bones.png")
    load("no_bone", "no_bone.png")
    #load("add_missing_groups", "add_missing_groups.png")
    load("apply_pose", "apply_pose.png")
    #load("custom_mapping", "custom_mapping.png")

    #load("x", "x.png")
    #load("x_red", "x_red.png")
    #load("x_blue", "x_blue.png")
    load("x_green", "x_green.png")
    load("x_black", "x_black.png")
    #load("x_white", "x_white.png")
    load("x_mixed", "x_mixed.png")
    #load("x_yellow", "x_yellow.png")
    #load("x_black_white", "x_black_white.png")
    #load("x_white_black", "x_white_black.png")

    #load("info", "info.png")

    load("key_red", "key_red.png")
    load("key_blue", "key_blue.png")
    #load("key_white", "key_white.png")
    load("key_black", "key_black.png")
    #load("key_green", "key_green.png")
    #load("key_yellow", "key_yellow.png")

    load("thumb_up", "thumb_up.png")
    load("thumb_down", "thumb_down.png")
    #load("thumb_up_green", "thumb_up_green.png")
    #load("thumb_down_red", "thumb_down_red.png")

    load("integrity_check", "integrity_check.png")
    #load("pose_library", "pose_library.png")
    #load("add", "add.png")
    #load("subtract", "subtract.png")
    #load("edit", "edit.png")
    #load("edit_red", "edit_red.png")
    #load("edit_rgb", "edit_rgb.png")
    #load("edit_grey", "edit_grey.png")
    #load("edit_white", "edit_white.png")
    #load("selection", "selection.png")
    #load("merge", "merge.png")
    #load("broken_link", "broken_link.png")

    load("loop_enabled", "loop_enabled.png")
    #load("range", "range.png")
    load("range_enabled", "range_enabled.png")

    #load("angle", "angle.png")
    #load("bake", "bake.png")
    #load("store", "store.png")
    #load("record", "record.png")
    #load("tools", "tools.png")
    #load("alert", "alert.png")
    #load("head", "head.png")
    #load("stabilize", "stabilize.png")
    #load("prefix", "prefix.png")
    load("prefix_remove", "prefix_remove.png")
    #load("reshape", "reshape.png")
    load("assume_pose", "assume_pose.png")
    load("volume_bones", "volume_bones.png")
    #load("spine_bones", "spine_bones.png")
    load("all_bones", "all_bones.png")
    load("all_types", "all_types.png")
    #load("selected_bones", "selected_bones.png")
    #load("smooth", "smooth.png")
    load("undeform", "undeform.png")
    #load("check_white", "check_white.png")
    #load("check_black", "check_black.png")
    #load("check_red", "check_red.png")
    #load("check_blue", "check_blue.png")
    load("check_green", "check_green.png")
    #load("check_yellow", "check_yellow.png")
    #load("sl", "sl.png")
    #load("skin", "skin.png")
    #load("menu_closed", "menu_closed.png")

    #load("menu_opened", "menu_opened.png")
    #load("orientation", "orientation.png")
    #load("off", "off.png")
    #load("on", "on.png")
    #load("choice_off", "choice_off.png")
    #load("choice_on", "choice_on.png")
    #load("choice_red", "choice_red.png")
    #load("choice_green", "choice_green.png")
    #load("sync", "sync.png")
    #load("inherit", "inherit.png")
    load("linear", "linear.png")
    load("retarget", "retarget.png")
    load("proxy", "proxy.png")
    #load("detach", "detach.png")
    #load("target", "target.png")
    load("disable_map_pose", "disable_map_pose.png")
    #load("magic", "magic.png")
    #load("hide_bones", "hide_bones.png")
    #load("hide_mapped_bones", "hide_mapped_bones.png")
    #load("hide_anchor_branch_bones", "hide_anchor_branch_bones.png")
    #load("isolation_mode", "isolation_mode.png")
    #load("isolate", "isolate.png")
    #load("reskin_bone", "reskin_bone.png")
    load("glue", "glue.png")
    load("experiment", "experiment.png")
    #load("curves", "curves.png")
    #load("ease", "ease.png")
    load("ease_enabled", "ease_enabled.png")

    #load("eye", "eye.png")
    #load("calc", "calc.png")
    #load("center", "center.png")
    #load("sliders", "sliders.png")
    #load("line_white", "line_white.png")
    #load("line_black", "line_black.png")
    #load("line_red", "line_red.png")
    #load("line_yellow", "line_yellow.png")
    #load("line_blue", "line_blue.png")
    #load("line_green", "line_green.png")
    load("line_thin_white", "line_thin_white.png")
    #load("line_thin_black", "line_thin_black.png")
    #load("star_red", "star_red.png")
    load("star_black", "star_black.png")
    #load("star_green", "star_green.png")
    #load("star_yellow", "star_yellow.png")
    #load("default", "default.png")
    #load("neutral", "neutral.png")
    load("shape_shifter", "shape_shifter.png")
    #load("shape_shifter_green", "shape_shifter_green.png")
    #load("shape_shifter_red", "shape_shifter_red.png")
    load("shape_shifter_navy", "shape_shifter_navy.png")
    #load("shape_shifter_white","shape_shifter_white.png")
    #load("peak", "peak_black.png")
    load("peak_black", "peak_black.png")
    #load("peak_blue", "peak_blue.png")
    #load("peak_green", "peak_green.png")
    #load("peak_orange", "peak_orange.png")
    load("peak_red", "peak_red.png")
    load("peak_white", "peak_white.png")
    load("peak_yellow", "peak_yellow.png")
    #oad("avastar_to_oni", "avastar_to_oni.png")
    #load("safe", "safe.png")
    #load("match", "match.png")
    load("fitmesh", "fitmesh.png")
    load("animation_start", "animation_start.png")
    #load("split", "split.png")
    #load("mesh", "mesh.png")
    #load("volume", "volume.png")
    #load("rotate", "rotate.png")
    #load("location", "location.png")
    load("location_red", "location_red.png")
    load("location_blue", "location_blue.png")
    #load("location_white", "location_white.png")
    load("location_enabled", "location_enabled.png")
    #load("rotation", "rotation.png")
    load("rotation_red", "rotation_red.png")
    load("rotation_blue", "rotation_blue.png")
    #load("rotation_white", "rotation_white.png")
    load("rotation_enabled", "rotation_enabled.png")
    #load("scale", "scale.png")
    load("scale_enabled", "scale_enabled.png")
    #load("scale_special", "scale_special.png")
    #load("transform", "transform.png")
    #load("transform_enabled", "transform_enabled.png")
    #load("transfer", "transfer.png")
    #load("properties_black", "properties_black.png")
    #load("properties_white", "properties_white.png")
    #load("freeze", "freeze.png")FREEZE
    load("thaw", "thaw.png")
    #load("clean", "clean.png")
    load("fill", "fill.png")
    load("empty", "empty.png")
    #load("copy", "copy.png")
    #load("paste", "paste.png")
    #load("insert", "insert.png")
    #load("play", "play.png")
    load("play_red", "play_red.png")
    #load("play_blue", "play_blue.png")
    load("play_green", "play_green.png")
    #load("play_white", "play_white.png")
    #load("play_yellow", "play_yellow.png")
    #load("play_orange", "play_orange.png")
    #load("progress", "progress.png")
    #load("flag_all", "flag_all.png")
    #load("flag_none", "flag_none.png")
    load("deviation", "deviation.png")
    #load("tolerance", "tolerance.png")
    #load("sample", "sample.png")
    #load("hand_love", "hand_love.png")
    load("full", "full.png")
    #load("time", "time.png")
    #load("hourglass", "hourglass.png")

    #load("symmetric", "symmetric.png")
    #load("paint_enabled", "paint_enabled.png") //paint
    load("paint_disabled", "paint_disabled.png")
    #load("back_face", "back_face.png")
    load("back_face_enabled", "back_face_enabled.png")
    load("back_face_disabled", "back_face_disabled.png")

    #load("link", "link.png")
    #load("opensim", "opensim.png")
    load("controller", "controller.png")
    #load("start", "start.png")
    #load("action", "action.png")
    #load("camera", "camera.png")
    #load("camera_on", "camera_on.png")
    load("director", "director.png")
    load("to_actor", "to_actor.png")
    #load("director_blue", "director_blue.png")
    #load("director_green", "director_green.png")
    #load("script", "script.png")
    #load("code", "code.png")
    load("code_disabled", "code_disabled.png")
    #load("nuke", "nuke.png")

    #load("next", "next.png")
    load("next_red_blue", "next_red_blue.png")

    load("select_ends", "select_ends.png")
    load("select_volumes", "select_volumes.png")
    load("select_attach", "select_attach.png")
    load("deselect_non_ends", "deselect_non_ends.png")

    #load("ik", "ik.png")
    #load("object", "object.png")
    #load("object_white", "object_white.png")
    load("object_red", "object_red.png")
    load("dynamic", "dynamic.png")

    #load("more", "more.png")
    #load("global", "global.png")
    #load("pull", "pull.png")
    load("master", "master.png")
    #load("puppet", "puppet.png")
    #load("align_bones", "align_bones.png")
    load("project", "project.png")
    #load("pin", "pin.png")
    load("inverse_motion", "inverse_motion.png")
    #load("nametag", "nametag.png")
    #load("axis_x", "axis_x.png")
    #load("axis_y", "axis_y.png")
    #load("axis_z", "axis_z.png")
    #load("unknown", "unknown.png")
    #load("ragdoll", "ragdoll.png")

    for root, dirs, files in os.walk(icons_dir):
        for file in files:
            if file.endswith(".png"):
                if not loaded_icons.get(file):
                    print("Unused file: " + file)

    for ico in used_icons:
        if not custom_icons.get(ico) and not map_icons.get(ico):
            print("Icon needed: " + ico)

    icon_items = bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.items()
    builtin_icons = {tup[1].identifier : tup[1].value for tup in icon_items}

def unload_icons():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

## https://blender.stackexchange.com/questions/224015/is-there-a-way-to-get-icon-value-for-the-uilist-using-icon-name-from-enum

def get_icon_id(name):
    global custom_icons
    global builtin_icons
    icon_name = map_icons.get(name)
    if icon_name:
        return builtin_icons[icon_name]
    else:
        icon = custom_icons.get(name)
        if icon:
            return icon.icon_id
        else:
            return builtin_icons[name]


def get_panel_icon_id(opened):
    if opened:
        return get_icon_id("panel_opened")
    else:
        return get_icon_id("panel_closed")

def get_prop_icon_id(name):
    global use_prop_icons
    if use_prop_icons:
        return get_icon_id(name)
    else:
        return 0

def get_oper_icon_id(name):
    global use_oper_icons
    global builtin_icons
    global map_icons
    global modern_icons
    if use_oper_icons:
        return get_icon_id(name)
    else:
        icon_name = map_icons.get(name)
        if icon_name or (name in modern_icons):
            return get_icon_id(name)
        else:
            return 0
