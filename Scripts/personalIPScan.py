#!/usr/bin/python2
# cmdline is a function to run External Commands from Python Script
# finds personal IP Address, lists open ports, services, & host OS


from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

personalIPAddr = cmdline("ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk$
print cmdline("nmap -sV -T4 -F "+personalIPAddr)



