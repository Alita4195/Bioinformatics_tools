# Bacterial Genome Analysis
THIS WORKFLOW USES ILLUMINA AND NANOPORE READS
running the tool with  *--help* if there is any flag or option that are out of knowledge

1. Qc --fastqc软件
2. trimming: 去除低质量的reads --fastqc
3. Assembly --SPAdes:When you run spades.py with the appropriate command-line arguments, it orchestrates the genome assembly process by utilizing various algorithms and modules included within the SPAdes software package.
#paired-end sequencing data
github 有option 以及格式
生成文件内部有2个重要的文件： contigs.fasta; scaffolds.fasta(raw_assembly.fasta)

4. polishing --pilon
polish trimmed reads
bwa index
align the paired-end reads to raw_assembly
samtools, convert file format
create samtools index
polish assembly
5. QC for assembled genome --Quast: provide reference genome 
6. reference guided scaffold --ragtag:reorder genome assembly contigs
7. typing --MLST
8. Check for antimicrobial resistance genes--abricate
9. Annotation --prokka
...










