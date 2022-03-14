init -100 python in shaders:
    class vec2(tuple):
        def __new__(cls, *args):
            if len(args) == 1:
                return tuple.__new__(cls, (args[0], args[0]))
            elif len(args) == 2:
                return tuple.__new__(cls, args)
            raise ValueError('vec2 accept 1 or 2 arguments, not %s' % len(args))

        @property
        def x(self):
            return self[0]

        @property
        def y(self):
            return self[1]

        def __add__(self, o):
            return vec2(self[0] + o[0], self[1] + o[1])

        def __sub__(self, o):
            return vec2(self[0] - o[0], self[1] - o[1])

        def __mul__(self, m):
            return vec2(self[0] * m, self[1] * m)

    class vec3(tuple):
        def __new__(cls, *args):
            if len(args) == 1:
                return tuple.__new__(cls, (args[0], args[0], args[0]))
            elif len(args) == 3:
                return tuple.__new__(cls, args)
            raise ValueError('vec3 accept 1 or 3 arguments, not %s' % len(args))

        @property
        def x(self):
            return self[0]

        @property
        def y(self):
            return self[1]

        @property
        def z(self):
            return self[2]

        def __add__(self, o):
            return vec3(self[0] + o[0], self[1] + o[1], self[2] + o[2])

        def __sub__(self, o):
            return vec3(self[0] - o[0], self[1] - o[1], self[2] - o[2])

        def __mul__(self, m):
            return vec3(self[0] * m, self[1] * m, self[2] * m)
        
    def mix(x, y, a):
        return x * (1 - a) + y * a
