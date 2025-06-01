data.file <- /PreviousOutput_Output2
Sample <- sequenza.extract(data.file, verbose=FALSE, assembly="hg123", chromosome.list= paste0("chr", c(1:22,"X","Y")))
CP <- sequenza.fit(Sample)
sequenza.results(sequenza.extract = Sample, cp.table = CP, sample.id=Sample_ID, out.dir = OutputFolder)
