"""
Extension setup hook
"""

from .version import __version__
from .directives import GraphDirective
from .nodes import graphml_reference, visit_graphml_reference, depart_graphml_reference


def setup(app):
    """
    Registers directives, roles, etc.

    :param app: the Sphinx app
    """

    app.add_directive('graph', GraphDirective)
    app.add_node(graphml_reference, html=(visit_graphml_reference, depart_graphml_reference))

    return {'version': __version__}
