import bpy
import os

from bpy import context

#----------------------------------
# PRINT BONE LOCATION ON ALL FRAMES
#----------------------------------

armatureN = "Armature.002"
boneN = "LowerArm R"

path = r"C:\Users\Alberto\Documents\Compartido\UA\Cuarto curso\RV\Animations\DirectR\DirectR.bbx"
filename = ""
enter = "\n"

for obj in bpy.data.objects:
    obj.select_set(False)
    
bpy.data.objects[armatureN].select_set(True)

scene = bpy.context.scene
armature = bpy.context.active_object
bones = armature.data.bones
pose_bones = armature.pose.bones

f2 = open(path + filename, "w")

for f in range(scene.frame_start, scene.frame_end+1):
    scene.frame_set(f)
    print("Frame " + str(f) + ": ")
    
    # This can be head, tail, center...
    # More info: https://docs.blender.org/api/current/bpy.types.PoseBone.html?highlight=bpy%20bone#bpy.types.PoseBone.bone
    bone = armature.pose.bones[boneN].tail
    
    # Since Blender 2.8 you multiply matrices with @ not with *
    bonePos = armature.matrix_world @ bone
    print(bonePos)
    f2.write(str(-bonePos[0]) + enter)
    f2.write(str(bonePos[2]) + enter)
    f2.write(str(-bonePos[1]) + enter)
    
    # bpy.ops.mesh.primitive_cube_add(size = 0.1, location=bonePos)
    # armature.pose.bones[boneN]
    
f2.close()