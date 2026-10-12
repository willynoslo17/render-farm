# Builds a simple default scene (no .blend needed): rotating cube, plane, light, camera.
import bpy, math
bpy.ops.wm.read_factory_settings(use_empty=True)
s = bpy.context.scene
s.frame_start, s.frame_end = 1, 120
bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.object
mat = bpy.data.materials.new("Accent"); mat.use_nodes = True
mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.1, 0.4, 0.9, 1)
cube.data.materials.append(mat)
cube.rotation_euler = (0, 0, 0); cube.keyframe_insert("rotation_euler", frame=1)
cube.rotation_euler = (0, 0, math.radians(360)); cube.keyframe_insert("rotation_euler", frame=120)
for fc in cube.animation_data.action.fcurves:
    for kp in fc.keyframe_points: kp.interpolation = 'LINEAR'
bpy.ops.object.light_add(type='SUN', location=(4, -4, 8)); bpy.context.object.data.energy = 4
bpy.ops.object.camera_add(location=(0, -9, 5), rotation=(math.radians(62), 0, 0))
s.camera = bpy.context.object
w = bpy.data.worlds.new("World"); s.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.08, 1)
