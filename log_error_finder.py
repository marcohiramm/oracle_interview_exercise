import os 
import re
import argparse



def count_errors(file):
    try:
        log_file =  open(file.filename, "r")

    except FileNotFoundError as e:
        print(f"Error: The file 'log.txt' was not found.")

    
    content = log_file.read()

    



def main():

    # Create parser object
    parser = argparse.ArgumentParser(description="Process a log file.")

    # Define arguments
    parser.add_argument("filename",default="log.txt", help="Path to the log file")

    # Parse arguments
    args = parser.parse_args()

    count_errors(args)



            
if __name__ == "__main__":

    main()

