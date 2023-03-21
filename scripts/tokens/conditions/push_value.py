class PushValue:
    """
    BOGUS
    """

    def __init__(self, value):
        """

        """

        self.value = value

    def run(self, maze, assets):
        return f"push 0x{self.value:04X}"
