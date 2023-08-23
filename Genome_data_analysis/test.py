from genomeToolkits import *

test = GenomeToolkit()
seq = "AAATCGATACG" * 10
kmer = "AA"

start_time = perf_counter()

print(test.count_kmer(seq, kmer))

finiTime = perf_counter()
runTime = finiTime - start_time
print(f"{runTime:0.5f}s")
print()

# 比较RUN SPEED
start_time = perf_counter()

print(test.count_kmer_regexp(seq, kmer))

finiTime = perf_counter()
runTime = finiTime - start_time
print(f"{runTime:0.5f}s")

print(test.find_most_frequent_kmers(seq, 3))
