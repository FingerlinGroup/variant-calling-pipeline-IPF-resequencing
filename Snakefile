# Inputs
data=config["directories"]["data"]
samples=config["samples"]
chromosomes=config["chromosomes"]
reference=config["inputs"]["reference"]
intervals=config["inputs"]["intervals"]
intervalsBed=config["inputs"]["intervals_bed"]
intervalsBedNoChr=config["inputs"]["intervals_bed_nochr"]
mills=config["inputs"]["mills"]
thousand_genomes_SNPs=config["inputs"]["thousand_genomes_SNPs"]
hapmap=config["inputs"]["hapmap"]
dbsnp=config["inputs"]["dbsnp"]
dbsnp129=config["inputs"]["dbsnp129"]
omni=config["inputs"]["omni"]

# Software
java=config["software"]["java"]
jvm=config["software"]["jvm"]
gatk=config["software"]["gatk"]
bwa=config["software"]["bwa"]
samtools=config["software"]["samtools"]
picard=config["software"]["picard"]
picardDir=config["software"]["picardDir"]
offTargetScript=config["software"]["off_target"]
vcftools=config["software"]["vcftools"]
plink=config["software"]["plink"]

# Output directories
outFastq=config["directories"]["output"]["fastq"]
outAlign=config["directories"]["output"]["alignment"]
outRealign=config["directories"]["output"]["realignment"]
outOffTarget=config["directories"]["output"]["off_target"]
outBQSR=config["directories"]["output"]["bqsr"]
outDiscovery=config["directories"]["output"]["variant_discovery"]
outRefinement=config["directories"]["output"]["callset_refinement"]
outVariantEval=config["directories"]["output"]["variant_eval"]
outVariantAnnot=config["directories"]["output"]["variant_annotation"]
outFormatConversion=config["directories"]["output"]["format_conversion"]

# Include rules
include:
	config["directories"]["rules"] + "file_util.py"
include:
	config["directories"]["rules"] + "batches.py"
include:
	config["directories"]["rules"] + "revert_bam.rules"
include:
	config["directories"]["rules"] + "alignment.rules"
include:
	config["directories"]["rules"] + "realignment.rules"
include:
	config["directories"]["rules"] + "bqsr.rules"
include:
	config["directories"]["rules"] + "off_target.rules"
include:
	config["directories"]["rules"] + "discovery.rules"
include:
	config["directories"]["rules"] + "refinement.rules"
include:
	config["directories"]["rules"] + "evaluation.rules"
include:
	config["directories"]["rules"] + "annotation.rules"
include:
	config["directories"]["rules"] + "format_conversion.rules"


##### Run workflow #####

## Revert bams only
#rule all:
#	input:
#		expand(outFastq + "/{sample}_1.fq", sample=samples),
#		expand(outFastq + "/{sample}_1.fq", sample=samples)
		
## BWA only
#rule all:
#	input:
#		expand(outAlign + "/{sample}.bam", sample=samples)
		
# Through realignment only
#rule all:
#	input:
#		expand(outRealign + "/{sample}.realign.bam", sample=samples)

## Entire pipeline
rule all:
    input:
    	[outOffTarget + "/" + sample + ".off_target.txt" for sample in samples],
    	variantEvaluation(),
    	variantAnnotation(),
    	plinkBed(chromosomes)




		
