"""
This extensions allows including .graphml files (generated using yEd) in the documentation
"""

from sphinx.roles import XRefRole
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import length_or_unitless

from .nodes import graphml_reference


class GraphDirective(Directive):
    has_content = True
    option_spec = {
        'height': length_or_unitless
    }

    role = XRefRole(nodeclass=graphml_reference)

    def run(self):
        text = 'GraphML file <%s>' % self.content[0]
        rawtext = ':download:`%s`' % text
        nodes = self.role('download', rawtext, text, self.lineno, self.state.inliner)[0]
        nodes[0]['height'] = self.options.get('height', '300px')
        return nodes
