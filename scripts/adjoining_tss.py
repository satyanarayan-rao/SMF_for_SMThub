import sys
from collections import defaultdict

tss_dict = defaultdict(list)

tss_file = open(sys.argv[1])

for line in tss_file:
    chrom, tf, tss = line.strip().split('\t')
    tss_dict[(chrom, tf)].append(tss)

promoter_bed_file = open(sys.argv[2])

for line in promoter_bed_file:
    chrom, st, en, tf = line.strip().split('\t')
    for tss in tss_dict[(chrom, tf)]:
        print(f"{chrom}\t{st}\t{en}\t{tf}\t{tss}") 
