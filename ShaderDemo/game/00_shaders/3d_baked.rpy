define PS_3D_BAKED = """

VARYING vec2 varUv;

UNIFORM sampler2D tex0;

void main()
{
    gl_FragColor = texture2D(tex0, varUv);
}
"""
