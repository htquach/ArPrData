# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.

import sys
import os
from unittest import TestCase
from subprocess import check_output, CalledProcessError


class TestPyLint(TestCase):
    def _run_test(self, file_name, disable="", enable=""):
        try:
            root_dir = os.path.join(os.path.dirname(__file__), "..")
            check_output("pylint %s --disable=%s, --enable=%s" %
                         (file_name, disable, enable), cwd=root_dir)
        except CalledProcessError as e:
            self.fail(e.output)

    def test_arprdata(self):
        self._run_test("arprdata.py")