import bpy
s = bpy.context.scene
s.render.engine = 'CYCLES'
s.cycles.device = 'CPU'
s.cycles.samples = 64
s.render.resolution_x, s.render.resolution_y = 1080, 1920
