
tbp = open("list.csv", "r")
iit = open("school.csv", "r")
out = open("out.csv", "w")

member = []

ls1 = tbp.readlines()
for line in ls1:
    words = line.split(",")
    if " " in words[0]:
        words[0] = words[0].split(" ")[0]
    key = (words[0], words[1])
    member.append(key)

ls2 = iit.readlines()


major_dict = {"BME": "Biomedical engg",
              "CPE": "Computer engg",
              "EE": "Electrical engg",
              "ARCE": "Architectural engg",
              "CE": "Civil engg",
              "AE": "Aerospace engg",
              "ME": "Mechanical engg",
              "CHE": "Chemical engg",
              "MSE": "Materials science and engg"}

words = []
for line in ls2:
    if line == " " or line == "\n":
        continue
    words = line.split(",")
    words[5].replace("\n", "")
    words[5].replace(" ", "")

    if words[5] in major_dict:
        major = major_dict[words[5]]
        fn = words[1]
        ln = words[0]
        sj = words[2]
        if sj == "Junior":
            year = "2013"
        else:
            year = "2012"
        month = "May"
        mem = ""
        for item in member:
            if fn in item and ln in item:
                mem = "M"
        out.write("{0},{1},{2},{3},{4},{5},{6}\n".\
                    format(fn,ln,sj,month,year,major,mem) )
    else:
        print "ERROR! ", line
tbp.close()
iit.close()
out.close()
