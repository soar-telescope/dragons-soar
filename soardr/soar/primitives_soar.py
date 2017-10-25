#
#                                                                         soardr
#
#                                                             primitives_soar.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt

from soardr import PrimitivesSoarBASE

#from recipe_system.utils.decorators import parameter_override
# ------------------------------------------------------------------------------
#@parameter_override
class Soar(PrimitivesSoarBASE):
    
    tagset = set(["SOAR"])

    def __init__(self, adinputs, **kwargs):
        super(Soar, self).__init__(adinputs, **kwargs)

    def helloWorld(self, adinputs, **params):
        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return #adinputs
