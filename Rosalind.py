from DNAToolKit import *


file_path = "/home/nina/Downloads/rosalind_prot.txt"

target_path = "/home/nina/jupy/notebook/bioinfomatics/solved_rosalind_dna.txt"

# 读取源文件内容
with open(file_path, "r") as my_file:
    dna_sequence = my_file.read().strip()
    print(dna_sequence)


# 计算核苷酸频率
# nucleotide_frequency = countNucFrequency(dna_sequence)

rna_seq = translate_seq(dna_sequence)

# 打开目标文件并写入核苷酸频率
with open(target_path, "w") as new_file:
    new_file.write(rna_seq)
    # for nucleotide, count in nucleotide_frequency.items():
    #     new_file.write(f"{nucleotide}: {count}\n")
