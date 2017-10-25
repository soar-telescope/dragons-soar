from functools import wraps
from copy import deepcopy

from gempy.utils import logutils
import inspect
# ------------------------------------------------------------------------------
LOGINDENT = 0
log = logutils.get_logger(__name__)

# ------------------------------------------------------------------------------
def set_logging(pname):
   global LOGINDENT
   LOGINDENT += 1
   logutils.update_indent(LOGINDENT)
   stat_msg = "PRIMITIVE: {}".format(pname)
   log.status(stat_msg)
   log.status("-" * len(stat_msg))
   return

def unset_logging():
   global LOGINDENT
   log.status(".")
   LOGINDENT -= 1
   logutils.update_indent(LOGINDENT)
   return    

def make_class_wrapper(wrapped):
    @wraps(wrapped)
    def class_wrapper(cls):
        for attr_name in dir(cls):
            if attr_name.startswith("_"):        # no prive, no magic
                continue

            attr_fn = getattr(cls, attr_name)
            if callable(attr_fn):
                if attr_name not in attr_fn.im_class.__dict__:
                    continue
                else:
                    setattr(cls, attr_name, wrapped(attr_fn))
        return cls
    return class_wrapper

@make_class_wrapper
def log_adjust(fn):
    @wraps(fn)
    def gn(*args, **kwargs):
        pobj = args[0]
        pname = fn.__name__
        set_logging(pname)
        ret_value = fn(*args, **kwargs)
        unset_logging()
        return ret_value
    return gn
   
