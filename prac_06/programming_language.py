"""
Programming Languages
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True, year=0):
        """ Initialize programming language instance"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.is_dynamic(),
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
