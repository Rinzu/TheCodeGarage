#!/usr/bin/python2

#cmdline is a function to run external commands from command line

from subprocess import PIPE, Popen

def cmdline(command):
        process = Popen(
                args=command,
                stdout=PIPE,
                shell=True
        )
        return process.communicate()[0]


#prints ip/mac addresses and to screen
print cmdline("arp-scan --interface=eth0 --localnet | grep QEMU")


