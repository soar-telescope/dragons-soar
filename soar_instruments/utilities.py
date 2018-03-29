
from collections import namedtuple

Section = namedtuple('Section', 'x1 x2 y1 y2')

__all__ = ['Section']


def section_to_tuple(section):
    """
    Takes a string describing a section in the raw format found on
    headers ("[x1:x2,y1:y2]"), and returns a `Section` named tuple
    with the values as integers.

    Parameters
    ----------
    section: str
             The section (in the form [x1:x2,y1:y2]) to be converted to a tuple

    Returns
    -------
    An instance of `Section`
    """
    return Section(*section_str_to_int_list(section))


def section_str_to_int_list(section):
    """
    Convert the input section in the form '[x1:x2,y1:y2]' to a tuple in the
    form (x1 - 1, x2, y1 - 1, y2), where x1, x2, y1 and y2 are
    integers. The values in the output tuple are converted to use 0-based and
    non-inclusive indexing, making it compatible with numpy.

    :param section: the section (in the form [x1:x2,y1:y2]) to be
                    converted to a tuple
    :type section: string

    :rtype: tuple
    :return: the converted section as a tuple that uses 0-based and
             non-inclusive in the form (x1 - 1, x2, y1 - 1, y2)
    """
    # Strip the square brackets from the input section and then create a
    # list in the form ['x1:x2','y1:y2']
    xylist = section.strip('[]').split(',')

    # Create variables containing the single x1, x2, y1 and y2 values
    x1 = int(xylist[0].split(':')[0]) - 1
    x2 = int(xylist[0].split(':')[1])
    y1 = int(xylist[1].split(':')[0]) - 1
    y2 = int(xylist[1].split(':')[1])

    # Return the tuple in the form (x1 - 1, x2, y1 - 1, y2)
    return x1, x2, y1, y2


