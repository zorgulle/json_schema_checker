class ValidatorTypeUndefinedException(Exception):
    pass


class SimpleValidator:
    type = None

    def is_valid(self, value) -> bool:
        return isinstance(value, self.type)

    def __new__(cls, *args, **kwargs):
        if cls.type is None:
            raise ValidatorTypeUndefinedException

        return super().__new__(cls, *args, **kwargs)

class Int(SimpleValidator):
    type = int

class String(SimpleValidator):
    type = str
