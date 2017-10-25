#
#                                                                         soardr
#
#                                                          primitives_goodman.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt

from soardr.soar.primitives_soar import Soar

#from recipe_system.utils.decorators import parameter_override
# ------------------------------------------------------------------------------
#@parameter_override
class Goodman(Soar):
    """
    This is the class containing the generic Gemini primitives.

    """
    tagset = set(["SOAR", "GOODMAN"])

    def __init__(self, adinputs, **kwargs):
        super(Goodman, self).__init__(adinputs, **kwargs)
        # self.parameters = ParametersGoodman

    def gudayMate(self, adinputs, **params):
        """

        """
        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return #adinputs
