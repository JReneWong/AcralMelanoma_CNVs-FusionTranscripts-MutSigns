#Mutational and Copy Number Signatures: Paired samples

Mutational and copy number signature analyses (Patient and PDX, separately) were performed using the tool SigProfilerExtractor v1.1.23 (Islam et al., 2022). SNVs and INDELs that passed the previously described filters were used as input data. Mutational signatures were extracted using the 96 SBS context with default parameters for exome data. For copy number signature, SEQUENZA segmentation data was used as input and setting minimum_signatures=1, maximum_signatures=10, nmf_replicates=100 and default parameters for the rest, for exome data. 


1. Mutational Signatures

We used the paired tumour MAF files (Variant Calling) to detect the mutational signatures. We built this main table with the following commands:

```bash
cat /PathToMAFSs/*.maf | cut -f1-16 | sort -u > ./MasterTable_MAF.maf
```
1.1 Running SigProfiler

```python
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen
matrices = matGen.SigProfilerMatrixGeneratorFunc("ALM", "GenomeRef", "/InputPath/",plot=True, exome=True, bed_file="/PathToBEDFile", chrom_based=False, tsb_stat=False, seqInfo=True, cushion=100)

from SigProfilerExtractor import sigpro as sig
sig.sigProfilerExtractor("matrix", "/OutputFolder/", "/PathToPreviousOutput/", reference_genome="GRChGenomeRef38", minimum_signatures=1, maximum_signatures=10, nmf_replicates=100, cpu=-1)
```

2. Copy Number Signatures

Using Sequenza outputs (paired samples) we generated the initial input file for the CN signatures calculation. Outputs should be processed in order to create a table with the following format and header:

sample  chromosome      start.pos       end.pos Bf      N.BAF   sd.BAF  depth.ratio     N.ratio sd.ratio        CNt     A       B       LPP

2.1 Generating the matrix with this input table

```python
from SigProfilerMatrixGenerator.scripts import CNVMatrixGenerator as scna
file_type = "SEQUENZA"
input_file = "/PathToCNSignaturesInputTable.txt" 
output_path = "/OutputDir"
project = "Project_Name"
scna.generateCNVMatrix(file_type, input_file, project, output_path)
```

2.2 Signature calculations

```python
from SigProfilerExtractor import sigpro as sig
sig.sigProfilerExtractor("matrix", "/OutputDir","/OutputFromMatrixGenerator.matrix.tsv", reference_genome="GenomeRef", minimum_signatures=1, maximum_signatures=10, nmf_replicates=100, cpu=-1)
```