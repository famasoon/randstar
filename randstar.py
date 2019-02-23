import urllib.request
import json
from random import choice
from sys import argv

if len(argv) != 2:
    print("Usage: python3 randstar.py <UserName>")
    exit(0)

user_name = argv[1]
url = "https://api.github.com/users/" + user_name + "/starred"

req = urllib.request.Request(url)
body = ""

try:
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
except Exception as e:
    print("ERROR: {}".format(e))
    exit(1)

json_obj = json.loads(body)
try:
    html_url = choice(json_obj)['html_url']
except IndexError:
    print("That user has not starred")
    exit(1)

print(html_url)