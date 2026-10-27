#Mutational and Copy Number Signatures: Paired samples

Mutational and copy number signature analyses (Patient and PDX, separately) were performed using the tool SigProfilerExtractor (Islam et al., 2022). SNVs and INDELs that passed the previously described filters were used as input data. Mutational signatures were extracted using the 96 SBS context with default parameters for exome data. For copy number signature, SEQUENZA segmentation data was used as input and setting minimum_signatures=1, maximum_signatures=10, nmf_replicates=100 and default parameters for the rest, for exome data.

Packages versions:
Python Version: 3.10.21
SigProfilerExtractor Version: 1.4.1
SigProfilerPlotting Version: 1.4.3
SigProfilerMatrixGenerator Version: 1.3.6
SigProfilerAssignment Version: 1.1.5
Pandas version: 2.3.3
Numpy version: 2.2.6
Scipy version: 1.15.3
Scikit-learn version: 1.7.2 
