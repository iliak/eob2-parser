
class Comparator:
    """

    """

    def __init__(self, value):
        """

        :param reader:
        """
        self.operator = value
        if self.operator == 0xff:
            self.text = " == "
        elif self.operator == 0xfe:
            self.text = " != "
        elif self.operator == 0xfd:
            self.text = " < "
        elif self.operator == 0xfc:
            self.text = " <= "
        elif self.operator == 0xfb:
            self.text = " > "
        elif self.operator == 0xfa:
            self.text = " >= "
        elif self.operator == 0xf9:
            self.text = " AND "
        elif self.operator == 0xf8:
            self.text = " OR "
        else:
            self.text = " [??] "

    def run(self, maze, assets):

        return self.text
