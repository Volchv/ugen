import argparse
import os


def generate_usernames(fname, mname, lname):

    """ Generate username based on input file.
        It takes first symbol from fname and middle name and whole lastname and concatenate it.
        Username is returned in lowercase.
        fname = first name
        mname = middle name , which is optional!, if nonexistent it is replaced by ''
        lname = last name"""

    username = fname[0] + (mname[0] if mname else '') + lname
    return username.lower()


def process_files(input_file, output_file):

    """ Processes an input file and writes output to an output file .
        Output file is opened in write mode in calling of this function and passed as output_file argument.
        Strip for removing leading/trailing spaces and split to divide into needed data-columns"""

    with open(input_file, 'r', encoding='utf-8') as my_file:
        line_number = 0  # cycle counter to identify on which line is error.
        for line in my_file:    # cycling through input file and creating data/columns
            line_number += 1
            columns = line.strip().split(':')
            if len(columns) == 5:   # Program is build for 5 column input. Other data is considered corrupted.
                uid, fname, mname, lname, dept = columns
            else:
                print(f"Error: Invalid line in file {my_file.name} on line:{line_number}. Continuing without this row.")

                continue  # Unknown data line, have columns != 5, can be corrupted,  it is skipped.
            username = generate_usernames(fname, mname, lname)  # Passing name data to generate_username function
            output_line = f"{uid}:{username}:{fname}:{mname}:{lname}:{dept}\n"

            output_file.write(output_line)  # writing data to output file


def main():
    # Parse arguments for input and output file and basic description.

    parser = argparse.ArgumentParser(description='Program to generate usernames from input files and '
                                                 'adding it to output file together with input data. ',
                                     usage='%(prog)s [options]')
    parser.add_argument('input_files', metavar='input_file', type=str, nargs='+',
                        help='One or more input files to process. Data must be in txt files, separated by colons (:) '
                             'and in utf-8 coding. ')
    parser.add_argument('-o', '--output', dest='output_file', type=str, default='output_file.txt',
                        help='The output file to write the generated data. Optional argument, if it is not added '
                             'then default name will be used to create output: output_file.txt ')
    args = parser.parse_args()

    # Check for each inserted file if it exists. If not , help will be printed and program exited.

    for file in args.input_files:
        if not os.path.isfile(file):
            print('\n Error: input file does not exist. Please check for naming errors or if files exists.\n ')
            parser.print_help()
            exit(1)

    # Open output file, either default or one parsed by user, call process_files function
    # which process and save generated data to output file

    with open(args.output_file, 'w', encoding='utf-8') as output_file:
        for save_data in args.input_files:
            process_files(save_data, output_file)
    print("File Successfully CREATED")


if __name__ == '__main__':
    main()
