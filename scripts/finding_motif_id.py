import sys

tf_with_gpc = sys.argv[1]
meme_file = sys.argv[2]

file1 = open(tf_with_gpc)
tfs = []

for line in file1:
    l1 = line.strip()
    tfs.append(l1)
    print(tfs)

file1.close()

file2 = open(meme_file)

#Arnt    MA0004.1
#Tbxt    MA0009.1
#Pax5    MA0014.1

for line in file2:
    line  = line.strip().split()
    k = line[0]
    if k in tfs:
        print(line)

file2.close() 
