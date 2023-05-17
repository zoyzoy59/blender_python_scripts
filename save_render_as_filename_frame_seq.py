import bpy
import os

# Get the current .blend file name
blend_file = bpy.path.basename(bpy.context.blend_data.filepath)
blend_name = os.path.splitext(blend_file)[0]

# Specify the custom output directory
output_dir = "/path/to/output/directory/"  # Replace with your desired output directory

# Set the output path
output_path = os.path.join(output_dir, blend_name)

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Set rendering settings to use the active camera
scene = bpy.context.scene

# Get the active camera by name
active_camera_name = bpy.context.scene.camera.name
active_camera = bpy.data.objects.get(active_camera_name)

# Check if the active camera exists and is a camera type
if active_camera and active_camera.type == 'CAMERA':
    scene.camera = active_camera
else:
    print("No active camera found. Please set an active camera and run the script again.")
    exit()

# Get the current frame number
frame_num = bpy.context.scene.frame_current

# Set the output filename and numbering
file_prefix = blend_name
file_numbering = 1
filename = f"{file_prefix}_{frame_num:03d}_{file_numbering:03d}.png"
filepath = os.path.join(output_path, filename)

# Set the output format to PNG
scene.render.image_settings.file_format = 'PNG'

# Check if the file already exists, incrementing the numbering if necessary
while os.path.exists(filepath):
    file_numbering += 1
    filename = f"{file_prefix}_{frame_num:03d}_{file_numbering:03d}.png"
    filepath = os.path.join(output_path, filename)

# Render the frame using the active camera view
scene.render.filepath = filepath
bpy.ops.render.render(write_still=True)

print(f"Rendered and saved {filename} in {output_path}")
