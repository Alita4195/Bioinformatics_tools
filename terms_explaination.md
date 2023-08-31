# 生物概念
- locus:the position of a gene or other significant sequence on a chromosome.
- Pseudogenes are like leftover copies of genes that used to be important in our ancestors but have lost their function over time.
# 测序相关
- mlst stands for "Multi-Locus Sequence Typing,the purpose of mlst is to identify the allelic profile of a bacterial isolate by analyzing the sequences of these housekeeping genes. 
- 基因簇venn diagram：首先确定cluster (具有相似功能注释或参与相似功能途径的基因可以被分到同一个基因 cluster)，然后可以进行近源物种之间或者同一物种不同生长周期序列画出Venn diagram.
- Fastq文件每四行表示一个read（如上图所示），其中第一第三行表示read名称等相关信息，第二行为read序列，第四行为第二行对应的每个碱基质量值。
# 工具
- dREP，它是一个用于分析微生物基因组之间相似性和亲缘关系的软件工具.
- GFF (Generic Feature Format) is a file format used to describe genomic features and annotations in biological sequences, such as DNA, RNA, and protein sequences. 
- BRIG (BLAST Ring Image Generator) is a bioinformatics tool used to visualize the similarity between genomes using BLAST comparisons.
- MASH， looks at these DNA codes and figures out how alike they are.
- bwa (Burrows-Wheeler Aligner) is a tool used for aligning DNA sequences to a reference genome. When you run bwa mem (or another bwa command), it aligns your sequencing reads to the
reference genome and produces a SAM (Sequence Alignment/Map) format output, which represents the alignments and mapping qualities.
- samtools is a set of tools for working with SAM (Sequence Alignment/Map) and BAM (Binary Alignment/Map) format files.