import bpy

def reset_armatures():
    selected_objects = bpy.context.selected_objects

    # Iterate through selected objects
    for obj in selected_objects:
        if obj.type == 'ARMATURE':
            armature = obj.data

            # Reset the armature to its default rest position
            for pose_bone in obj.pose.bones:
                pose_bone.matrix_basis.identity()

            # Reset the armature's rotation and position to world origin
            obj.location = (0, 0, 0)
            obj.rotation_euler = (0, 0, 0)

reset_armatures()
