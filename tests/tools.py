"""
Testing tools
"""

import os
import sys
import re
from shutil import rmtree
from unittest import TestCase

from sphinx.cmd.build import main as sphinx_main
from sphinx.util.osutil import cd


__test__ = False
__unittest = True


class SphinxBuildTestCase(TestCase):
    """
    Base test case that builds the sphinx documentation and deletes it once the tests have run
    """

    docs_dir = None

    @classmethod
    def setup_class(cls):
        """
        Run Sphinx against the dir adjacent to the testcase
        """
        cls.docs_dir = os.path.join(
            os.path.dirname(sys.modules[cls.__module__].__file__), 'src'
        )
        with cd(cls.docs_dir):
            if sphinx_main(['.', '-b', 'html', '-E', '_build']):
                raise RuntimeError('Sphinx build error')

    @classmethod
    def teardown_class(cls):
        if cls.docs_dir is not None and not getattr(cls, 'keep_output', False):
            rmtree(os.path.join(cls.docs_dir, '_build'))

    def assertOutputContains(self, filename, expected_output):
        if self.docs_dir is None:
            raise AssertionError("No docs dir defined")
        with open(os.path.join(self.docs_dir, '_build', '%s.html' % filename), 'r') as f:

            if isinstance(expected_output, re._pattern_type):
                self.assertRegexpMatches(f.read(), re.compile('.*' + expected_output.pattern),
                                         expected_output.flags)
            else:
                self.assertIn(expected_output, f.read())