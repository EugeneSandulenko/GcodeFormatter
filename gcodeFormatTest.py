import unittest
import os


class TestGcodeFormater(unittest.TestCase):
    testFileName = 'testFile.txt'
    newFileName = 'testFile_m.txt'

    def tearDown(self):
        if os.path.exists(self.newFileName):
            os.remove(self.newFileName)
        if os.path.exists(self.testFileName):
            os.remove(self.testFileName)

    def create_test_file(self, content):
        sourceFile = open(self.testFileName, 'w')
        sourceFile.writelines(content)
        sourceFile.close()

    def run_gcode_formater(self):
        os.system('gcodeFormat.py ' + self.testFileName)

    def test_gcodeFormater_cretes_new_file(self):
        fileContent = ["File with gcode\n", "Second line\n", "Third line"]
        self.create_test_file(fileContent)

        self.run_gcode_formater()

        newFile = open(self.newFileName, 'r')
        newFileContent = newFile.readlines()
        newFile.close()

        self.assertEqual(newFileContent, fileContent)
