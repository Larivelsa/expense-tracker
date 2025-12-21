import json
from cli_parser import create_parser
'''
[  ] Use any programming language for any available module for parsing command arguments 
(e.g. python with the argparse, node.js with commander etc).

[  ] Use a simple text file to store the expenses data. You can use JSON, CSV, or any 
other format to store the data.

[  ] Add error handling to handle invalid inputs and edge cases (e.g. negative amounts, 
non-existent expense IDs, etc).

[  ] Use functions to modularize the code and make it easier to test and maintain.

'''

def main():
    create_parser()

if __name__ == '__main__':
    main()