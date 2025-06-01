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

