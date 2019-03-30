"""
Creating a graphml node to add the relevant javascript element that will load the .swf
"""

import os
import posixpath
import tempfile

from sphinx.addnodes import download_reference
from sphinx.writers.html5 import HTML5Translator

import graphml2svg


class graphml_reference(download_reference):
    pass


def visit_graphml_reference(self, node):
    """
    Converts the graphml to svg and insert the SVG into the page
    """
    if isinstance(self, HTML5Translator):
        atts = {}
        file = None
        if 'refuri' in node:
            atts['path'] = node['refuri']
            # TODO: download file in a temp location to convert to SVG
            file = ''
        elif 'filename' in node:
            file = os.path.join(os.path.dirname(node.source), node['reftarget'])
            atts['path'] = posixpath.join(self.builder.dlpath, node['filename'])

        if file:
            svg_file=tempfile.NamedTemporaryFile('w')
            svg_filename = svg_file.name
            svg_file.close()
            graphml2svg.Graph(file, output_path=svg_filename).run()
            with open(svg_filename, 'r') as svg_file:
                self.body.append(svg_file.read())
            os.remove(svg_filename)

    self.visit_download_reference(node)

def depart_graphml_reference(self, node):
    self.depart_download_reference(node)
