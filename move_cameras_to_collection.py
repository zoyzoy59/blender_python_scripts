import bpy

def create_cameras_collection():
    cameras_collection = bpy.data.collections.get("Cameras")
    if cameras_collection is None:
        cameras_collection = bpy.data.collections.new("Cameras")
        bpy.context.scene.collection.children.link(cameras_collection)
    return cameras_collection

def move_cameras_to_collection(cameras_collection):
    for obj in bpy.data.objects:
        if obj.type == 'CAMERA':
            original_collection = obj.users_collection[0] if obj.users_collection else None
            if original_collection != cameras_collection:
                cameras_collection.objects.link(obj)
                if original_collection:
                    original_collection.objects.unlink(obj)

def main():
    cameras_collection = create_cameras_collection()
    move_cameras_to_collection(cameras_collection)
    bpy.context.view_layer.update()

    # Refresh the Outliner
    for area in bpy.context.screen.areas:
        if area.type == 'OUTLINER':
            area.tag_redraw()

if __name__ == "__main__":
    main()
