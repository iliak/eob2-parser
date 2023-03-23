class GetTriggerFlag:
    """

    Get last script flag
    https://github.com/scummvm/scummvm/blob/master/engines/kyra/script/script_eob.cpp#L1093
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

    def decode(self, tokens, maze, assets):

        return "trigger flag"

