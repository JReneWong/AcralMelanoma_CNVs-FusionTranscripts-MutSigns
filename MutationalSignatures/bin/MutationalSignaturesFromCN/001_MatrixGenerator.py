#Using Sequenza outputs (paired samples) we generated the initial input file for the CN signatures calculation. Outputs should be processed in order to create a table with the following format and header:

#sample  chromosome      start.pos       end.pos Bf      N.BAF   sd.BAF  depth.ratio     N.ratio sd.ratio        CNt     A       B       LPP

#Generating the matrix with this input table

from SigProfilerMatrixGenerator.scripts import CNVMatrixGenerator as scna
file_type = "SEQUENZA"
input_file = "/PathToCNSignaturesInputTable.txt" 
output_path = "/OutputDir"
project = "Project_Name"
scna.generateCNVMatrix(file_type, input_file, project, output_path)

