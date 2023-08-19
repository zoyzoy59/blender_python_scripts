import bpy

# Iterate through all objects in the scene
for obj in bpy.context.scene.objects:
    if obj.type == "MESH":
        # Create a new Solidify modifier
        solidify_modifier = obj.modifiers.new(name="Solidify", type="SOLIDIFY")
        
        # Set the thickness value to 0.01 m
        solidify_modifier.thickness = 0.01
        
        # Set the offset value to 1
        solidify_modifier.offset = 1.0
        
        # Set the modifier to be visible in the viewport but not in render
        solidify_modifier.show_render = False

print("Solidify modifiers added to all mesh objects with custom thickness and offset, and render visibility disabled.")
