default waves_demo_wave_size = 150.0
default waves_demo_amplitude = 30.0

init python:
    class ControlableWaves(WavesBase):
        def __init__(self, image, wave_size, amplitude, **kwargs):
            WavesBase.__init__(self, image, **kwargs)
            self._wave_size = wave_size
            self._amplitude = amplitude

        def _get_wave_size(self):
            return self._wave_size.get()

        def _get_amplitude(self):
            return self._amplitude.get()

style waves_demo_field is hbox


screen waves_demo:
    frame:
        xalign 1.0
        yoffset 32
        xoffset -32
        xsize 600

        vbox:
            vbox:
                text _('Wave size(%.3f):'% waves_demo_wave_size)
                bar style 'slider' value VariableValue('waves_demo_wave_size', 500.0)
            vbox:
                text _('Wave amplitude(%.3f):'% waves_demo_amplitude)
                bar style 'slider' value VariableValue('waves_demo_amplitude', 500.0)
            textbutton 'Return' xalign 1.0 action Return(True)

label waves_demo:
    scene expression ControlableWaves('bg ext_beach_day', VariableSimpleValue('waves_demo_wave_size'), VariableSimpleValue('waves_demo_amplitude'))
    show screen waves_demo with dissolve

    $ ui.interact()

    hide screen waves_demo with dissolve

    return

transform waves_demo_transform:
    contains waves_shader