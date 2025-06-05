import bpy
import os
from . import mod_settings
from .mod_settings import *

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
        ## icon_defs.py
        "choice_off",
        "choice_on",
        ## __init__.py
        "action",
        "add",
        "alert",
        "align_bones",
        "anchor",
        "animation",
        "animation_start",
        "apply",
        "armature",
        "arrow_up",
        "axis",
        "axis_side",
        "axis_y",
        "bake",
        "blank",
        "bone",
        "bone_bent",
        "bone_black",
        "bone_blue",
        "bone_fixed",
        "bone_green",
        "bone_red",
        "bones",
        "bones_mesh",
        "broken_link",
        "build",
        "calc",
        "camera",
        "camera_on",
        "cancel",
        "checked",
        "checkmark",
        "child",
        "clean",
        "code",
        "constraint",
        "convert",
        "copy",
        "cut",
        "default",
        "delete",
        "detach",
        "deviation",
        "director",
        "disable",
        "done",
        "dot_black",
        "dot_blue",
        "dot_green",
        "dot_red",
        "dot_white",
        "dot_yellow",
        "duplicate",
        "ease",
        "ease_enabled",
        "edit",
        "enable",
        "export",
        "eye",
        "fill",
        "fix",
        "flag",
        "flag_red",
        "folder",
        "follow",
        "freeze",
        "hammer",
        "ik",
        "info",
        "insert",
        "isolate",
        "kit",
        #"line",
        "link",
        "load",
        "location",
        "location_enabled",
        "lock",
        "locked",
        "loop",
        "loop_enabled",
        "magic",
        "magnify",
        "map",
        "master",
        "match",
        "merge",
        "mesh",
        "more",
        "move",
        "nuke",
        "object",
        "object_red",
        "old",
        "overwrite",
        "paint",
        "paint_disabled",
        "paste",
        "pen",
        "play",
        "pose",
        "prefix",
        "prefix_remove",
        "preset",
        "range",
        "range_enabled",
        "record",
        "remove",
        "reset",
        "reset_all",
        "restore",
        "reverse",
        "roll",
        "rotate",
        "rotation",
        "rotation_enabled",
        "run",
        "sample",
        "save",
        "save_default",
        "scale",
        "scale_enabled",
        "script",
        "selection",
        "shape",
        "skeleton",
        "sliders",
        "smooth",
        "split",
        "stabilize",
        "star",
        "star_off",
        "store",
        "subtract",
        "symmetric",
        "sync",
        "target",
        "thumb_down",
        "thumb_up",
        "time",
        "tools",
        "transfer",
        "transform",
        "unchecked",
        "undo",
        "unknown",
        "unlock",
        "unlocked",
        "weight",
        "x",
        "x_black",
        "x_red",
        "y",
        "z",
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
        "paste": "PASTEDOWN",
        "axis_y" : "AXIS_FRONT",
        "axis": "EMPTY_AXIS",
        "tools": "TOOL_SETTINGS",
        "star": "SOLO_ON",
        "star_off": "SOLO_OFF",
        "kit": "PACKAGE",
        "pose": "OUTLINER_OB_ARMATURE",
        "rotate": "ORIENTATION_GIMBAL",
        "clean": "BRUSH_DATA",
        "restore": "LOOP_BACK",
        "time": "PREVIEW_RANGE", #SORTTIME
        "range": "ACTION_TWEAK",
        "build": "MOD_BUILD",
        "refresh": "FILE_REFRESH",
        "reset": "CON_ROTLIMIT",
        "reset_all": "CON_ROTLIKE",
        "undo": "LOOP_BACK",
        "redo": "LOOP_FORWARDS",
        "target": "CON_OBJECTSOLVER", #PIVOT_BOUNDBOX or OBJECT_DATAMODE
        "override": "DECORATE_OVERRIDE",
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
        "remove": "TRASH", # "CLOSE",
        "close": "PANEL_CLOSE",
        "edit": "GREASEPENCIL",
        "overwrite": "MOD_LINEART",
        "apply": "NLA_PUSHDOWN", #SHADERFX
        "done": "CHECKMARK",
        "checkmark": "CHECKMARK",
        "cube" :"CUBE",
        "constraint": "CONSTRAINT",
        "invert": "MOD_MASK",
        "tag": "BOOKMARKS",
        "lock": "DECORATE_LOCKED",
        "unlock": "DECORATE_UNLOCKED",
        "locked": "DECORATE_LOCKED",
        "unlocked": "DECORATE_UNLOCKED",
        "console": "CONSOLE",
        "camera": "OUTLINER_DATA_CAMERA",
        "camera_on": "OUTLINER_OB_CAMERA",
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
        "x_black": "X",
        "plus": "PLUS",
        "add": "PLUS",
        "prefix":"EVENT_P", #SYNTAX_OFF
        "fix": "MODIFIER",
        "axis_side": "AXIS_SIDE",
        #"data": "ASSET_MANAGER",
        "choice_on": "CHECKBOX_HLT",
        "choice_off": "CHECKBOX_DEHLT",
        "deviation": "MOD_SMOOTH",
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
        "script": "WORDWRAP_ON", #"SCRIPT",
        "code": "SCRIPT",
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
        "armature": "ARMATURE_DATA",
        "director": "CON_ARMATURE",
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
        #"object": "CUBE",
        "more": "COLLAPSEMENU",
        "freeze": "FREEZE",
        "ease": "FORCE_CURVE",
        "default": "PRESET_NEW",
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
        "run": "ARMATURE_DATA",
        "play": "PLAY",
        "weight": "MOD_VERTEX_WEIGHT",
        "remove_keys": "KEY_DEHLT",
        "merge": "AREA_JOIN_LEFT",
        "child": "CON_CHILDOF",
        "unknown": "QUESTION",
        "disable": "MODIFIER_OFF",
        "enable": "MODIFIER_ON",
        "constraint_bone":"CONSTRAINT_BONE",
        #"pose": "POSE_HLT",
        "proxy": "MOD_PARTICLE_INSTANCE",
        "animation_start": "TRACKING_FORWARDS_SINGLE",
        "linear": "NORMALIZE_FCURVES",
        #"line":"IPO_LINEAR",
        "full": "CENTER_ONLY",
        "follow": "CURVE_PATH",
        "retarget": "CON_OBJECTSOLVER"
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
    load("glue", "glue.svg")
    load("master", "master.svg")
    load("fill", "fill.svg")
    load("prefix_remove", "prefix_remove.svg")
    ## https://www.svgrepo.com/svg/409322/thumb-down
    load("thumb_down", "thumb_down.svg")
    load("thumb_up", "thumb_up.svg")

    load("object", "object.svg")
    load("object_red", "object_red.svg")
    load("bones_mesh", "bones_mesh.svg")

    ## https://www.svgrepo.com/svg/321379/skeleton-inside
    #load("skeleton", "skeleton.svg")

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

def get_enabled_icon_id(icon, enabled):
    if enabled:
        return get_icon_id(icon)
    else:
        return get_icon_id(icon) #i dont know how to disable it