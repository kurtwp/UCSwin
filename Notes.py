
def acreadMe ():
    #Clear()
    note = '''
Program provides configuration files for Adtran 1570 only
and defaults to 24 ports.
--------------
Enter Hostname:
Must be in the following format:
Eight letters followed by two digits, then W
For example:  ASDFGHJK02W
-------------
Enter IP: 
If you replacing the first switch enter 10.12.0.5.
If not the First Switch, enter in the appropriate IP address. 
--------------
Port 23 :
YES - Will configure port 23 as a Downlink to Another switch
NO - Will configure port 23 as a VoIP Phone port. 
---------------
Connected to VGW:
If YES, script will provide a configuration for a switch
directly connected to the VGW. If NO, script will configure
the switch(s) as connected to another swtich. 

'''
    return note

def creadMe ():
    #Clear()
    note = '''
Cisco Switch note will go here.

'''
    return note

def adreadMe ():
    #Clear()
    note = '''
Adtran Switch note will go here.

'''
    return note
