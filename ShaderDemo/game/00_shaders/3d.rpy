define VS_3D = """

ATTRIBUTE vec4 inPosition;
ATTRIBUTE vec3 inNormal;
ATTRIBUTE vec2 inUv;

VARYING vec3 varNormal;
VARYING vec2 varUv;

UNIFORM mat4 worldMatrix;
UNIFORM mat4 viewMatrix;
UNIFORM mat4 projMatrix;

void main()
{
    varUv = inUv;
    varNormal = inNormal;
    gl_Position = projMatrix * viewMatrix * worldMatrix * inPosition;
}
"""
