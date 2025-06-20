import sys

search_tfs = sys.argv[1]
found_tfs = sys.argv[2]

file1 = open(search_tfs)
tfs = []

for line in file1:
    line = line.strip().split("\t")
    k = line[0]
    tfs.append(k)
    #print(tfs)

file1.close()

file2 = open(found_tfs)

found = []
for line in file2:
    l1 = line.strip().split("\t")
    l2 = l1[0]
    if l2 in tfs:
        print(l1[0],l1[1],l1[2],l1[3], sep = "\t")
