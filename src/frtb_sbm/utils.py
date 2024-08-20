class DotDict:
    def __init__(self, **entries):
        for key, value in entries.items():
            if isinstance(value, dict):
                value = DotDict(**value)
            self.__dict__[key] = value
            