#!/usr/bin/env python

f = open("color.html", "r")
new_lines = ["<pre style='line-height: 58%'>"]
for line in f.readlines():
    case = line[0]
    if case == "d":
        new_line = "<span><b>{0}</b></span>".format(line)
    elif case == "i":
        new_line = "<span>{0}</span>".format(line)
    elif case == "-":
        if line[1] == "-":
            new_line = "<span style='color: #ED5158'><b>{0}</b></span>".format(line)
        else:
            new_line = "<span style='color: red'><b>{0}</b></span>".format(line)
    elif case == "+":
        if line[1] == "+":
            new_line = "<span style='color: #5fbf00'><b>{0}</b></span>".format(line)
        else:
            new_line = "<span style='color: green'><b>{0}</b></span>".format(line)
    elif case == "@" or case == " ":
        new_line = "<span>{0}</span>".format(line)

    new_lines.append(new_line)
new_lines.append("</pre>")

print "\n".join(new_lines)
    
