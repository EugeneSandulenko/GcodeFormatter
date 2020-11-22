import unittest
import os


class TestGcodeFormater(unittest.TestCase):
    test_file_name = 'testFile.txt'
    new_file_name = 'testFile_m.txt'

    def tearDown(self):
        if os.path.exists(self.new_file_name):
            os.remove(self.new_file_name)
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def create_test_file(self, content):
        with  open(self.test_file_name, 'w') as source_file:
            source_file.writelines(content)

    def run_gcode_formater(self):
        os.system('gcodeFormat.py ' + self.test_file_name)

    def test_gcodeFormater_creates_new_file(self):
        file_content = ["File with gcode\n", "Second line\n", "Third line"]
        self.create_test_file(file_content)

        self.run_gcode_formater()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, file_content)

    def test_gcodeFormater_adds_message_for_each_layer(self):
        file_content = [
            "File with gcode\n",
            ";LAYER:0\n",
            ";LAYER:1\n",
            ";LAYER:238\n",
            "some code\n",
            "Third line"]

        expected_content = [
            "File with gcode\n",
            ";LAYER:0\n",
            "M117 LAYER:0\n",
            ";LAYER:1\n",
            "M117 LAYER:1\n",
            ";LAYER:238\n",
            "M117 LAYER:238\n",
            "some code\n",
            "Third line"]

        self.create_test_file(file_content)

        self.run_gcode_formater()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, expected_content)
