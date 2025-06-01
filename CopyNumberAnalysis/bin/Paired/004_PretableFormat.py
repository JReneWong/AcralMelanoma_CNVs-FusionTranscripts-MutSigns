#This module requires as input to indicate the output folder from module 003. 

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

