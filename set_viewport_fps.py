import bpy

def set_viewport_playback(fps):
    bpy.context.scene.render.fps = fps
    bpy.context.scene.render.frame_map_old = bpy.context.scene.render.frame_map_new
    bpy.context.scene.render.frame_map_new = round(fps / bpy.context.scene.render.fps)

set_viewport_playback(10)  # Replace 24 with your desired fps value
