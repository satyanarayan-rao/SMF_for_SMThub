import sys
from collections import defaultdict

#chr1    3009102 3009368 SRR10055871.15607800_15607800/1_overlapping`99~147|.3F156.108   1       .       .2H.8h.4h.5h.14x.28h.54x.2x.2h.31H.86H.20
#chr1    3009102 3009368 SRR10055871.15608130_15608130/1_overlapping`99~147|.3F156.108   1       .       .2H.8h.4h.5h.14x.28h.54x.2x.2h.31H.86H.20
#chr1    3009102 3009368 SRR10055871.21050349_21050349/1_overlapping`99~147|.3F156.108   1       .       .2H.8h.4h.5h.14x.28h.54x.2x.2h.31H.86H.20
#chr1    3009102 3009368 SRR10055871.22033808_22033808/1_overlapping`99~147|.3F156.108   1       .       .2H.8h.4h.5h.14x.28h.54x.2x.2h.31H.86H.20
 

pcr_duplicate_dict = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:0))))

for line in sys.stdin:
    line = line.strip().split('\t')
    l1 = line.split('.')
    l2 = line.spli('|')
    
    sample_id = l1[3]
    comp_fp = l2[4]
    exp_fp = line[-1]

    pcr_duplicate_dict[sample_id][comp_fp][exp_fp]
