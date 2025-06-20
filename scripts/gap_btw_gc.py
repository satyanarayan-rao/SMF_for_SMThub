import sys
from collections import defaultdict

#chr1	10470
#chr1	10482
#chr1	10486
#chr1	10490
#chr1	10494

gc_file = open(sys.argv[1])
gc_pos_dict = defaultdict(list)

for line in gc_file:
    lines = line.strip().split("\t")
    chrom = lines[0]
    start = lines[1]
    st = int(start)
    gc_pos_dict[chrom].append(st)

for chrom in gc_pos_dict:
    gc_pos_list = gc_pos_dict[chrom]
    for i in range(len(gc_pos_list) - 2):
        st = gc_pos_list[i]
        mid = gc_pos_list[i + 1]
        end = gc_pos_list[i + 2]
        
        g1 = mid - st
        g2 = end - mid

        print(f"{chrom}\t{st}\t{end}\t{g1}\t{g2}")
