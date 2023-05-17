import bpy

def reset_armatures():
    selected_objects = bpy.context.selected_objects

    # Reset the armature and bones
    for obj in selected_objects:
        if obj.type == 'ARMATURE':
            armature = obj.data

            # Reset the armature to its default rest position
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.transforms_clear()

            # Reset the armature's rotation and position to world origin
            obj.location = (0, 0, 0)
            obj.rotation_euler = (0, 0, 0)

            # Remove keyframes for pose bones without affecting other keyframes
            for pbone in obj.pose.bones:
                bone = pbone.bone
                bone_name = bone.name
                
                # Clear keyframes only for the bone's location and rotation channels
                for channel in ['location', 'rotation_euler']:
                    full_channel_name = f'pose.bones["{bone_name}"].{channel}'
                    obj.keyframe_delete(data_path=full_channel_name, action='KEYFRAME')

reset_armatures()
