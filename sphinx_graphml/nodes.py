"""
Creating a graphml node to add the relevant javascript element that will load the .swf
"""


import posixpath

from sphinx.addnodes import download_reference

from sphinx.writers.html import HTMLTranslator
from sphinx.writers.html5 import HTML5Translator

from docutils.nodes import Element


class graphml_reference(download_reference):
    pass


def visit_graphml_reference(self, node):
    """
    Appends a javascript element calling GraphML's RunPlayer function
    """
    if isinstance(self, (HTMLTranslator, HTML5Translator)):
        atts = {'height': node['height']}
        if 'refuri' in node:
            atts['path'] = node['refuri']
        elif 'filename' in node:
            atts['path'] = posixpath.join(self.builder.dlpath, node['filename'])

        if 'path' in atts:
            self.body.append(self.starttag(
                Element(), 'script',
                'RunPlayer("height", "%(height)s", "graphURL", "%(path)s");' % atts,
                type="text/javascript", language="javascript"
            ))
            self.body.append('</script>')

    self.visit_download_reference(node)

def depart_graphml_reference(self, node):
    self.depart_download_reference(node)
