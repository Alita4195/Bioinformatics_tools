# 生物概念
- locus:the position of a gene or other significant sequence on a chromosome.
- Pseudogenes are like leftover copies of genes that used to be important in our ancestors but have lost their function over time.
# 测序相关
- mlst stands for "Multi-Locus Sequence Typing,the purpose of mlst is to identify the allelic profile of a bacterial isolate by analyzing the sequences of these housekeeping genes. 
- 基因簇venn diagram：首先确定cluster (具有相似功能注释或参与相似功能途径的基因可以被分到同一个基因 cluster)，然后可以进行近源物种之间或者同一物种不同生长周期序列画出Venn diagram.
- Fastq文件每四行表示一个read（如上图所示），其中第一第三行表示read名称等相关信息，第二行为read序列，第四行为第二行对应的每个碱基质量值。
- Read quality:读取质量通常以Phred质量分数（Phred Quality Score）表示。  
![Alt text](image.png)

# 工具
- dREP，它是一个用于分析微生物基因组之间相似性和亲缘关系的软件工具.
- GFF (Generic Feature Format) is a file format used to describe genomic features and annotations in biological sequences, such as DNA, RNA, and protein sequences. 
- BRIG (BLAST Ring Image Generator) is a bioinformatics tool used to visualize the similarity between genomes using BLAST comparisons.
- MASH， looks at these DNA codes and figures out how alike they are.
- bwa (Burrows-Wheeler Aligner) is a tool used for aligning DNA sequences to a reference genome. When you run bwa mem (or another bwa command), it aligns your sequencing reads to the
reference genome and produces a SAM (Sequence Alignment/Map) format output, which represents the alignments and mapping qualities.
- samtools is a set of tools for working with SAM (Sequence Alignment/Map) and BAM (Binary Alignment/Map) format files.

# NCBI
- GO_process 是指 "Gene Ontology Biological Process"
Gene Ontology（GO）是一种用于描述基因和蛋白质功能的标准化生物信息学术语和体系结构。
打开NCBI，在nucleotide 板块输入物种学名：

具体信息解读举例：
```
gene            complement(10810..10896) #该基因在互补链上的起始和结束位置
                /locus_tag="PP652_00050" #该基因的一个标签，用于唯一标识该基因
                /pseudo                  #标记为pseudo，通常它不会翻译成蛋白质，而是存在于基因组中但没有功能
CDS             complement(10810..10896) #与基因关联的蛋白质编码序列的注释行
                /locus_tag="PP652_00050" #唯一标识该蛋白质编码序列
                /inference="COORDINATES: similar to AA
                sequence:RefSeq:WP_003600284.1" #表示该蛋白质序列的推断，根据类似的氨基酸序列（AA sequence）推测出来，参考序列是RefSeq中的WP_003600284.1
                /note="incomplete; partial on complete genome; missing
                C-terminus; Derived by automated computational analysis
                using gene prediction method: Protein Homology." #蛋白质序列附加信息
                /pseudo                                          #标记为pseudo
                /codon_start=1 #翻译起始密码子的位置，这里是1，表示从序列的第一个密码子开始翻译。
                /transl_table=11
                /product="deoxyribose-phosphate aldolase" #蛋白质的功能-脱氧核糖磷酸醛缩酶
```

```
gene            1099120..1099725              #该基因在互补链上的起始和结束位置
                /gene="vanZ"                  #基因名称
                /locus_tag="LGG_01083"        #该基因的一个标签，用于唯一标识该基因
CDS             1099120..1099725
                /gene="vanZ"
                /locus_tag="LGG_01083"
                /codon_start=1
                /transl_table=11
                /product="Glycopeptide antibiotics resistance protein"
                /protein_id="CAR86978.1" 
                /db_xref="EnsemblGenomes-Gn:LGG_01083"   #与其他数据库的交叉引用，指示该基因在Ensembl Genomes数据库中的标识符为 "LGG_01083"
                /db_xref="EnsemblGenomes-Tr:CAR86978"
                /db_xref="InterPro:IPR006976"
                /db_xref="UniProtKB/TrEMBL:C7TBI5"
                /translation="MLFLGPFYNWINSTSLSQVNHFPLVRLIIFSLDKTILYLLVFAV
                LRCLWLVRHHRRTTFGRELKLGLFVGYLMLLFALTVFRDVYYPWQLVFHWQRSLSVIN
                LQPMVETLKLRQAASHFDLWYQSLGNVAWFMPLGFGIPWVSVHRRRLFAVVGIGLITS
                LSIETLQFLLISGVADIDDVIFNVIGAILGYAFYRLLHPKG"
```

