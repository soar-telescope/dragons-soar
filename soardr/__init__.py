
from inspect import stack

from gempy.utils import logutils


class PrimitivesSoarBASE(object):
    
    tagset = None

    def __init__(self, adinputs, **kwargs):
        self.log = logutils.get_logger(__name__)
        self.myself = lambda: stack()[1][3]
        self.adinputs = adinputs
