# oracle_interview_exercise

This Repository includes two files to test a script that finds and counts ERRORS in a log file.
The script is written in Python and uses the `argparse` library to handle command-line arguments. 
It reads a log file, counts the occurrences of the word "ERROR", and prints the count to the console.


Error log created with chat GPT using the next command: "Can you create a log that includes 7 "ERROR:" lines so I can use it for testing"


In order to run the script, you need to have Python installed on your machine.
You can run the script from the command line by providing the path to the log file as an argument.
# Usage
Example of how to run the script:
python3 .\log_error_finder.py log.txt

Libraries used:
re for regular expressions
argparse for command-line argument parsing
