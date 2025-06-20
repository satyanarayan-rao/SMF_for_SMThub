import sys

#creating windows of 30 bases in file downloaded from ReMap website.

#extracted_data = 'data_from_ReMap/numbered_max_peaks.bed'
#ext_peaks = open(extracted_data)


#chr2L	5086	6115	Ice1:Schneider-2	1	.	5690	5691	224,168,252
#chr2L	5088	6114	Sce:S2-DRSC	2	.	5818	5819	244,242,133
#chr2L	5103	6142	DnaJ-1:Schneider-2	1	.	5897	5898	62,241,1
for line in sys.stdin:
    l1 = line.strip().split("\t")
    #print (l1)
    start = int(l1[2])
    end = int(l1[3])
    N = end-start 
    r = N%30
    a=0        
    if r==0:
        for i in range(start,end,30):
            a+=1    
            print (f"{l1[0]}\t{l1[1]}\t{i}\t{i+30}\t{l1[4]}@window{a}\t{l1[5]}\t{l1[6]}\t{l1[7]}\t{l1[8]}\t{l1[9]}")
        
    else:
       q = r%2
       p = int (r/2)
       if q==0:
           start = int(l1[2]) + p 
           end = int(l1[3]) - p
           for i in range(start,end,30):
            a+=1
            print (f"{l1[0]}\t{l1[1]}\t{i}\t{i+30}\t{l1[4]}@window{a}\t{l1[5]}\t{l1[6]}\t{l1[7]}\t{l1[8]}\t{l1[9]}")

       elif q!=0:
           start = int(l1[2])+ p + 1 
           end = int(l1[3]) - p
           for i in range(start,end,30):
                a+=1
                print (f"{l1[0]}\t{l1[1]}\t{i}\t{i+30}\t{l1[4]}@window{a}\t{l1[5]}\t{l1[6]}\t{l1[7]}\t{l1[8]}\t{l1[9]}")
