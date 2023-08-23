# lesson 1
import collections
from collections import Counter

from structures import *
from bio_structs import DNA_Codons


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
        else:
            return tmpseq


def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "T": 0, "G": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(collections.Counter(seq))


# lesson 2
def transcription(seq):  # DNA is transcript to RNA
    """DNA-RNA"""
    return seq.replace("T", "U")


def complement(seq):
    return "".join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


# def reverse_complement(seq):
#     return "".join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


# note
# str = "test"
# print(str[::-1])


def reverse_complement(seq):
    """better solution"""
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]


# lesson 3
def gc_content(seq):
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)


def gc_content_subsec(seq, k=10):
    """Particular part of DNA"""
    result = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i : i + k]
        result.append(gc_content(subseq))
    return result


# lesson 4
def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos : pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]


def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []

    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i : i + 3]] == aminoacid:
            tmpList.append(seq[i : i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict


# lesson 5
def gen_reading_frames(seq):
    """要考虑六个阅读框，以确保不错过可能的编码区域"""
    frame = []
    frame.append(translate_seq(seq, 0))
    frame.append(translate_seq(seq, 1))
    frame.append(translate_seq(seq, 2))
    frame.append(translate_seq(reverse_complement(seq), 0))
    frame.append(translate_seq(reverse_complement(seq), 1))
    frame.append(translate_seq(reverse_complement(seq), 2))
    return frame


# lesson 6
def proteins_from_rf(aa_seq):
    """search for start M codon end_ codon"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins


# lesson 7


def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos:endReadPos])
    else:
        rfs = gen_reading_frames(seq)
    result = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            result.append(p)
    if ordered:
        return sorted(result, key=len, reverse=True)  # order: from longest to shortest
    return result
