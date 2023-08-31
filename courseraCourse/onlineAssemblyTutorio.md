# Bacterial Genome Analysis
THIS WORKFLOW USES ILLUMINA AND NANOPORE READS
running the tool with  *--help* if there is any flag or option that are out of knowledge

1. Qc --fastqc软件
2. trimming: 去除低质量的reads, move sequence adapters --fastqc
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
 
# 微生物重测序
微生物重测序是基于高通量测序数据，与近缘参考基因组进行比对，进行变异检测的方法。通过重测序可以获得目标基因组对于参考基因组的SNP、InDel、SV等一系列变异信息，从中尝试对基因组之间的性状差异进行解析，或作为标记进行大规模的进化分析。
## 流程
1. 参考基因组文件: NCBI下载基因组序列ref.fa和基因组注释文件ref.gff(用于变异注释)
2. bwa mapping到参考基因组
    1) 为参考基因组建立索引
bwa index ref.fa #参数说明：
-a BWT构建算法：bwtsw, is of rb2 [default]，bwtsw适用于较长基因组
-p 索引的前缀
-b bwtsw算法模块长度，与-a bwtsw一起使用，[default 10000000]

    2) 寻找SA coordinates
sam文件格式如下，以@开头的行为注释行，没有@开头的部分为具体比对信息，每行表示一条read与参考基因组的比对情况，每行共有12列，依次为：read name，flag,参考序列编号，比对上的位置，mapping的质量值，简要比对信息表达式，下一个片段比对上的参考序列编号，下一片段比对到参考序列上的第一个碱基位置，参考序列和比对上的序列共同组成的序列Template的长度，序列片段信息，序列质量值信息以及可选区域（格式为TAG TYPE VALUE）。
    3) 将sam进行排序，并转换为bam文件
参数说明：
-a 输出所有位点，包括深度为0的位点；
-l read长度阈值，低于该长度的read将被忽略；
-d 最大覆盖深度，默认8000；
-q 碱基质量阈值；
-Q 比对质量阈值；

3. Samtools变异检测
    1) 输入文件
比对结果文件sample.sort..bam和参考基因组序列ref.fa（上一期已对其建立索引，此处不再建立索引）;

    2) Variant Calling主要流程
        - Samtools index sample.sort.bam#对bam文件建立索引,默认生成文件为bam文件加.bai,此处生成sample.sort.bam.bai;

        - Samtools rmdup sample.sort.bam sample.dedup.bam#去除PCR等实验过程中产生的多余duplications;

        - Samtools mpileup –q 20 –d 8000 –ugo sample.bcf –f ref.fa sample.dedup.bam#variant calls

备注：参考自https://maimengkong.com/zu/1347.html






