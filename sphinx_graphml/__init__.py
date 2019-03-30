"""
Extension setup hook
"""

import os

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

    app.add_js_file('js/GraphMLViewer.js')

    # modifying raw config is the only way to add a static path from which static files can be
    # collected, see:
    # https://github.com/sphinx-doc/sphinx/issues/1379
    # https://groups.google.com/forum/#!msg/sphinx-users/Z-wcktOhIAc/pGDWO0yVBQAJ
    app.config._raw_config.setdefault('html_static_path', []).append(
        os.path.join(os.path.dirname(__file__), 'static')
    )

    return {'version': __version__}
