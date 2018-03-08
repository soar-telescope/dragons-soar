"""
Test recipe for SAMI IMAGE data.
"""

recipe_tags = set(['SAMI', 'IMAGE'])


def grecipe(p):
    p.helloWorld()
    p.gudayMate()
    p.samiPrimitive()
    return

default = grecipe
