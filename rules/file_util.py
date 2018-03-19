
def fastq1(wildcards) :
    """Return the path of the original fastq file 1."""
    return outFastq + "/" + wildcards.sample + "_1.fq"

def fastq2(wildcards) :
    """Return the path of the original fastq file 2"""
    return outFastq + "/" + wildcards.sample + "_2.fq"

def origBam(wildcards) :
    """Return the path of the original bam file."""
    return outAlign + "/" + wildcards.sample + ".bam"

def bamDupsMarked(wildcards):
    """Return the path of the bam file with duplicates marked."""
    return outAlign + "/" + wildcards.sample + ".duplicates_marked.bam"

def baiDupsMarked(wildcards):
    """Return the path of the index of the bam file with duplicates marked."""
    return outAlign + "/" + wildcards.sample + ".duplicates_marked.bai"

def realignerTargets(wildcards):
    """Return the path of the output intervals from RealignerTargetCreator."""
    return outRealign + "/" + wildcards.sample + ".interval_list"

def realignedBam(wildcards):
    """Return the path of the output bam file from IndelRealigner."""
    return outRealign + "/" + wildcards.sample + ".realign.bam"

def realignedBamIdx(wildcards):
    """Return the path of the output bam index file from IndelRealigner."""
    return outRealign + "/" + wildcards.sample + ".realign.bai"

def offTarget(wildcards):
    """Return the path of the off target count file"""
    return outOffTarget + "/" + wildcards.sample + ".off_target.txt"

def baseRecalibratorFirstPass(wildcards):
    """Return the path of the output from the first pass of BaseRecalibrator."""
    return outBQSR + "/" + wildcards.sample + ".base_recalibrator_first_pass.out"

def baseRecalibratorSecondPass(wildcards):
    """Return the path of the output from the second pass of BaseRecalibrator."""
    return outBQSR + "/" + wildcards.sample + ".base_recalibrator_second_pass.out"

def analyzeCovariatesPlots(wildcards):
    """Return the path of the plots output from AnalyzeCovariates"""
    return outBQSR + "/analyze_covariates_" + wildcards.sample + ".realign.BQSR.pdf"

def analyzeCovariatesCSV(wildcards):
    """Return the path of the CSV output from AnalyzeCovariates"""
    return outBQSR + "/analyze_covariates_" + wildcards.sample + ".realign.BQSR.csv"

def recalibratedBam(wildcards):
    """Return the path of the recalibrated bam file from PrintReads"""
    return outBQSR + "/" + wildcards.sample + ".recalibrated.bam"

def recalibratedBamIdx(wildcards):
    """Return the path of the recalibrated bam file index from PrintReads"""
    return outBQSR + "/" + wildcards.sample + ".recalibrated.bai"

def haplotypeCaller(wildcards):
    """Return the path of the vcf output file from HaplotypeCaller"""
    return outDiscovery + "/" + wildcards.sample + ".recalibrated.raw.snps.indels.g.vcf"

def batchGVCFs(sampleNames):
    """Return the paths of the vcf output files from HaplotypeCaller for a set of sample names"""
    return [outDiscovery + "/" + sample + ".recalibrated.raw.snps.indels.g.vcf" for sample in sampleNames]

def combineGVCFs(wildcards):
    """Return the combined VCF from CombineGVCFs"""
    return outDiscovery + "/multisample." + wildcards.batch + "g.vcf"

def genotypeGVCFs():
    """Return the genotyped VCF from GenotypeGVCFs"""
    return outDiscovery + "/multisample.genotyped.vcf"

def variantRecalSNPsRecal():
    """Return the recal output file from VariantRecalibrator for SNPs"""
    return outDiscovery + "/multisample.genotyped.SNP.recal"

def variantRecalSNPsTranches():
    """Return the tranches output file from VariantRecalibrator for SNPs"""
    return outDiscovery + "/multisample.genotyped.SNP.tranches"

def variantRecalIndelsRecal():
    """Return the recal output file from VariantRecalibrator for indels"""
    return outDiscovery + "/multisample.genotyped.indel.recal"

def variantRecalIndelsTranches():
    """Return the tranches output file from VariantRecalibrator for indels"""
    return outDiscovery + "/multisample.genotyped.indel.tranches"

def applyRecalibrationSNPs():
    """Return the recalibrated vcf file from ApplyRecalibration for SNPs"""
    return outDiscovery + "/multisample.genotyped.recalibrated.filtered.SNPs_only.vcf"

def applyRecalibrationIndels():
    """Return the recalibrated vcf file from ApplyRecalibration for indels (SNPs already recalibrated)"""
    return outDiscovery + "/multisample.genotyped.recalibrated.filtered.vcf"

def calculateGenotypePosteriors():
    """Return the output vcf file from CalculateGenotypePosteriors"""
    return outRefinement + "/multisample.genotyped.recalibrated.filtered.withPosteriors.vcf"

def variantFiltration():
    """Return the filtered callset from VariantFiltration"""
    return outRefinement + "/multisample.genotyped.recalibrated.filtered.withPosteriors.Gfiltered.vcf"

def variantEvaluation():
    """Return the output file from VariantEval"""
    return outVariantEval + "/multisample.genotyped.recalibrated.filtered.withPosteriors.Gfiltered.variantEval.txt"

def variantAnnotation():
    """Return the output file from VariantAnnotator"""
    return outVariantAnnot + "/multisample.genotyped.recalibrated.filtered.withPosteriors.Gfiltered.annotated.vcf"

def vcftoolsPlinkConv(chromosomes):
    """Return the ped output file from vcftools PLINK conversion"""
    return [outFormatConversion + "/multisample.genotyped.recalibrated.filtered.withPosteriors.Gfiltered.annotated." +
            chr + ext for chr in chromosomes for ext in [".tped", ".tfam"]]
    
def plinkBed(chromosomes):
    """Return the PLINK bed, bim, fam files"""
    return [outFormatConversion + "/multisample.genotyped.recalibrated.filtered.withPosteriors.Gfiltered.annotated." + 
            chr + ext for chr in chromosomes for ext in [".bed", ".bim", ".fam"]] 



 




