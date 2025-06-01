# Fusion Trascript Detection

This script was used to calculate the fusion transcripts for both patient and PDX samples. As input, the script takes the transcriptome sequencing data provided in the repository. This process was performed using STAR-Fusion v1.11.11 (STAR V.2.7.8a.). The Trinity Cancer Transcriptome Analysis Toolkit genome reference library Chieraviz V1.26.0  for GRCh38, which uses GENCODEv37 (Ensembl version 103) gene annotations, was used. The results were annotated and validated in-silico using FusionInspector V.2.7.0 with parameters: only fusions labelled as in-frame and out-of-frame, supported by ≥5 split reads and ≥5 spanning reads, with 'Yes anchor support' set to TRUE, left and right breakpoint entropy ≥1.5, and unknown coding effect or annotated as previously reported in normal tissues on the Genotype-Tissue Expression (GTEx) dataset were retained. Finally, results obtained were plotted using the Chimeraviz V1.26.0 package in R v1.34.0.

Extra references:
About STAR-Fusion: https://github.com/STAR-Fusion/STAR-Fusion
Extra reference to understand better STAR-Fusion outputs: https://nf-co.re/rnafusion/1.2.0/docs/output#star-fusion
About Chimeraviz: https://www.bioconductor.org/packages/release/bioc/html/chimeraviz.html 