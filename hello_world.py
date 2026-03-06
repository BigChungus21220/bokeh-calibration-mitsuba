import mitsuba as mi

mi.set_variant('scalar_rgb')

img = mi.render(mi.load_dict(mi.cornell_box()))
ldr = mi.Bitmap(img).convert(mi.Bitmap.PixelFormat.RGB, mi.Struct.Type.UInt8)

ldr.write('cbox.png')