import sys
from collections import defaultdict

#>chr2L
#Cgacaatgcacgacagaggaagcagaacagatatttagattgcctctcat
#tttctctcccatattatagggagaaatatgatcgcgtatgcgagagtagt

fasta_file = open(sys.argv[1])

gc_loc_dict = defaultdict(list)

for line in fasta_file:
    if line.startswith(">"):
        l1 = line.strip().split()
        chrom = l1[0][1:]

        counter = 0
        seq = ""

    else:
        line = line.strip()
        seq += line

        for i in range(len(seq) - 1):
            if seq[i:i+2] in ["GC", "gc", "gC", "Gc"]:

                if line[i:i+2] in ["GC", "gc", "gC", "Gc"]:
                    gc_loc_dict[chrom].append(counter + i + 1)
                else:
                    gc_loc_dict[chrom].append(counter + i )
        counter += len(line)
        seq = seq[-1]
for chrom in gc_loc_dict:
    for loc in gc_loc_dict[chrom]:
        print(f"{chrom}\t{loc}")
