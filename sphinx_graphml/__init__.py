"""
Extension setup hook
"""

from .version import __version__

def setup(app):
    """
    Registers directives, roles, etc.

    :param app: the Sphinx app
    """

    return {'version': __version__}

