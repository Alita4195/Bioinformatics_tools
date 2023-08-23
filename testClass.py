from bio_seq import bio_seq

# sample_dna = bio_seq("ATCGX")  # AssertionError: Provided data does not seem to be a correct DNA sequence
sample_dna = bio_seq("ATCG")
print(sample_dna.get_seq_info())
