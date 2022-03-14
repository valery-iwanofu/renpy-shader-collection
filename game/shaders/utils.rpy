init -100 python:
    @renpy.pure
    class SimpleValue(renpy.object.Object):
        def get(self):
            raise Exception("Not implemented.")

        def set(self, value):
            raise Exception("Not implemented.")

    @renpy.pure
    class FieldSimpleValue(SimpleValue):
        def __init__(self, obj, name):
            self._obj = obj
            self._name = name

        def get(self):
            return getattr(self._obj, self._name)

        def set(self, value):
            setattr(self._obj, self._name, value)
            renpy.restart_interaction()

    @renpy.pure
    def VariableSimpleValue(name):
        return FieldSimpleValue(store, name)

    @renpy.pure
    class ScreenSimpleValue(SimpleValue):
        def __init__(self, name):
            self._name = name
            self._screen = renpy.current_screen()

        def get(self):
            return self._screen.scope[self._name]

        def set(self, value):
            self._screen.scope[self._name] = value
            renpy.restart_interaction()

    @renpy.pure
    class SimpleBarValue(BarValue):
        def __init__(self, simple_value, range, max_is_zero=False, style='bar', offset=0, step=None, action=None, force_step=False):
            self._simple_value = simple_value

            self.range = range
            self.max_is_zero = max_is_zero
            self.style = style
            self.offset = offset
            self.force_step = force_step

            if step is None:
                if isinstance(range, float):
                    step = range / 10.0
                else:
                    step = max(range / 10, 1)

            self.step = step
            self.action = action

        def changed(self, value):
            if self.max_is_zero:
                if value == self.range:
                    value = 0
                else:
                    value = value + 1

            value += self.offset

            self._simple_value.set(value)
            renpy.restart_interaction()

            renpy.run(self.action)

        def get_adjustment(self):
            value = self._simple_value.get()

            value -= self.offset

            if self.max_is_zero:
                if value == 0:
                    value = self.range
                else:
                    value = value - 1

            return ui.adjustment(
                range=self.range,
                value=value,
                changed=self.changed,
                step=self.step,
                force_step=self.force_step,
            )

        def get_style(self):
            return self.style, "v" + self.style