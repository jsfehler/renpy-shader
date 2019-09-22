define PS_BEAM_FADE_2D = """

VARYING vec2 varUv;

UNIFORM sampler2D tex0;
UNIFORM float shownTime;

const float intensity = 1.0;

float rand(vec2 co){
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

void main()
{
    float f = rand(vec2(0.0, varUv.y)) * rand(vec2(0.0, gl_FragCoord.y + shownTime));
    float fade = shownTime / 2.0;

    vec4 color = vec4(-f * 0.5, f * 0.5, f, 0.0);
    vec4 diffuse = texture2D(tex0, varUv);
    gl_FragColor = vec4((diffuse * gl_Color + color * intensity).rgb, max(diffuse.a - fade, 0.0));
}
"""
