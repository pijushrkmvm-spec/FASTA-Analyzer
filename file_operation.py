# File operation with Header,Length,Validity,A_Count,T_Count,G_Count,C_Count
import re
import csv

pattern = "^[GATC]+$"

with open ('sequence_multi.fasta', 'r') as file:
    header = ''
    sequence = ''
    results = []
    for line in file:
        line = line.strip()
        if line == '':
            continue
        if line[0] == '>':
            if sequence != '':
                if re.match (pattern, sequence):
                    validity = 'valid'
                    length = len(sequence)
                    a_count = sequence.count('A')
                    t_count = sequence.count('T')
                    g_count = sequence.count('G')
                    c_count = sequence.count('C')
                    gc_content = (g_count+c_count) / (a_count+t_count+g_count+c_count)
                    print(f"{header} is valid")
                    results.append([header, length, validity, a_count, t_count, g_count, c_count, gc_content])
            header = line
            sequence = ''
        else:
            sequence += line

    if sequence != '':
                if re.match (pattern, sequence):
                    validity = 'valid'
                    length = len(sequence)
                    a_count = sequence.count('A')
                    t_count = sequence.count('T')
                    g_count = sequence.count('G')
                    c_count = sequence.count('C')
                    gc_content = (g_count+c_count) / (a_count+t_count+g_count+c_count)
                    print(f"{header} is valid")
                    results.append([header, length, validity, a_count, t_count, g_count, c_count, gc_content])
                
 
with open ('sequence_multi.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Header', 'Length', 'Validity', 'A', 'T', 'G', 'C','GC Percentage'])
    writer.writerows(results)