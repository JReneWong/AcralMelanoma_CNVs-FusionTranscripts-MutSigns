# Copy Number Variants Analysis

Copy number calling for tumour samples with matched normal controls was done using the tool SEQUENZA v3.0.0 executed in python3 v3.8.8 and R v4.2.1. The R package copynumber v1.29.0.9 was used in combination with SEQUENZA to use the GRCh38 reference genome. BAM files from tumour/normal pairs were used as input data for this analysis. For PDX samples, BAM files with reads aligned against the GRCh38 reference genome and processed with XenofilteR (as described above) were used for analysis. Manual quality filtering of the outputs was performed, and all samples with a cellularity lower than 0.35 were excluded from follow-up analysis.  

Significant regions with frequent amplifications and deletions were identified using Gistic2 (V.2.0.23) with default parameters and using only one sample per patient. Segmentation data and copy number estimations retrieved from Sequenza were used as input. Regions were considered to be significant where estimated q-values were below 0.1. Focal and broad copy number scores per sample were obtained using the Web application CNApp (Franch-Expósito et al., 2020). CNApp was performed using default parameters and using SEQUENZA segmentation data as input, FCS and BCS profiles were compared between the patient tumour and PDX-X1 samples, and across mutational status groups (4WT, KIT, N/K/HRAS, NF1, and hailstorm status (absent vs present).

For tumour samples without matched normal controls, copy number calling was done using CNVkit (v0.9.10). Briefly, sex-specific reference profiles were generated using normal-against-normal copy number calling to filter out low quality normal samples, following the protocols described by Chandramohan, R. et al. (2022). Copy number alterations were called using the batch subcommand, gains were defined as segments with a log₂ ratio > 0.585, and losses as segments with a log₂ ratio < – 0.4. To reduce noise-related artifacts, we filtered samples based on signal variability: we calculated the median absolute deviation (MAD) of log₂ ratios for each sample, normalized this value based on segment length, and applied a modified z-score threshold of 3.5 to exclude outlier samples.

Calculating CNVs:

1. Sequenza

For each paired (Normal-Tumor) sample:

```python
#Step1
sequenza-utils bam2seqz -n /PathToNORMALBAMFile -t /PathToTUMORFile --fasta /PathToReferenceFASTA -gc /GCPercentageFile -o ./results/Output1

#Step2
sequenza-utils seqz_binning --seqz /PreviousOutput_Output1 -w 50 -o /Output2

#Step3
data.file <- /PreviousOutput_Output2
Sample <- sequenza.extract(data.file, verbose=FALSE, assembly="hg123", chromosome.list= paste0("chr", c(1:22,"X","Y")))
CP <- sequenza.fit(Sample)
sequenza.results(sequenza.extract = Sample, cp.table = CP, sample.id=Sample_ID, out.dir = OutputFolder)

#Step4: Giving format to the new input


#Open output file

OutputFile = open(/PreviousOutput_Output4, 'w')
################################################################################

#File format:
#chromosome      start.pos       end.pos Bf      N.BAF   sd.BAF  depth.ratio     N.ratio sd.ratio        CNt     A       B
with open(/PreviousOutput_Output3, 'r') as InputFile:
  next(InputFile) #Avoiding the header 
  for line in InputFile:
    line = line.split()
    Pre_Chr = line[0] #chr1
    Chr = Pre_Chr.replace("chr", "") 
    St_Pos = line[1] 
    End_Pos = line[2] 
    Num_Marks = line[4] 
    if not(line[9] == 'NA'):
    	Seg_CN = float(line[9]) 
     	if not(Seg_CN == 0):
        	Log2_Seg_CN = math.log(Seg_CN, 2)
      	else:
        	Log2_Seg_CN = "-Inf"
      	#Creating new line
      	New_Line = SampleID+'\t'+Chr+'\t'+St_Pos+'\t'+End_Pos+'\t'+Num_Marks+'\t'+str(Log2_Seg_CN)+'\n'
      	print(SampleID, St_Pos, Seg_CN)
      	#Writing the new line in the output file
	OutputFile.write(New_Line)
```

MasterInputTable.txt is a table obtained by concatenating the segmentation files from Step4. This table is the input for 2. Gistic2. 

```bash
gistic2 -b ./results/ -seg /PathToMasterInputTable.txt -refgene /PathToReference/ -savegene 1
```

For tumor-only samples (No available normal paired sample).

```bash
#Creating Panel of Normals
cnvkit.py batch -n /PathNormal1.bam /PathNormal2.bam /PathNormal3.bam --targets /PathToBEDFile -f /PathToReferenceFASTAFile  --output-reference /PathToOutputRef.cnn --output-dir /PathToOutputDir

#CNVKit. For each tumor-only sample
cnvkit.py batch /PathToInputBAM -r /PathToOutputRef.cnn --scatter --diagram -d /PathToOutputDir
```

