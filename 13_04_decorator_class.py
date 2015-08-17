class trace_call:
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print("Function executed: {} args: {}".format(self.f.__name__,
                                                      args))
        self.f(*args, **kwargs)

@trace_call
def add(a, b):
    return a + b

add(1, 3)
