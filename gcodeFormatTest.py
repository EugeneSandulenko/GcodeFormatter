import unittest
import os


class TestGcodeFormatter(unittest.TestCase):
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

    def run_gcode_formatter(self):
        os.system('gcodeFormat.py ' + self.test_file_name)

    def test_gcodeFormatter_creates_new_file(self):
        file_content = ["File with gcode\n", "Second line\n", "Third line"]
        self.create_test_file(file_content)

        self.run_gcode_formatter()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, file_content)

    def test_gcodeFormatter_adds_message_for_each_layer(self):
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
            "M117 3-0\n",
            ";LAYER:1\n",
            "M117 5-1\n",
            ";LAYER:238\n",
            "M117 7-238\n",
            "some code\n",
            "Third line"]

        self.create_test_file(file_content)

        self.run_gcode_formatter()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, expected_content)

    def test_gcodeFormatter_adds_message_for_each_layer_with_total_layers_number(self):
        file_content = [
            "File with gcode\n",
            ";Layer count: 356\n",
            ";LAYER:0\n",
            ";LAYER:1\n",
            ";LAYER:238\n",
            "some code\n",
            "Third line"]

        expected_content1 = [
            "File with gcode\n",
            ";Layer count: 356\n",
            ";LAYER:0\n",
            "M117 4-0 of 356\n",
            ";LAYER:1\n",
            "M117 6-1 of 356\n",
            ";LAYER:238\n",
            "M117 8-238 of 356\n",
            "some code\n",
            "Third line"]

        self.create_test_file(file_content)

        self.run_gcode_formatter()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, expected_content1)

    def test_gcodeFormatter_adds_message_with_type(self):
        file_content = [
            "File with gcode\n",
            ";Layer count: 356\n",
            ";LAYER:0\n",
            ";TYPE:SKIN\n"
            ";TYPE:INNER\n"
            ";LAYER:1\n",
            ";LAYER:238\n",
            "some code\n",
            "Third line"]

        expected_content = [
            "File with gcode\n",
            ";Layer count: 356\n",
            ";LAYER:0\n",
            "M117 4-0 of 356\n",
            ";TYPE:SKIN\n",
            "M117 6-0 of 356 SKIN\n",
            ";TYPE:INNER\n",
            "M117 8-0 of 356 INNER\n",
            ";LAYER:1\n",
            "M117 10-1 of 356\n",
            ";LAYER:238\n",
            "M117 12-238 of 356\n",
            "some code\n",
            "Third line"]

        self.create_test_file(file_content)

        self.run_gcode_formatter()

        with open(self.new_file_name, 'r') as new_file:
            new_file_content = new_file.readlines()

        self.assertEqual(new_file_content, expected_content)
