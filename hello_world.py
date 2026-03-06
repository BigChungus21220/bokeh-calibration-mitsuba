import mitsuba as mi

mi.set_variant('scalar_rgb')

img = mi.render(mi.load_file('point_grid_scene.xml'))
ldr = mi.Bitmap(img).convert(mi.Bitmap.PixelFormat.RGB, mi.Struct.Type.UInt8, srgb_gamma=True)

ldr.write('result.png')