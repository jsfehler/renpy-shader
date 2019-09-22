# Generic screen for showing 2d-images. In some cases it might be wise
# to create more specific screens which know the images and
# parameters they want to use instead of passing them all in every time you
# want to show the screen. Also remember the screen "tag"-attribute, it can come in handy.
screen shaderScreen(name, pixelShader, textures={}, uniforms={}, update=None, xalign=0.5, yalign=0.1):
    modal False
    add ShaderDisplayable(shader.MODE_2D, name, VS_2D, pixelShader, textures, uniforms, None, update):
        xalign xalign
        yalign yalign
