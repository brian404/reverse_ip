from insides import *
from sys import argv
import requests
import json
import optparse
import os
import re

################################  Banner   ################################

banner = """
  __                      __  
 /__)_    _ _  _ _  __  //__) 
/ ( (- \/(-/ _) (-     (/     
                              
                      brian :)
"""

print(banner)

################################ Functions ################################

def reverseViaHT(website):
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="

    combo = "{url}{website}".format(url=url, website=webs)

    request = requests.get(combo, headers=functions._headers, timeout=5).text
    if len(request) != 5:
        _list = request.strip("").split("\n")
        for _links in _list:
            if len(_links) != 0:
                write(var=" ", color=g, data=_links)
    else:
        write(var="@",
              color=r,
              data="Sorry, the webserver of the website you entered has no domains other than the one you gave :')")

def heading(heading, website, color, afterWebHead):
    space = " " * 15
    var = str(space + heading + " '" + website + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1
    print("\n" + str("{white}" + "-" * length + "-").format(white=w))
    print(str("{color}" + var).format(color=color))
    print(str("{white}" + "-" * length + "-").format(white=w) + "\n")

################################ Args ################################

_usage = "python " + argv[0] + " --all hackthissite.org"
_version = "[" + c + "~" + w + "] " + g + "Version: " + c + "2.0"
parser = optparse.OptionParser(usage=_usage, version=_version, conflict_handler="resolve")
general = optparse.OptionGroup(parser, y + 'Basic Help')
general.add_option('-h', '--help', action='help', dest='help', help='Shows the help for the program.')
general.add_option('-v', '--version', action='version', help='Shows the version of the program.')

reverse_ip = optparse.OptionGroup(parser, g + "Reverse IP")
reverse_ip.add_option("-r", "--revht",  action='store_true', dest='hackertarget', help="For Doing Reverse IP Via Hacker Target's API")

grouped_scanning = optparse.OptionGroup(parser, c + "Grouped Results")
grouped_scanning.add_option("-a", "--all",  action='store_true', dest='all', help="All Things at Once!")

parser.add_option_group(general)
parser.add_option_group(reverse_ip)
parser.add_option_group(grouped_scanning)

(options, args) = parser.parse_args()
try:
    website = addHTTP(args[0])
except:
    pass

try:
    if options.hackertarget:
        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via HT <3", color=c)
        reverseViaHT(website)

    elif options.all:
        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via HT <3", color=c)
        reverseViaHT(website)

    else:
        write(var="~", color=c, data="Usage: python " + argv[0] + " --all hackthissite.org")

except KeyboardInterrupt:
    write(var="~", color=y, data="Error: User Interrupted!")

except Exception as e:
    write(var="#", color=r, data="Error: Kindly report the error below to brian :) (If your internet is working ;)\n\"\"\"\n" + str(e) + "\n\"\"\"")

print(Footer)

# ~ See Ya :)
# ~ brian4044 :) 
