import sys,os,csv

with open("data.csv",newline="",encoding="utf8") as ofile:
    opencsvfile = csv.DictReader(ofile)
    clean = [i for i in ofile]
    print(clean)
with open("dataw.csv","w",newline="",encoding="utf8") as wfile:
    writefile = csv.DictWriter(wfile ,fieldnames="tototoyoyo.csv")
    writefile.writerow()
    