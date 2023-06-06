#!/bin/bash
# Name: Asadbek
# Course: Operating_System

echo "Displaying the last 100 lines of the system log:"
tail -n 100 /var/log/syslog

echo "Storing the last 100 lines of the system log in a file called 'log_output.txt':"
tail -n 100 /var/log/syslog > log_output.txt

