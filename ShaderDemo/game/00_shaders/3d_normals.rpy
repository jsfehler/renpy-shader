define PS_3D_NORMALS = """

VARYING vec3 varNormal;
VARYING vec2 varUv;

UNIFORM sampler2D tex0;

void main()
{
    float r = (varNormal.x + 1.0) / 2.0;
    float g = (varNormal.y + 1.0) / 2.0;
    float b = (varNormal.z + 1.0) / 2.0;
    gl_FragColor = vec4(r, g, b, 1.0);
}
"""
