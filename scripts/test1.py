import sys
from collections import defaultdict

DNA_state_dict = defaultdict(lambda: defaultdict(lambda: {'count': 0, 'percentage': 0}))

for line in sys.stdin:
    line = line.strip().split('\t')
    chrom, start, end, window, label, count, percentage = line
    count = int(count)
    percentage = float(percentage)

    DNA_state_dict[(chrom, start, end, window)][label]['count'] = count
    DNA_state_dict[(chrom, start, end, window)][label]['percentage'] = percentage

print("Chromosome\tStart\tEnd\tWindow\tTF_Occupancy_Percentage\tTF_Occupancy_Count\tNaked_DNA_Percentage\tNaked_DNA_Count\tNuc_Occupancy_Percentage\tNuc_Occupancy_Count\tTotal_Count")

for (chrom, start, end, window), label_data in DNA_state_dict.items():
    tf_count = label_data['TF_occupancy']['count']
    tf_percentage = label_data['TF_occupancy']['percentage']

    naked_count = label_data['naked_DNA']['count']
    naked_percentage = label_data['naked_DNA']['percentage']

    nuc_count = label_data['nuc_occupancy']['count']
    nuc_percentage = label_data['nuc_occupancy']['percentage']

    total_count = tf_count + naked_count + nuc_count

    print(chrom, start, end, window, tf_percentage, tf_count, naked_percentage, naked_count, nuc_percentage, nuc_count, total_count, sep="\t")
