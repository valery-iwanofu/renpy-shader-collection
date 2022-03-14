default color_picker_demo_color = Color('#922222')

init python:
    def __color_picker_demo_bg(st, at):
        return Transform('images/ext_beach_day.jpg', matrixcolor=TintMatrix(color_picker_demo_color)), None

image color_picker_demo_bg = DynamicDisplayable(__color_picker_demo_bg)

screen color_picker_demo:
    frame:
        xalign .5
        yalign .5
        vbox:
            hbox:
                frame:
                    xsize 300
                    ysize 300
                    background Solid(color_picker_demo_color)

                use color_picker(
                    VariableSimpleValue('color_picker_demo_color')
                )
            textbutton 'Return' action Return(True)

label color_picker_demo:
    scene color_picker_demo_bg
    show screen color_picker_demo with dissolve

    $ ui.interact()

    hide screen color_picker_demo with dissolve

    return