#!/usr/bin/python3
import sys
sys.path.append("..")
import unittest
from console import HBNBCommand
import io

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_quit(self):
        self.assertEqual(self.console.do_quit(), True)

    def test_EOF(self):
        self.assertEqual(self.console.do_EOF(''), True)

    def test_empty_line(self):
        self.console.onecmd("")
        self.assertEqual(self.capturedOutput.getvalue(), "")

    def test_help(self):
        self.console.onecmd("help")
        output = self.capturedOutput.getvalue()
        self.assertIn("quit", output)
        self.assertIn("EOF", output)

    def test_do_all(self):
        self.console.onecmd("all")
        output = self.capturedOutput.getvalue()
        self.assertIn("** class doesn't exist **", output)

    def test_do_all_with_class_name(self):
        self.console.onecmd("all User")
        output = self.capturedOutput.getvalue()
        self.assertIn("[]", output)

if __name__ == '__main__':
    unittest.main()

