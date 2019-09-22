define PS_WALK_2D = """

VARYING vec2 varUv;

UNIFORM sampler2D tex0;
UNIFORM sampler2D tex1;
UNIFORM float shownTime;
UNIFORM float animationTime;

void main()
{
    vec4 color1 = texture2D(tex0, varUv);
    vec4 weights = texture2D(tex1, varUv);
    float influence = weights.r;

    if (influence > 0.0) {
        float speed = sin(animationTime * 5.0);
        float xShift = sin(speed + varUv.x * varUv.y * 10) * influence * 0.01;
        float yShift = cos(speed + varUv.x * varUv.y * 5) * influence * 0.01;

        gl_FragColor = texture2D(tex0, varUv + vec2(xShift, yShift));
    }
    else {
        gl_FragColor = color1;
    }
}
"""
