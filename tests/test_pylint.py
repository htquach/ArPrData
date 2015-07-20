# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.

import os
from unittest import TestCase
from subprocess import check_output, CalledProcessError


class TestPyLint(TestCase):
    def _run_test(self, file_name, disable="", enable=""):
        try:
            root_dir = os.path.join(os.path.dirname(__file__), "..")
            # check_output("pylint %s --disable=%s, --enable=%s" %
            #              (file_name, disable, enable), cwd=root_dir)
            check_output(["pylint",
                          "--msg-template={path}:{line}: "
                          "[{msg_id}({symbol}), {obj}] {msg}",
                          file_name], cwd=root_dir)
        except CalledProcessError as e:
            self.fail(e.output)

    def test_main(self):
        self._run_test("main.py")

    def test_policy(self):
        self._run_test("policy.py")

    def test_policyqueue(self):
        self._run_test("policyqueue.py")

    def test_arpr(self):
        self._run_test("arpr.py")

    def test_db(self):
        self._run_test("db.py")

    def test_exc(self):
        self._run_test("exc.py")

    def test_constant(self):
        self._run_test("constant.py")
