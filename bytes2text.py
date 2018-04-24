import sys

#convert back to original

f = open(sys.argv[1],"r")

contents = f.read()

byteslist = []

string = ""

for i in range(0,len(contents),8):
    byteslist.append(contents[i:i+8])

for i in byteslist:
    string = string + str(chr(int(i,2)))

f.close()


f2= open(sys.argv[2],"w")

f2.write(string)

f2.close()
