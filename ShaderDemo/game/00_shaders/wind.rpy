define LIB_WIND = """

UNIFORM sampler2D tex0;
UNIFORM sampler2D tex1;

UNIFORM float mouseEnabled;
UNIFORM vec2 mousePos;

UNIFORM vec2 eyeShift;
UNIFORM vec2 mouthShift;

const float WIND_SPEED = 5.0;
const float DISTANCE = 0.0075;
const float FLUIDNESS = 0.75;
const float TURBULENCE = 15.0;
const float FADE_IN = 1.0; //In seconds

vec4 applyWind(vec2 uv, float time)
{
    float movement = 0.1;

    vec4 weights = texture2D(tex1, uv);

    if (weights.g > 0.0) {
        vec2 eyeCoords = uv + (eyeShift * weights.g);
        if (texture2D(tex1, eyeCoords).g > 0.0) {
            return texture2D(tex0, eyeCoords);
        }
    }

    if (weights.b > 0.0) {
        vec2 smileCoords = uv + (mouthShift * weights.b);
        if (texture2D(tex1, smileCoords).b > 0.0) {
            return texture2D(tex0, smileCoords);
        }
    }

    float timeFade = min(time / FADE_IN, 1.0);
    float influence = weights.r * (0.5 + (movement * 1.25)) * timeFade;

    if (mouseEnabled > 0.0) {
        //Use mouse position to set influence
        influence = (1.0 - distance(mousePos, uv) * 5.0) * 2.0;
    }

    if (influence > 0.0) {
        float modifier = sin(uv.x + time) / 2.0 + 1.5;
        float xShift = sin((uv.y * 20.0) * FLUIDNESS + (time * WIND_SPEED)) * modifier * influence * DISTANCE;
        float yShift = cos((uv.x * 50.0) * FLUIDNESS + (time * WIND_SPEED)) * influence * DISTANCE;
        return texture2D(tex0, uv + vec2(xShift, yShift));
    }
    else {
        return texture2D(tex0, uv);
    }
}
"""

define PS_WIND_2D = LIB_WIND + """

VARYING vec2 varUv;

UNIFORM float shownTime;
UNIFORM float animationTime;

void main()
{
    gl_FragColor = applyWind(varUv, shownTime);
}
"""


define PS_SKINNED = LIB_WIND + """

VARYING vec2 varUv;
VARYING float varAlpha;

UNIFORM float wireFrame;
UNIFORM float shownTime;

void main()
{
    vec4 color = applyWind(varUv, shownTime);

    color.rgb *= 1.0 - wireFrame;
    color.a = (color.a * varAlpha) + wireFrame;
    gl_FragColor = color;
}
"""
