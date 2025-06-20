import sys


#chr4	55456109	55456388
#chr4	55494009	55494308
#chr4	55543269	55543468

for line in sys.stdin:
    l1 = line.strip().split("\t")
    #print (l1)
    start = int(l1[1])
    end = int(l1[2])
    N = end-start
    r = N%30
    a=0
    if r==0:
        for i in range(start,end,30):
            a+=1
            print (f"{l1[0]}\t{i}\t{i+30}\t{l1[3]}@window{a}")

    else:
       q = r%2
       p = int (r/2)
       if q==0:
           start = int(l1[1]) + p
           end = int(l1[2]) - p
           for i in range(start,end,30):
            a+=1
            print (f"{l1[0]}\t{i}\t{i+30}\t{l1[4]}@window{a}")

       elif q!=0:
           start = int(l1[1])+ p + 1
           end = int(l1[2]) - p
           for i in range(start,end,30):
                a+=1
                print (f"{l1[0]}\t{i}\t{i+30}\t{l1[4]}@window{a}")

