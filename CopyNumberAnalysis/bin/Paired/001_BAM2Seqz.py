#For each paired (Normal-Tumor sample) execute from module 001 to 003. 
#Then you will need to generate a table from the output from 003. 
#Details in the script. 

sequenza-utils bam2seqz -n /PathToNORMALBAMFile -t /PathToTUMORFile --fasta /PathToReferenceFASTA -gc /GCPercentageFile -o ./results/Output1

