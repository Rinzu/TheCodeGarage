#Python Ping

import sh

print "Scanning..."
# ping range 8.8.8.7 - 8.8.8.9
for num in range(7,10):
    # declare ip address
    address = "8.8.8." + str(num)

    # check if host is alive using PING
    try:
        # bash equivalent: ping -c 1 > /dev/null
        sh.ping(address, "-c 1", _out="/dev/null")
        print "ping to", address, "OK"
    except sh.ErrorReturnCode_1:
        print "no response from", address
