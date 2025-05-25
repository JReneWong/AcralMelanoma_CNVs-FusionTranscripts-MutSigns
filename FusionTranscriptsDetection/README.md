# Fusion Trascript Detection

This script was used to calculate the fusion transcripts for both patient and PDX samples. As input, the script takes the transcriptome sequencing data provided in the repository. This process was performed using STAR-Fusion v1.11.11 (STAR V.2.7.8a.). The Trinity Cancer Transcriptome Analysis Toolkit genome reference library Chieraviz V1.26.0  for GRCh38, which uses GENCODEv37 (Ensembl version 103) gene annotations, was used. The results were annotated and validated in-silico using FusionInspector V.2.7.0 with parameters: only fusions labelled as in-frame and out-of-frame, supported by ≥5 split reads and ≥5 spanning reads, with 'Yes anchor support' set to TRUE, left and right breakpoint entropy ≥1.5, and unknown coding effect or annotated as previously reported in normal tissues on the Genotype-Tissue Expression (GTEx) dataset were retained. Finally, results obtained were plotted using the Chimeraviz V1.26.0 package in R v1.34.0.

```bash
for Folder in /InputFolder/; do

        #Variables to be used
        BAM_File=$(ls $Folder | grep -e '.bam$')
        BAM_File2=$(echo $Folder$BAM_File)
        Sorted_BAM=$(echo $BAM_File2 | sed -e 's/\.bam/_SortedBAM\.bam/')
        Patient_ID=$(echo $BAM_File | cut -d'_' -f7 | cut -d'.' -f1)
        R1_fastq=$(echo $Folder$Patient_ID'_R1.fastq.gz')
        R2_fastq=$(echo $Folder$Patient_ID'_R2.fastq.gz')
        STAR_Fusion_OutputFolder=$(echo $Folder'STARFusion_Output')

        #Extracting fastq files from BAM file
        samtools sort -n $BAM_File2 -o $Sorted_BAM
        samtools fastq -@ 8 $Sorted_BAM \
                -1 $R1_fastq \
                -2 $R2_fastq
                
        #Executing STAR-Fusion, using singularity
        singularity exec -e -B `pwd` -B /path/ \
        ./star-fusion.v1.11.1.simg \
        STAR-Fusion \
        --left_fq $R1_fastq \
        --right_fq $R2_fastq \
        --genome_lib_dir /ReferenceGenomeFolder/ \
        -O $STAR_Fusion_OutputFolder \
        --FusionInspector validate \
        --examine_coding_effect \
        --denovo_reconstruct
done
```

For visualization: 

```R
#############################################################################################

library(chimeraviz)

#############################################################################################

#Reading STAR-Fusion output file

Fusions <- import_starfusion("/OutputFromSTARFusion(Input)")
edb_Inputfile <- "/edbInputFile"
edb_Inputfile <- ensembldb::EnsDb(edb_Inputfile)

#############################################################################################

#The specific fusion corresponds to the n object in "Fusions"
Fusion <- get_fusion_by_id(Fusions, n)

#############################################################################################

pdf("/OutputFolder/", width = 30, height = 20)

plot_fusion_transcript_with_protein_domain(fusion = Fusion, edb = edb_Inputfile, bamfile = "/BamFilePath", bedfile = "/BEDFilePath", gene_upstream_transcript = "ATranscriptENSID", gene_downstream_transcript = "BTranscriptENSID", plot_downstream_protein_domains_if_fusion_is_out_of_frame = FALSE)

dev.off()
```

Extra references:
About STAR-Fusion: https://github.com/STAR-Fusion/STAR-Fusion
Extra reference to understand better STAR-Fusion outputs: https://nf-co.re/rnafusion/1.2.0/docs/output#star-fusion
About Chimeraviz: https://www.bioconductor.org/packages/release/bioc/html/chimeraviz.html 