
image bg ext_beach_day = 'images/ext_beach_day.jpg'

define config.log_gl_shaders = True



label start:
    jump loop

label loop:
    scene bg ext_beach_day with dissolve
    menu:
        'Waves':
            call waves_demo
        'Color picker':
            call color_picker_demo
            
    jump loop
