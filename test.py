import subprocess
import tempfile
import os

# Define test data file
test_data_file = "test_data.txt"

# Open test data file and read lines
with open(test_data_file, 'r') as file:
    test_cases = file.readlines()

# Creating temporary directory so test wont create real files
temp = tempfile.TemporaryDirectory()

# Iterate over test cases and run tests. i is count, test_case contain input , expected output and note about test line
for i, test_case in enumerate(test_cases):
    # Extract input, expected output and note from test case
    input_data, expected_output, note = test_case.strip().split("\t") # data in file are divided with TAB

    input_file = os.path.join(temp.name, 'input.txt')   # creation of temp input file
    with open(input_file, 'w') as test_file:
        test_file.write(input_data)     # writing extracted input data from test data file into input file

    output_file = os.path.join(temp.name, 'output.txt') # creation of temp output file

    # running ugen.py with with parameters containing our created temp input/output file and data from test_data file
    subprocess.run(["python3", "ugen.py", "--output", output_file, input_file])

    # saving output from output temp file
    with open(output_file, 'r') as file:
        output = file.read().strip()

    # Results based on similarity between output and expected output
    if output == expected_output:
        print(f"Test case {i+1}: PASSED\n NOTE: {note}\n")
    else:
        print(f"Test case {i+1}: FAILED\n NOTE: {note}")
        print(f"Input data: {input_data}")
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}\n")
