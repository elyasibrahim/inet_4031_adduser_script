#!/usr/bin/python3

import os
import re
import sys

def main():

    # ask user if they want dry-run mode
    tty = open("/dev/tty", "r")
    print("Run in dry-run mode? (Y/N): ", end="", flush=True)
    dry_run = tty.readline().strip().upper()

    for line in sys.stdin:

        # skip comment lines that start with #
        match = re.match("^#", line)

        # split each line into fields separated by colon
        fields = line.strip().split(':')

        # skip line if it is a comment OR does not have exactly 5 fields
        if match or len(fields) != 5:
            if dry_run == 'Y':
                print("Skipping invalid or comment line:", line.strip())
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # groups list split by comma
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run == 'Y':
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run == 'Y':
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run == 'Y':
                    print("DRY RUN:", cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
