"""
Test recipe for SAMI BIAS data.
"""

recipe_tags = set(['SAMI', 'BIAS'])


def grecipe(p):
    print(p.__class__)
    p.helloWorld()
    p.gudayMate()
    p.samiPrimitive()
    return

default = grecipe