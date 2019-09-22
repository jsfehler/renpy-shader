# A simple, custom pixel shader. Feel free to edit this and see what changes.
# Also check out the shaders bundled with this library if you want to.
define PS_COLOR_WAVE = """
    VARYING vec2 varUv; //Texture coordinates

    UNIFORM sampler2D tex0; //Texture bound to slot 0
    UNIFORM float shownTime; //RenPy provided displayable time

    void main()
    {
        vec4 color = texture2D(tex0, varUv);
        float red = color.r * ((sin(shownTime) + 1.0) / 2.0);
        float green = color.g * ((sin(shownTime + 2.0) + 1.0) / 2.0);
        float blue = color.b * ((sin(shownTime + 4.0) + 1.0) / 2.0);
        gl_FragColor = vec4(red, green, blue, color.a);
    }
"""
