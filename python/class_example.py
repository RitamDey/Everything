class Tiger:
    __type = 'Cat'
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f'{self.name} says Ghrrrrr!!! Ghrrrr!!!')
    def __repr__(self):
        return f"< Dog object: {self.name} >"
    def __getType(self):
        return self.__type

obj = Tiger('Sherro')
print(obj)
print(obj._Tiger__type == obj._Tiger__getType())
obj.bark()
print(f'Do you the Tiger is actually {obj._Tiger__getType()}....Oopps')
