csv = []
with open("files/sampledata.csv", "r") as csv_file:
    for line in csv_file:
        if "Name" in line:
            continue
        data = line.split(",")
        name = data[0]
        score2 = float(data[2])
        score3 = float(data[3])
        avgscore = (score2+score3)/2
        csv.append([name,avgscore])
        print (f"{name} scored {score2} and {score3}, averaging {int(avgscore)}")
with open("files/averages.csv", "w") as file:
    file.write("Name,Average\n")
    i=0
    for item in csv:
        filebuffer = str(item[0])+","
        filebuffer = filebuffer+str(averages[i])+"\n"
        print(str(averages[i]))
        i = i + 1
        file.write(filebuffer)
        filebuffer = ""