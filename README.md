# INET4031 Add Users Script

## Program Description
This program is a Python automation script that helps a system administrator create multiple Linux user accounts and assign them to groups quickly. Normally, adding users on Linux requires manually running commands like **adduser**, **passwd**, and **usermod** , or **adduser username group**. This can take a long time and increases the chance of mistakes when many users need to be created.

This script automates that process by reading user information from an input file and running the same system commands automatically. This makes user account setup faster, more consistent, and easier to manage on multiple servers.

## Program User Operation
The script reads a list of users from an input file and processes each line one at a time. Each valid line results in a new Linux account being created, a password being set, and optional group assignments being made.

To run the script, the user must first make sure the Python file is executable:


chmod a+x create-users.py


Then the script can be executed using input redirection:


./create-users.py < create-users.input


This sends the contents of the input file into the script for processing.

## Input File Format
Each line in the input file is colon-delimited and follows this structure:


username:password:lastname:firstname:groups


Field descriptions:

- **username** → the Linux login name to be created  
- **password** → the password that will be set for the account  
- **lastname** → user's last name (used in account description)  
- **firstname** → user's first name (used in account description)  
- **groups** → comma-separated list of groups to assign the user to  

If a user should **not be added to any groups**, a dash `-` is used.

If a line should be **skipped entirely**, it can be commented out by placing a `#` at the beginning of the line.

## Command Execution
The script internally runs Linux administrative commands such as:

- **/usr/sbin/adduser**
- **/usr/bin/passwd**
- **/usr/sbin/adduser username group**

These commands are executed through Python using system calls. This allows the script to perform the same actions that a system administrator would normally type manually in the terminal.

## Dry Run Mode
During testing, the script can be run in a “dry run” configuration where the system commands are commented out. In this mode, the script will display the actions it would perform without actually creating users or modifying the system.

This helps verify that the input file is formatted correctly and prevents accidental incorrect user creation before running the script for real.
