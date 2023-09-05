import bpy

# Create or retrieve the Holdout material from the shader library
holdout_material = bpy.data.materials.get("Holdout_Material")
if not holdout_material:
    holdout_material = bpy.data.materials.new(name="Holdout_Material")

# Ensure the material uses nodes
holdout_material.use_nodes = True

# Clear existing nodes
nodes = holdout_material.node_tree.nodes
nodes.clear()

# Create Holdout shader node
holdout_node = nodes.new(type='ShaderNodeHoldout')
holdout_node.location = (0, 0)

# Create Material Output node
output_node = nodes.new(type='ShaderNodeOutputMaterial')
output_node.location = (400, 0)

# Link nodes
holdout_material.node_tree.links.new(holdout_node.outputs['Holdout'], output_node.inputs['Surface'])

# Assign the Holdout material to selected mesh objects without removing other material slots
selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
for obj in selected_objects:
    # Create a new material slot for the Holdout material and assign it
    obj.data.materials.append(holdout_material)
    
    # Assign the Holdout material to all faces of the object
    for polygon in obj.data.polygons:
        polygon.material_index = len(obj.data.materials) - 1  # Assign the last material slot

print(f"Holdout material added to {len(selected_objects)} selected mesh objects as a new material slot.")
