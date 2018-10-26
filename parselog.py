import datetime
import time
bestandprefix = "2005"
filepath = '2005.log'
with open(filepath) as fp:
   line = fp.readline()
   teller160 = 1
   teller80 = 1
   teller40 = 1
   teller20 = 1
   teller15 = 1
   teller10 = 1
   while line:
     line = fp.readline()
     if line.split(" ")[0] == "QSO:":
       try:
            datum = line.split(" ")[3]
            tijd = line.split(" ")[4]
       except:
            datum = ""
            tijd = ""
       try:
            freq = int(line.split(" ")[1])
       except:
            freq = 0


       tijdstr = tijd[:2] + ':' + tijd[-2:]
       datumtijdstr = datum + " " + tijdstr
       try:
           datumtijd = datetime.datetime.strptime(datumtijdstr, '%Y-%m-%d %H:%M')
       except:
           datumtijd = ""
       if freq <= 2000 and freq >=1800:
            fh = open(bestandprefix+"-160.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller160) + "\n")
            teller160 += 1
       if freq <= 3800 and freq >=3500:
            fh = open(bestandprefix+"-80.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller80) + "\n")
            teller80 += 1
       if freq <= 7200 and freq >=7000:
            fh = open(bestandprefix+"-40.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller40) + "\n")
            teller40 += 1
       if freq <= 14350  and freq >=14000:
            fh = open(bestandprefix+"-20.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller20) + "\n")
            teller20 += 1
       if freq <= 21450  and freq >=21000:
            fh = open(bestandprefix+"-15.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller15) + "\n")
            teller15 += 1
       if freq <= 30000  and freq >=28000:
            fh = open(bestandprefix+"-10.txt", "a")
            fh.write(str(int(time.mktime(datumtijd.timetuple())))+ "," + str(teller10) + "\n")
            teller10 += 1
