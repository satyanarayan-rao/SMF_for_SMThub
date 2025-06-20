import sys

tf_with_gpc = sys.argv[1]
meme_file = sys.argv[2]

with open(tf_with_gpc) as file1:
    tfs = []
    for line in file1:
        l1 = line.strip()
        tfs.append(l1)

with open(meme_file) as file2:
    for line in file2:
        line = line.strip().split()
        if not line:
            continue 
        k = line[0]
        if k in tfs:
            print(f"{line[0]}\t{line[1]}")
