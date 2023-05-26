import bpy

def create_lights_collection():
    lights_collection = bpy.data.collections.get("Lights")
    if lights_collection is None:
        lights_collection = bpy.data.collections.new("Lights")
        bpy.context.scene.collection.children.link(lights_collection)
    return lights_collection

def move_lights_to_collection(lights_collection):
    for obj in bpy.data.objects:
        if obj.type == 'LIGHT':
            original_collection = obj.users_collection[0] if obj.users_collection else None
            if original_collection != lights_collection:
                # Preserve visibility state
                is_hidden = obj.hide_get()
                
                lights_collection.objects.link(obj)
                if original_collection:
                    original_collection.objects.unlink(obj)
                
                # Restore visibility state
                obj.hide_set(is_hidden)

def main():
    lights_collection = create_lights_collection()
    move_lights_to_collection(lights_collection)
    bpy.context.view_layer.update()

    # Refresh the Outliner
    for area in bpy.context.screen.areas:
        if area.type == 'OUTLINER':
            area.tag_redraw()

if __name__ == "__main__":
    main()
