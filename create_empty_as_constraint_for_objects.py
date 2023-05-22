import bpy

def create_empty_parent_for_objects():
    selected_objects = bpy.context.selected_objects
    
    # Create an empty object
    empty = bpy.data.objects.new("Empty", None)
    bpy.context.scene.collection.objects.link(empty)
    
    # Set the empty object as the parent for selected objects
    for obj in selected_objects:
        obj.parent = empty

create_empty_parent_for_objects()
