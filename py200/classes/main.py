class BodyPen:
    """class Describes pen"""
    def __init__(self, color, weigth=100, name=None):
        self.color = self.init_color(color)
        self.weigth = weigth
        if name is None:
            self.name = ""
        else:
            self.name = name

    def init_color(self, color):
        if not isinstance(color, str):
            raise TypeError(f"color must be str, not {type(color)}")

    def get_weigth(self):
        return self.weigth

# class kernel:
#     def __init__(self, color, weigth=100):
#         self.color = self.init_color(color)
#         self.weigth = weigth
#
#     def init_color(self, color):
#         if not isinstance(color, str):
#             raise TypeError(f"color must be str, not {type(color)}")
#
#     def get_weigth(self):
#         return self.weigth

