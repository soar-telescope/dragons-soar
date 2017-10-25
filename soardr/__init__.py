# ------------------------------------------------------------------------------
from inspect import stack

from gempy.utils import logutils

#from recipe_system.utils.decorators import parameter_override

# ------------------------------------------------------------------------------
class PrimitivesSoarBASE(object):
    
    tagset = None

    def __init__(self, adinputs, **kwargs):
        self.log    = logutils.get_logger(__name__)
        self.myself = lambda: stack()[1][3]
