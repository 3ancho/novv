#!/usr/bin/env python
# md to html for kindle 6'' device 
# Width 47 chars when p = 10px;

import optparse
import sys

try:
    import envoy
except ImportError:
    envoy = None

try:
    import markdown
except ImportError:
    markdown = None

def main():
    usage = "usage: %prog [options] args"
    op = optparse.OptionParser(usage)
    op.add_option('--full-name', '-f', dest="fullname", help="the full name of the site")
    op.add_option('--short-name', '-s', dest="shortname", help="SHORTNAME.prometdev.com")
    op.add_option('--drupal', '-D', dest="drupal_version", help="if to install drupal, option = 6 or 7")

def run_cmd(command):
    " A wrapper to envoy run "

    print "Executing Shell Command: \n", command
    r = envoy.run(command)
    if r.status_code == 1:
        print "!Err: ",r.std_err
        sys.exit(1)
    print r.std_out,
    print "Executing Done!\n"

def check_sitename():
    pass

template = """
<html>
<head><style type="text/css"> 
p, a, code, li {font-size: 10px;}
h1 {font-size:15px;}
h2 {font-size:12px;}
</style></head>
<body>
BODY_CONTENT
</body>
</html>"""

if __name__ == '__main__':
    main()

