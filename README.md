# blender_python_scripts

This is a list of basic Blender Python scripts that I made using ChatGPT. 

These scripts have only been tested for Blender 3.5.

If your project is complex or has a lot of objects, your results may vary. Execute with console open, preferably.

## move_cameras_to_collection
- moves all cameras into collection called "Cameras"

## move_lights_to_collection
- moves all lights into collection called "Lights"

## create_empty_parent_for_objects.py
- creates empty for a set of selected objects; use the empty to control transformation of group

## list_all_hidden_objects.py
- prints (in system console) the object name and collection name for all hidden objects

## move_hidden_objects_to_new_collection.py
- self-explanatory

## render_viewport.py
- whatever appears in your 3d viewport, with overlays, is rendered in 1920 x 1080
- paste your desired output directory in "/path/to/output/directory/"
- (does not render cycles viewport preview)

# Scripts WIP -- danger, might mess up your scene, sorrylol

## reset_bones_and_armatures.py
sets selected rigs back to default pose and to world origin (testing)

## save_render_as_filename_frame_seq.py
saves render of active camera as blendname_frame_00x.png in specified directory (testing)

