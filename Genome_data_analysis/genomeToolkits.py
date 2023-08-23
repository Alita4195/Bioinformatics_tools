# lesson 1
import re
import time
from time import perf_counter


class GenomeToolkit:
    def __init__(self):
        print("Hi Tools")

    # lesson 2
    def count_kmer(self, sequence, kmer):
        """不同物种具有特异的Kmer"""
        kmer_count = 0

        for position in range(len(sequence) - (len(kmer) - 1)):
            if sequence[position : position + len(kmer)] == kmer:
                kmer_count += 1

        return kmer_count

    # lesson 3
    # regExp solution
    def count_kmer_regexp(self, seq, kmer):
        return len(re.findall(f"(?=({kmer}))", seq))

    def find_most_frequent_kmers(self, sequence, k_len):
        kmer_frequencies = {}

        for i in range(len(sequence) - k_len + 1):
            kmer = sequence[i : i + k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1

        highest_frequency = max(kmer_frequencies.values())

        return [
            kmer
            for kmer, frequency in kmer_frequencies.items()
            if frequency == highest_frequency
        ]
