import re

from .tools import SphinxBuildTestCase


class DirectiveTestCase(SphinxBuildTestCase):

    def test_output(self):

        self.assertOutputContains('index', re.compile(
            r'<script language="javascript" type="text/javascript">'
                r'RunPlayer\("height", "200px", "graphURL", "_downloads/[0-9a-f]{'r'32}/empty_chart.graphml"\);'
            r'</script>'
            r'<a class="reference download internal" download="" href="_downloads/[0-9a-f]{32}/empty_chart.graphml">'
                r'<code class="xref download docutils literal notranslate">'
                    r'<span class="pre">GraphML</span> '
                    r'<span class="pre">file</span>'
                r'</code>'
            r'</a>'
        ))
