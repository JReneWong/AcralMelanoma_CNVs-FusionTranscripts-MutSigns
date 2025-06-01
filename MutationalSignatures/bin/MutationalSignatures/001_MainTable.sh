#We used the paired tumour MAF files (Variant Calling) to detect the mutational signatures.

cat /PathToMAFSs/*.maf | cut -f1-16 | sort -u > ./MasterTable_MAF.maf

