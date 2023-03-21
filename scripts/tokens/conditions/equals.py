class Equals:
    """

    """
    def __init__(self, value):
        pass

    def decode(self, tokens, maze, assets):
        right = tokens.pop()
        rtext = right.decode(tokens, maze, assets)

        left = tokens.pop()
        ltext = left.decode(tokens, maze, assets)

        return f"{ltext} == {rtext}"
