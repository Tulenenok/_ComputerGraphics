class Tools:
    EXIT_SUCCESS = 0
    EXIT_FAILURE = 1
    SEPARATOR_COORDS = ' ; '
    SEPARATOR_POL = '---'
    INVALID_FILENAME = -1
    INVALID_LISTNAME = -2
    INVALID_HEAD = -3
    INVALID_DATA = -4
    INVALID_FORMAT_DATA = -5
    OBSCURE_ERROR = -6

    @staticmethod
    def isInt(x):
        try:
            x = int(x)
            return True
        except:
            return False

    @staticmethod
    def isFloat(x):
        try:
            x = float(x)
            return True
        except:
            return False

    @staticmethod
    def isRightFilename(filename):
        try:
            f = open(filename, 'r')
            f.close()
            return True
        except:
            return False

    @staticmethod
    def rgb_to_hex(r, g, b):
        rh = '0' + str(hex(int(r * 255))[2:].upper())
        gh = '0' + str(hex(int(g * 255))[2:].upper())
        bh = '0' + str(hex(int(b * 255))[2:].upper())
        return f'#{rh[-2:]}{gh[-2:]}{bh[-2:]}'