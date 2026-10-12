import bpy
s = bpy.context.scene
s.render.engine = 'CYCLES'
s.cycles.device = 'CPU'
s.cycles.samples = 8
s.cycles.use_adaptive_sampling = True
s.cycles.use_denoising = True
s.cycles.denoiser = 'OPENIMAGEDENOISE'
s.render.resolution_x, s.render.resolution_y = 540, 960
s.render.resolution_percentage = 100
s.render.use_persistent_data = True
s.render.threads_mode = 'AUTO'  # use all CPU threads
s.render.image_settings.file_format = 'PNG'
