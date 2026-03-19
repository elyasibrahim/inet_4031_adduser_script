#!/usr/bin/python3

# INET4031
# Your Name
# Data Created
# Date Last Modified

#importing os so the script can run Linux system commands like adduser and passwd
import os
#importing re so the script can use regular expressions to check for special characters in each line
import re
#importing sys so the script can read input lines that are redirected into the program
import sys

def main():
    for line in sys.stdin:
	#this checks if the line starts with the "#" character which means it is a comment or should be skipped
        match = re.match("^#",line)
	#this removes whitespace/newlines and splits the line into fields separated by colons
        fields = line.strip().split(':')

	#this condition skips processing if the line is a comment or does not contain the correct number of fields (5 expected)
        if match or len(fields) != 5:
            continue
	#these lines assign the username, password, and formatted user info that will be stored in the system passwd file
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

	#splits the group list into individual groups using commas so the script can loop through them
        groups = fields[4].split(',')

	#prints a status message showing that the script is about to create the user account
        print("==> Creating account for %s..." % (username))
	#builds the Linux adduser command string that would be executed to create the account
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        print(cmd)
        os.system(cmd)

	#prints a message showing the script is about to set the password for the new user
        print("==> Setting the password for %s..." % (username))
	#builds a command that pipes the password into the passwd command to automatically set the user's password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        os.system(cmd)

        for group in groups:
	# this checks if the group value is not "-" which means the user should be added to an actual group if it is not "-", the script prints a message and prepares a command to add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
