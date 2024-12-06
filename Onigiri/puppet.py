import bpy
import traceback
import mathutils


if 1 == 1:

    props = {}

    props["help"] = "FIXME"

    props["master"] = None


def get_master(armature, report=False):
    OBJ = armature
    if isinstance(armature, str):
        OBJ = bpy.data.objects[armature]

    masRig = OBJ.get("oni_puppet_master")
    minions = OBJ.get("oni_puppet_minions")
    if masRig is None and minions is None:
        if report:
            print("puppet::get_master reports : not in the set")
        return False
    if masRig is not None and minions is not None:
        if report:
            print(
                "puppet::get_master reports : provided object contains both data sets for master and puppet, this is invalid."
            )
        return False
    if masRig is not None:
        return masRig

    if minions is not None:
        return OBJ

    if report:
        print("puppet::get_master reports : fall-through, this shouldn't happen.")

    return False
