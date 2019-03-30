from .tools import SphinxBuildTestCase


class DirectiveTestCase(SphinxBuildTestCase):

    def test_output(self):

        self.assertOutputContains(
            'index',
            '<script language="javascript" type="text/javascript">'
                'RunPlayer("height", "200px", "graphURL", "_downloads/701917bc8d4c77f259d4c5c32401e00e/empty_chart.graphml");'
            '</script>'
            '<a class="reference download internal" download="" href="_downloads/701917bc8d4c77f259d4c5c32401e00e/empty_chart.graphml">'
                '<code class="xref download docutils literal notranslate">'
                    '<span class="pre">GraphML</span> '
                    '<span class="pre">file</span>'
                '</code>'
            '</a>'
        )
