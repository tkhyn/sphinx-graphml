"""
This extensions allows including .graphml files (generated using yEd) in the documentation
"""

from sphinx.roles import XRefRole
from docutils.parsers.rst import Directive

from .nodes import graphml_reference


class GraphDirective(Directive):

    has_content = True
    role = XRefRole(nodeclass=graphml_reference)

    def run(self):
        text = 'GraphML file <%s>' % self.content[0]
        rawtext = ':download:`%s`' % text
        nodes = self.role('download', rawtext, text, self.lineno, self.state.inliner)[0]
        return nodes
