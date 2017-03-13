"""
Meta-classes are callables that are used to create classes
"""

def my_meta(name, bases, dicts):
# Simple meta class. Prints class name, its bases and its __dict__ and then
# creates the class via type()
    print(
        f'Class {name} has bases {bases} and has attributes {dicts}'
    )

    return type(name, bases, dicts)


class Foo(metaclass=my_meta):
    foo = 'bar'


class FooBar(Foo, metaclass=my_meta):

    def say(self):
        return f'foo {self.foo}'



