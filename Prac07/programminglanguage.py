class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appear" \
               "ed in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    pass
