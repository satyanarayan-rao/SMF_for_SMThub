import sys

file1_path = sys.argv[1]  # hocomoco file
file2_path = sys.argv[2]  # jaspar file

# Read hocomoco data
hocomoco = {}
with open(file1_path) as f1:
    for line in f1:
        line = line.strip().split()
        if not line:
            continue
        tf = line[0]
        id_ = line[1]
        hocomoco[tf] = id_

# Read jaspar data
jaspar = {}
with open(file2_path) as f2:
    for line in f2:
        line = line.strip().split()
        if not line:
            continue
        tf = line[0]
        id_ = line[1]
        if tf in jaspar:
            jaspar[tf].append(id_)
        else:
            jaspar[tf] = [id_]

# Combine and print output
print("TF\tHOCOMOCO_ID\tJASPAR_IDs")
all_tfs = set(list(hocomoco.keys()) + list(jaspar.keys()))
for tf in sorted(all_tfs):
    hoc_id = hocomoco.get(tf, 'NA')
    jas_ids = ','.join(jaspar[tf]) if tf in jaspar else 'NA'
    print(f"{tf}\t{hoc_id}\t{jas_ids}")
