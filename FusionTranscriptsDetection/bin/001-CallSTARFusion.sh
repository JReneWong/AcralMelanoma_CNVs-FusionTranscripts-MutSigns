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
