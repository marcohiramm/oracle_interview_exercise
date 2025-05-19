import re
import argparse



def count_errors(file):
    try:
        log_file =  open(file.filename, "r")
        content = log_file.read()

    except FileNotFoundError as e:
        print(f"Error: The file 'log.txt' was not found.")

    
    
    error_line_counter = 0 

    error_lines = re.findall(r'^.*ERROR:.*$', content, re.MULTILINE)



    for line in error_lines:
        error_line_counter += 1
        print(line)

    return error_line_counter




    



def main():

    # Create parser object
    parser = argparse.ArgumentParser(description="Process a log file.")

    # Define arguments
    parser.add_argument("filename",default="log.txt", help="Path to the log file")

    # Parse arguments
    args = parser.parse_args()

    errors_in_line = count_errors(args)
    print("Amount of errors in Log: ", errors_in_line)



            
if __name__ == "__main__":

    main()

