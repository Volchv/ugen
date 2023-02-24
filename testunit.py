import unittest
import tempfile
import os
import ugen
import HtmlTestRunner


class TestUgen(unittest.TestCase):  # Class for testing functions "process_files" and "generate_usernames" from ugen.py

    def setUp(self):    # creating temporary directory with SetUp
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self):     # cleaning temporary directory on tearDown
        self.tempdir.cleanup()

    def test_process_files(self):   # Test of process_files function
        # creating temporary input /output files so test wont create normal files
        input_file = os.path.join(self.tempdir.name, 'input.txt')
        output_file = os.path.join(self.tempdir.name, 'output.txt')

        with open(input_file, 'w') as test_file:    # Creating inside of input file
            test_file.write('1234:Jozef:Miloslav:Hurban:Legal\n')
            test_file.write('4567:Milan:Rastislav:Stefanik:Defence\n')
            test_file.write('4563:Jozef::Murgas:Development\n')

        with open(output_file, 'w+') as test_file:  # w+ mode , first we write through process_files than read
            ugen.process_files(input_file, test_file)
            test_file.seek(0)   # Important, after writing we need to start from beginning of file or it will be empty
            result = test_file.read()

        # Creating control answer
        expected = '1234:jmhurban:Jozef:Miloslav:Hurban:Legal\n'\
                   '4567:mrstefanik:Milan:Rastislav:Stefanik:Defence\n' \
                   '4563:jmurgas:Jozef::Murgas:Development\n'

        self.assertEqual(result, expected)  # Actual test, comparing result and expected

    def test_generate_usernames(self):  # Test of generate_usernames function
        # Test case for generating username with middle name
        self.assertEqual(ugen.generate_usernames("John", "Robert", "Doe"), "jrdoe")

        # Test case for generating username without middle name
        self.assertEqual(ugen.generate_usernames("Benjamin", "", "Franklin"), "bfranklin")


if __name__ == '__main__':  # runing "python testunit.py" will create hmtl report. import of HtmlTestRunner needed.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report'))