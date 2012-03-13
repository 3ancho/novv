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

    request_url = "http://dev.virtualearth.net/REST/V1/Routes/{method}?wp.0={start}&wp.1={end}&timeType=Departure&routePathOutput=Points&dateTime=3:00:00PM&optmz=distance&maxSolns=3&output=json&key=AupvjJj-8-1RYDPSIIxnP8IQfomRdF8CJAyhe4KrWMBNS7pdOkUDRBU2OtlBoPu8".format(method=METHODS[method], start=start, end=end)

    google_url= "" 

    print request_url
    r = requests.get(request_url)
    
    raw = json.loads(r.text)
    
    f = open('rjson.json', 'w')
    f.write(json.dumps(raw, sort_keys=True, indent=2))
    f.close()
    routes = raw['resourceSets'][0]['resources']
    #routes = rjson[0]['resources']
    for route in routes:
        print route["id"] 
        legs = route['routeLegs'][0]['itineraryItems']
        parts = []
        for leg in legs:
            part = []
            if leg['transitTerminus']:
                info = "Terminus is " + str(leg['transitTerminus'])
            else:
                info = ""

            part = leg['instruction']['text'], leg['travelDistance'], info, leg['iconType'] 
            parts.append(part)

        for part in parts:
            print part[0]
            print "Distance: ", part[1]
        print "----------\n" 

    if options.print_flag:
        prettify(legs)

def prettify(rjson):
    print json.dumps(rjson, sort_keys=True, indent=2)

if __name__ == '__main__':
    main()


