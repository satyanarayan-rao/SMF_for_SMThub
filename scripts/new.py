import sys

# >chrI
#CCACACCACACCCACACACCCACACACCACACCACACACCACACCACACC
#CACACACACACATCCTAACACTACCCTAACACAGCCCTAATCTAACCCTG
#GCCAACCTGTCTCTCAACTTACCCTCCATTACCCTGCCTCCACTCGTTAC


for line in sys.stdin:
    l1 = line.strip()
    if not l1.startswith(">"):
        l2 = l1.strip("\n")   
        print(l2)
