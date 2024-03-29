import bpy

def move_hidden_objects_to_new_collection():
    # Create a new collection
    new_collection = bpy.data.collections.new("Hidden Objects")
    bpy.context.scene.collection.children.link(new_collection)

    # List to store the names of hidden objects
    hidden_objects = []

    # Iterate through all objects in the scene
    for obj in bpy.context.scene.objects:
        # Check if the object is hidden
        if obj.hide_get():
            hidden_objects.append(obj)
    
    # Move the hidden objects to the new collection
    for obj in hidden_objects:
        # Unlink from current collection if any
        if obj.users_collection:
            current_collection = obj.users_collection[0]
            current_collection.objects.unlink(obj)
        
        # Link to the new collection
        new_collection.objects.link(obj)

# Run the function to move hidden objects to a new collection
move_hidden_objects_to_new_collection()
