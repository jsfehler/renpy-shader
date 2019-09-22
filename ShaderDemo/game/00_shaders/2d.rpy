define VS_2D = """

ATTRIBUTE vec4 inVertex;

VARYING vec2 varUv;

UNIFORM mat4 projection;

void main()
{
    varUv = inVertex.zw;
    gl_Position = projection * vec4(inVertex.xy, 0.0, 1.0);
}
"""
