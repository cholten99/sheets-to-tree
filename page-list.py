#!/usr/bin/python

import cgi

arguments = cgi.FieldStorage()
action = arguments["action"].value

# Logging
log_file = open("logfile.txt", "w")  
log_file.write("Start\n")
log_file.write(action + "\n")

# Http headers when outputting JSON
# Yes, you need the empty print statement or it won't work...
print "Content-Type: text/json"
print ""

log_file.write(action + "\n")

if action is "read":
    with open("list-pages.json", "r") as pages_file:
        content = pages_file.read()
        print content
else:
    with open("list-pages.json", "w") as pages_file:
        pages_file.write(arguments["json"].value)

    # Need to return something to trigger the jQuert POST .done method
    print "NOP"

