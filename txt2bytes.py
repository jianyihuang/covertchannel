import sys

#first argument input, second output


f = open(sys.argv[1],"r")

contents = f.read()

intcontents = [];

bincontents = "";

for i in contents:
    intcontents.append(ord(i))

for i in intcontents:
    bincontents = bincontents + bin(i)[2:].zfill(8)

f.close()


f2= open(sys.argv[2],"w")

f2.write(bincontents)

f2.close()
