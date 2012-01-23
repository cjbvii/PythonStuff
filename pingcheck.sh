#!/bin/bash

### test whether we've already written out a status file. If we have, copy it to another file so we can compare it to the current server status. If not, create an empty one.
 
if [ -f server_status.txt ]; then
cp server_status.txt last_server_status.txt
else
 touch server_status.txt
fi
cp server_status.txt last_server_status.txt

### icmp ping the server in question, supplied as an argument to the script; send results of command to /dev/null since we only care about exit status here

ping -o $1 > /dev/null 2>&1

### write the ping command's exit status to server_status.txt; anything other than zero means the server is not reachable

echo $? > server_status.txt

### check to see if the results of the ping command have changed since the last time the script was run. If so, then check the most recent status and send the appropriate e-mail depeding on results of the ping above

if [ `cat server_status.txt` != `cat last_server_status.txt` ] ; then
  if [ `cat server_status.txt` != "0" ] ; then
     echo "$1 is not returning pings" |mailx -s "$1 DOWN" "charlesburns@gmail.com"
else
     echo "$1 is returning pings" |mailx -s "$1 UP" "charlesburns@gmail.com"
fi
else
exit 0
fi



