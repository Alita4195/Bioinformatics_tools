#Genome Assembly
1.Nanopore三代测序分析流程：
1) 数据预处理,使用poretools或MinKNOW等软件从Nanopore设备中获取原始FAST5数据，并使用albacore或Guppy等软件将FAST5数据转换为FASTQ格式。
2) qc,使用Nanoplot软件绘制详细的质量数据图。
3) trimming,NanoFilt或Porechop等软件进行低质量数据去除，前后端或adapter修剪.
4) 与ref对比，使用Minimap2或其他基准比对软件将经过质量过滤和修剪的reads比对到参考基因组或转录组中。
5) 组装，使用Canu或Flye等读取组装软件对基准比对后的reads进行组装。
6) 结果评估与注释,使用QUAST或其他评估工具对组装结果进行比较和评估。然后对其进行注释。
7) 数据分析,使用不同的工具和软件分析组装结果，例如基因预测，基因功能注释和基因家族分析。

2.Pacbio三代测序分析流程：
1) HifiAdapterFilt
2) Qc, FastQC 
3) assembly, Hifiasm
3) Quast



# Genome Reseqencing
1）qc
2) trimming

Genome mapping
3) indexing of ref genome (bwa软件)
4）Aligning Reads to a Ref (bwa)
mapping is a computationally expensive process!

5）samtools进行变异检测
convert sam file to bam file (samtools)
BAM（Binary Alignment/Map）文件是其二进制表示,通常比SAM文件更小，占用更少的存储空间
![Alt text](image-3.png)
sort bam file #在许多生物信息学分析中，数据必须按某种顺序排列，以便有效地执行操作。
sorted.bam used for variant calling
结果读取:
https://www.htslib.org/doc/samtools-flagstat.html
```bash
samtools flagstat output.sorted.bam >mappingstats.txt
```
![Alt text](image-4.png)

6）variant calling (bcftools)
bcftools可以将原始测序数据（通常是BAM文件）与参考基因组比对，并识别出SNPs和Indels等变异位点。它可以生成VCF（Variant Call Format）文件，其中包含了变异位点的详细信息，如位置、变异类型、质量得分等。
https://samtools.github.io/bcftools/bcftools.html
- 生成 .bcf 文件
```bash
bcftools mpileup -0 b -o raw.bcf f <ref> --threads 8 -q 20 -Q 30 output.sorted.bam
```
```bash
bcftools call --ploidy 1 -m -v -o variants.raw.vcf raw.bcf #call the variants
```
结果读取：
```bash
bcftools view -v snps variant.raw.vcf | grep -v -c "^#" <filename>
```
查看变异位点
```bash
bcftools query -f "%POS\n" variant.raw.vcf >pos.txt
```
7）Variant Filtering
https://www.youtube.com/watch?v=Ht8PbwP8qQ4

8）Annotation 

#可以去看黑人小哥tutorial on snippy, bcftools and freebayes
基本流程：
![Alt text](image-1.png)

# 其他好用工具
1. blast -Linux command line 见https://www.youtube.com/watch?v=1AzujLnr3RM

2. Artemis 工具使用见 https://www.youtube.com/watch?v=XrE5SK0n8y0
read an entry 打开的是自己手动注释的文件？ .tab 格式的数据

# 如果用的是server：
server 没有浏览器
![Alt text](image-2.png)
python 脚本如上图所示

