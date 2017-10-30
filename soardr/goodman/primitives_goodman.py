#
#                                                                         soardr
#
#                                                          primitives_goodman.py
# ------------------------------------------------------------------------------
from gempy.gemini import gemini_tools as gt

from soardr.soar.primitives_soar import Soar

from ..utils.logging_handlers import log_adjust
# ------------------------------------------------------------------------------
@log_adjust
class Goodman(Soar):
    """
    This is the class containing the generic Gemini primitives.

    """
    tagset = set(["SOAR", "GOODMAN"])

    def __init__(self, adinputs, **kwargs):
        super(Goodman, self).__init__(adinputs, **kwargs)

    def gudayMate(self, *args, **kwargs):

        log = self.log
        log.stdinfo(gt.log_message("primitive", self.myself(), "starting"))
        for ad in self.adinputs:
            log.stdinfo("Hello World! This is {}".format(ad.filename))
            log.stdinfo("Sporting a tagset: {}".format(ad.tags))
            log.stdinfo("Coming to you from {}.".format(self.myself()))

        return

    def goodmanPrimitive(self, *args, **kwargs):
        log = self.log
        log.stdinfo(gt.log_message(" This is a ", self.myself()))
        for ad in self.adinputs:
            log.stdinfo("The file name is: {}".format(ad.filename))
            log.stdinfo("Tags are: {}".format(ad.tags))
