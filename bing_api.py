#!/usr/bin/env python

import requests
import simplejson as json

r = requests.get("http://dev.virtualearth.net/REST/V1/Routes/Transit?wp.0=Golden%20Gate%20Bridge&wp.1=Fishermans%20Wharf&timeType=Departure&dateTime=3:00:00PM&output=json&key=AupvjJj-8-1RYDPSIIxnP8IQfomRdF8CJAyhe4KrWMBNS7pdOkUDRBU2OtlBoPu8")

raw = json.loads(r.text)

rjson = raw['resourceSets']

print json.dumps(rjson, sort_keys=True, indent=2)

#for item in rjson:
#    print item
