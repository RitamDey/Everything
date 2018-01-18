class Vector:
    def __init__(self, **coords):
        private = {'_'+k: v for k, v in coords.items()}
        self.__dict__.update(private)

    def __getattr__(self, name):
        name = '_'+name
        return getattr(self, name)

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __repr__(self):
        return "{}({})".format(
                self.__class__.__name__,
                ', '.join("{k}={v}".format(
                        k=k[1:],
                        v=self.__dict__[k])
                    for k in sorted(self.__dict__.keys())
                    ))
