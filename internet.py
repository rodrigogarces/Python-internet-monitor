from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from math import inf

def plotgraph():
    print("---- generate graph ----")
    print("opening input file")
    a = open("output.csv","r")
    lines = a.readlines()
    dt =[]
    ping = []

    start  = []
    finish = []

    print("processing csv file...")
    #ingore first line (cvs header) and process the file
    print ("lenght= " + str(len(lines)))
    for i in range(1, (len(lines))):
        #print (i)
        k_before = lines[i-1].split(",")
        k = lines[i].split(",")
        print(k)

        #if current registry is not the last from file
        if(i != len(lines) - 1):
            k_after = lines[i+1].split(",")
        else:
            #to prevent a bug if last registry is a bad ping
            #print("lasts")
            k_after = 1

        if float(k[1]) != 0:
            #print (k[1])
            dt.append(datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S:'))
            ping.append(float(k[1]))
            #print ("valid %i" %i + "    " + k[1].rstrip())
            #print (k[1])
        else:
            #print ("invalid %i" %i)
            if float(k[1]) != float(k_before[1]):
                start.append(datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S:'))
            print (i)
            #print(k_before)
            #print(k_after)
            if i != (len(lines)-1) and float(k_after[1]) != float(k[1]):
                finish.append(datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S:'))
    finish.append(datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S:'))


    #set y (ping) scale
    plt.plot(dt,ping, drawstyle='steps')
    plt.title("Results")
    plt.ylim([50,65])
    plt.xlabel("Datetime")
    plt.ylabel("Ping (ms)")

    #bad pings
    for i in range(len(start)):
        plt.axvspan(start[i],finish[i], color="red")
        #plt.axvspan(,, color="red")

    print("generating graph...")
    plt.show()

def generatecsv():
    print("---- generate csv file ----")
    #open input file
    print("opening input file")
    a = open("testeperda.log")

    #open output file
    print("opening output file")
    b = open("output.csv","w")
    lines = a.readlines()
    #print output file header (for display as csv)
    b.write("datetime,status\n")

    #extract usefull data from line
    print("reading initial datetime")
    temp = lines[1].split(" ")
    actual = datetime.strptime(str(temp[0])+","+str(temp[1]), '%Y-%m-%d,%H:%M:%S:')
    counter = 0

    #exclude header and footer
    print("processing file...")
    for i in range(1, (len(lines) - 3)):
        counter += 1
        k = lines[i].split(" ")
        prox = datetime.strptime(str(k[0])+","+str(k[1]), '%Y-%m-%d,%H:%M:%S:')

        #if is a "hole" between registers
        if (prox-actual).seconds > 1:
            for i in range(((prox-actual).seconds)-1):
                actual = actual + timedelta(seconds=1)
                b.write('%s:,0\n' % (str(actual)))

            #a little hack to display next registry after a "hole"
            actual = prox
            #split string "time=xxx" to display only numbers
            temp2 = k[-2].split("=")
            temp2 = temp2[1]
            b.write("%s:,%s\n" % (str(actual),temp2))

        #if network is unreachable
        elif(lines[i].find("unreachable") != -1):
            string  = ("%s %s,%i\n" % (str(k[0]),str(k[1]),0))
            b.write(string)

        #if network is reached
        else:
            #split string "time=xxx" to display only numbers
            temp2 = k[-2].split("=")
            temp2 = temp2[1]

            string  = ("%s %s,%s\n" % (str(k[0]),str(k[1]),temp2))
            b.write(string)

        actual = prox
    print("file sucessfully processed")

    print("closing input file")
    a.close()
    print("closing output file")
    b.close()

#generatecsv()#ok!
plotgraph()
