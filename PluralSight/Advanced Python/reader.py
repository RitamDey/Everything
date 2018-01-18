import struct
import pprint
from binascii import hexlify


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return "Color({}, {}, {})".format(self.red, self.green, self.blue)


class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return "Vertex({!r}, {!r})".format(self.vector, self.color)


def make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z), Color(red, green, blue))


if __name__ == '__main__':
    with open('colors.bin', 'rb') as f:
        buffer_f = f.read()

    print(len(buffer_f))
    
    hex_buffer = hexlify(buffer_f).decode("ascii")
    hex_pairs = ' '.join(hex_buffer[i:i+2] for i in range(len(hex_buffer), 2))
    print(hex_pairs)

    # The first argument is the format string
    # The `@` stands to mention the runtime to use native ordering
    # The `f`s stands to mention to interpret a C `float`
    # The `H`s stands to mention to interpret a C `unsigned short`
    # The `x`s stands to mention to interpret a C padding that aligns struct
    vertices = []
    for feilds in struct.iter_unpack("@3f3Hxx", buffer_f):
        vertices.append(make_colored_vertex(*feilds))

    pprint.pprint(vertices)
