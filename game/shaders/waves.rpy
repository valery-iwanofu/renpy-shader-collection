init -10 python:
    from renpy.display.layout import Container

    renpy.register_shader("collection.waves", variables="""
        uniform float u_lod_bias;
        uniform sampler2D tex0;

        varying vec2 v_tex_coord;
        varying vec2 v_position;

        uniform float u_wave_size;
        uniform float u_amplitude;

        uniform float u_custom_time;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_position = a_position.xy;
    """, fragment_300="""
        vec2 uv = v_tex_coord;

        vec2 center_dist = 1.0 - abs(uv - .5) / .5;
        vec4 color = texture2D(tex0, uv, u_lod_bias);
        float arg = sin(u_custom_time + v_position.y / u_wave_size);

        gl_FragColor = texture2D(tex0, uv + arg / u_amplitude * center_dist);
    """)

    class WavesBase(Container):
        def __init__(self, image, **kwargs):
            child = renpy.easy.displayable(image)
            Container.__init__(self, child, **kwargs)

        def _get_amplitude(self):
            raise NotImplementedError

        def _get_wave_size(self):
            raise NotImplementedError

        def _get_time_offset(self):
            return 0

        def render(self, width, height, st, at):
            child = self.child
            child_render = renpy.render(child, width, height, st, at)
            rv = renpy.Render(child_render.width, child_render.height)
            child_pos = child.place(rv, 0, 0, width, height, child_render)
            self.offsets = [child_pos]

            rv.add_shader('collection.waves')
            rv.add_uniform('u_wave_size', self._get_wave_size())
            rv.add_uniform('u_amplitude', self._get_amplitude())
            rv.add_uniform('u_custom_time', st)

            renpy.redraw(self, 0)
            
            return rv

    class Waves(WavesBase):
        def __init__(self, image, wave_size=150.0, amplitude=30.0, time_offset=0, **kwargs):
            WavesBase.__init__(self, image, **kwargs)
            self._wave_size = wave_size
            self._amplitude = amplitude
            self._time_offset = time_offset

        def _get_wave_size(self):
            return self._wave_size

        def _get_amplitude(self):
            return self._amplitude

        def _get_time_offset(self):
            return self._time_offset


transform waves_shader(wave_size=150.0, amplitude=30.0):
    shader "collection.waves"
    u_wave_size wave_size
    u_amplitude amplitude
    u_custom_time 0.0
    # so bad
    block:
        linear 100000000 u_custom_time 100000000
        u_custom_time 0.0
        repeat