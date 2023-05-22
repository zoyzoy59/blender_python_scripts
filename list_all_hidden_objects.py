import bpy

def list_all_hidden_objects():
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # List to store the names of hidden objects
    hidden_objects = []

    # Iterate through all objects in the scene
    for obj in bpy.context.scene.objects:
        # Check if the object is hidden
        if obj.hide_get():
            obj.select_set(True)
            collection_name = obj.users_collection[0].name if obj.users_collection else "No collection"
            hidden_objects.append(f'"{obj.name}", "{collection_name}"')

    # Print the formatted list of hidden objects
    if hidden_objects:
        print("Hidden objects:")
        for obj_info in hidden_objects:
            print(obj_info)
    else:
        print("No hidden objects found.")

# Run the function
list_all_hidden_objects()
