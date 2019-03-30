import re

from .tools import SphinxBuildTestCase


class DirectiveTestCase(SphinxBuildTestCase):

    def test_output(self):

        self.assertOutputContains('index', re.compile(
            '<script language="javascript" type="text/javascript">'
                'RunPlayer\("height", "200px", "graphURL", "_downloads/[0-9a-f]{32}/empty_chart.graphml"\);'
            '</script>'
            '<a class="reference download internal" download="" href="_downloads/[0-9a-f]{32}/empty_chart.graphml">'
                '<code class="xref download docutils literal notranslate">'
                    '<span class="pre">GraphML</span> '
                    '<span class="pre">file</span>'
                '</code>'
            '</a>'
        ))
