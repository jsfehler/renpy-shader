define VS_SKINNED = """

ATTRIBUTE vec2 inVertex;
ATTRIBUTE vec2 inUv;
ATTRIBUTE vec4 inBoneWeights;
ATTRIBUTE vec4 inBoneIndices;

VARYING vec2 varUv;
VARYING float varAlpha;

UNIFORM mat4 projection;
UNIFORM mat4 boneMatrices[MAX_BONES];
UNIFORM vec2 screenSize;
UNIFORM float shownTime;

vec2 toScreen(vec2 point)
{
    return vec2(point.x / (screenSize.x / 2.0) - 1.0, point.y / (screenSize.y / 2.0) - 1.0);
}

void main()
{
    varUv = inUv;

    vec2 pos = vec2(0.0, 0.0);
    float transparency = 0.0;
    vec4 boneWeights = inBoneWeights;
    ivec4 boneIndex = ivec4(inBoneIndices);

    for (int i = 0; i < 4; i++) {
        mat4 boneMatrix = boneMatrices[boneIndex.x];
        pos += (boneMatrix * vec4(inVertex, 0.0, 1.0) * boneWeights.x).xy;

        //Apply damping
        vec2 boneDelta = vec2(boneMatrix[0][3], boneMatrix[1][3]);
        pos += (boneDelta * boneWeights.x) * boneMatrix[2][3];

        //Apply transparency
        transparency += boneMatrix[3][3] * boneWeights.x;

        boneWeights = boneWeights.yzwx;
        boneIndex = boneIndex.yzwx;
    }
    varAlpha = max(1.0 - transparency, 0.0);

    gl_Position = projection * vec4(toScreen(pos.xy), 0.0, 1.0);
}
"""
