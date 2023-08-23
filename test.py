from DNAToolKit import *
import random

from utilities import *


# rndDNAStr = "ATCGCTAGATGCact"
randDNAStr = "".join([random.choice(nucleotides) for nuc in range(100)])  # random list
DNAStr = validateSeq(randDNAStr)
reverse_DNAStr = reverse_complement(DNAStr)

print(validateSeq(randDNAStr))
print(colored(DNAStr))

print(countNucFrequency(DNAStr))
print(transcription(colored(DNAStr)), "\n")


print(f"5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {(reverse_DNAStr)[::-1]} 5'")
print(f"5' {reverse_complement(DNAStr)} 3'")

# print(f"GC Content: {gc_content(DNAStr)}%\n")
# print(f"GC Content in subsection k=10: {gc_content_subsec(DNAStr, k=10)}%\n")
print(f"Aminoacids sequence from DNA: {translate_seq(DNAStr)}\n")

print(codon_usage(DNAStr, "P"))
for frame in gen_reading_frames(DNAStr):
    print(frame)
    print(proteins_from_rf(frame))

# test_rf_fram = ["R", "M", "V", "L", "_"]
# print(proteins_from_rf(test_rf_fram))
for prot in all_proteins_from_orfs(DNAStr, 0, 0, True):
    print(prot)

filePath = "/home/nina/Downloads/sequence.fasta"
rawData = read_FASTA(filePath)
for key, value in rawData.items():
    data = value

for prot in all_proteins_from_orfs(data, 0, 0, True):
    print(prot)
