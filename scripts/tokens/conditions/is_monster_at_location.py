from location import Location


class IsMonsterAtLocation:
    """
    Test block flag
    https://github.com/scummvm/scummvm/blob/master/engines/kyra/script/script_eob.cpp#L886
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.location = None
        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        # TODO: Location is wrong...
        self.location = Location(reader)

    def decode(self, tokens, maze, assets):
        return f"monster at {self.location}"
