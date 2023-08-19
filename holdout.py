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

# Assign the Holdout material to all mesh objects
for obj in bpy.context.scene.objects:
    if obj.type == "MESH":
        obj.data.materials.clear()  # Remove existing materials
        obj.data.materials.append(holdout_material)

print("Holdout materials assigned to all meshes.")
