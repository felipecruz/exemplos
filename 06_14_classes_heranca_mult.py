class A:
    def run(self):
        return "A"

class B:
    def run(self):
        return "B"

class C(A, B):
    pass

a = A()
b = B()
c = C()
assert "A" == c.run()

