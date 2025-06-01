from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen
matrices = matGen.SigProfilerMatrixGeneratorFunc("ALM", "GenomeRef", "/InputPath/",plot=True, exome=True, bed_file="/PathToBEDFile", chrom_based=False, tsb_stat=False, seqInfo=True, cushion=100)

from SigProfilerExtractor import sigpro as sig
sig.sigProfilerExtractor("matrix", "/OutputFolder/", "/PathToPreviousOutput/", reference_genome="GRChGenomeRef38", minimum_signatures=1, maximum_signatures=10, nmf_replicates=100, cpu=-1)

