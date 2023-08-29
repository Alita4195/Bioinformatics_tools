import urllib.request
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import ExPASy  # use a handle to download a SwissProt file from ExPASy
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW

url = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta"
local_filename = "ls_orchid.fasta"
url2 = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.gbk"
local_filename2 = "ls_orchid.gbk"
# urllib.request.urlretrieve(url, local_filename)

urllib.request.urlretrieve(url2, local_filename2)
with open(local_filename2, "r") as f:
    data = f.read()

# print(data)

# for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))

# print("AAAA".count("AA"))

unknown_seq = Seq(None, 10)
print(len(unknown_seq))

record_iterator = SeqIO.parse("ls_orchid.gbk", "genbank")
first_record = next(record_iterator)
print(
    first_record
)  # This gives a human readable summary of most of the annotation data for the SeqRecord.

all_species = [
    seq_record.annotations["organism"]
    for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank")
]
print(all_species)


with ExPASy.get_sprot_raw("O23729") as handle:
    seq_record = SeqIO.read(handle, "swiss")
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])

result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
# if you have a nucleotide sequence you want to search against the nucleotide database (nt) using BLASTN, and you know the GI number of your query sequence
