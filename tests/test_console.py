#!/usr/bin/python3
"""This is the test for console.py"""

import unittest
import sys
from unittest.mock import create_autospec
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """This is the test for console.py"""    
    def setUp(self):
        """This is the setUp mock stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """This is the test of create"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """This is the test for exit"""
        cmd = self.create()
        self.assertRaises(SystemExit, quit)
