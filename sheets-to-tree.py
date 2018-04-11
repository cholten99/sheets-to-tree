#!/usr/bin/python

# https://goo.gl/pjW4ig -- spreadsheet
# sheets-to-tree@plenary-hangout-93402.iam.gserviceaccount.com

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Recursive function to build the JSON for the tree using data from the google sheet array
def buildJson(data_line, headings, data_list, json_string):
    json_string += "{ "

    pos = 1;
    for heading in headings:
        if heading != "parent":
          json_string += '"' + heading + '": "' + data_line[pos] + '", '
          pos += 1
    json_string = json_string[:-2]

    has_kids = False
    for entry in data_list:
        if entry[0] == data_line[1]:
            if not has_kids:
                json_string += ', "children": ['
                has_kids = True
            json_string = buildJson(entry, headings, data_list, json_string)
            json_string += ","

    if has_kids:
        json_string = json_string[:-1]
        json_string += " ]"
    json_string += " }"

    return json_string

# MAIN

# Connect to the google sheet and get the worksheet handle
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets-to-tree-credentials.json', scope)
drive_handle = gspread.authorize(credentials)
worksheet = drive_handle.open("Tree data test").sheet1

# Get the headings and the data
data_list = worksheet.get_all_values()
headings = data_list[0]
del data_list[0]

# Build the JSON for the tree
json_string = ""
json_string = buildJson(data_list[0], headings, data_list, json_string)

# Output

# Http headers when outputting to a tab rather than to javascript
# Yes, you need the empty print statement or it won't work...
# print "Content-Type: text/html"
# print ""

# Http headers when outputting JSON
# Yes, you need the empty print statement or it won't work...
print "Content-Type: text/json"
print ""
print json_string

