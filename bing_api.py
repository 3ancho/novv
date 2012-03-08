#!/usr/bin/env python

import sys
import optparse
import requests
import simplejson as json

def main():
    """Main"""
    usage = "usage: %prog [options] args" 
    op = optparse.OptionParser(usage)

    op.add_option('--to', '-t', dest="end",\
                   help="To")
    op.add_option('--from', '-f', dest="start",\
                   help="From")        
    op.add_option('--method', '-m', dest="method", default=0,\
                   help="From")        
    op.add_option('--print', '-p', action="store_true", default=False,\
                                 dest="print_flag", help="if you want to print")

    (options, args) = op.parse_args()

    TRANSIT = 0
    DRIVE = 1
    WALK = 2
    
    METHODS = ['Transit', 'Driving', 'Walking']
    method = int(options.method)

    if not options.start or not options.end:
        op.print_help()
        sys.exit(1)

    start = options.start.replace(" ", "%20")
    end = options.end.replace(" ", "%20")
    
    print start
    print end

    request_url = "http://dev.virtualearth.net/REST/V1/Routes/{method}?wp.0={start}&wp.1={end}&timeType=Departure&dateTime=3:00:00PM&output=json&key=AupvjJj-8-1RYDPSIIxnP8IQfomRdF8CJAyhe4KrWMBNS7pdOkUDRBU2OtlBoPu8".format(method=METHODS[method], start=start, end=end)

    print request_url
    r = requests.get(request_url)
    
    raw = json.loads(r.text)
    
    rjson = raw['resourceSets']
    f = open('rjson.json', 'w')   
    f.write(json.dumps(rjson, sort_keys=True, indent=2))
    f.close()
    b = rjson[0]
    legs = rjson[0]['resources'][0]['routeLegs'][0]['itineraryItems']

    part = []
    parts = []
    for leg in legs:
        part = leg['instruction']['text'], leg['travelDistance']
        parts.append(part)

    for part in parts:
        print "Info: ", part[0]
        print "Distance: ", part[1]

    if options.print_flag:
        prettify(legs)

def prettify(rjson):
    print json.dumps(rjson, sort_keys=True, indent=2)

if __name__ == '__main__':
    main()


