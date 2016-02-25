import socket
import subprocess
import sys
from datetime import datetime
from sys import exit

def title():
    print ("")
    print ("-=-=-Open Port Scanner-=-=-")
    print ("-=-=-By Scorpio-=-=-")
    print ("")



    title()

Target = raw_input("Enter a target to start > ")
TargetIP = socket.gethostbyname(Target)




print "=" * 65
print "Please wait, scanning remote host", TargetIP, "This Can Be A While"
print "=" * 65

ogtime = datetime.now()


try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((TargetIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

posttime = datetime.now()

total =  posttime - ogtime

print 'Scan Finished in: ', total

raw_input("Press Any Button To Exit...")