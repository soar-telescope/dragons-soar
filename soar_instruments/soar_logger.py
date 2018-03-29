import logging

__all__ = ['COLORS', 'get_logger']

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

RESET_SEQ = '\033[0m'
COLOR_SEQ = '\033[1;%dm'
BOLD_SEQ = '\033[1m'

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': RED,
    'ERROR': RED
}


def get_logger(logger_name, use_colors=True):
    """
    Return a logger with the "logger_name".

    Args:
        logger_name (str) : the logger name to be used in different contexts.
        use_colors (bool, optional) : use colors on Stream Loggers.

    Returns:
        _logger (logging.Logger) : the logger to be used.
    """
    message_format = " [%(levelname).1s %(asctime)s %(name)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    formatter = SoarLogFormatter(message_format, datefmt=date_format, use_colours=use_colors)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    _logger = logging.getLogger(logger_name)
    _logger.addHandler(handler)

    return _logger


class SoarLogFormatter(logging.Formatter):
    """
    A customized formatter to be used at Dragons Soar.

    Attributes:
        char_left (str): the character used to set where the coloured string
            starts (default = "[").
        char_right (str): the character used to set where the coloured string
            ends (default = "]")
    Args:
        fmt (str, optional): a string containing the logging format
            (See `Logging facility for Python`_).
        datefmt (str, optional): a string containing the date format for
            logging (See `Logging facility for Python`_).
        use_colours (bool, optional): set colored output (default: True).

    ..  _Logging facility for Python:
        https://docs.python.org/3/library/logging.html

    """

    def __init__(self, fmt="%(levelno)s: %(msg)s", datefmt=None, use_colours=True):
        logging.Formatter.__init__(self, fmt, datefmt=datefmt)
        self.use_colours = use_colours
        self.char_left = "["
        self.char_right = "]"

    def color_format(self, message, levelname):
        colour = COLOR_SEQ % (30 + COLORS[levelname])

        message = message.replace(self.char_left, "{:s} {:s}".format(colour, self.char_left))
        message = message.replace(self.char_right, "{:s} {:s}".format(self.char_right, RESET_SEQ))

        return message

    def format(self, record):
        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        if self.use_colours:
            result = self.color_format(result, record.levelname)

        return result
