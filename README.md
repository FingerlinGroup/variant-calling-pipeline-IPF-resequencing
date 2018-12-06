# Summary

This repository contains a Snakemake pipeline that implements the [GATK Best Practices](https://software.broadinstitute.org/gatk/best-practices/) for variant calling. The pipeline assumes targeted sequencing of specific genomic intervals. This is the code that was used to call variants for Moore et al., "Host Defense and Cell Senescence Gene Variants Contribute to the Risk of Idiopathic Pulmonary Fibrosis".

# To run

[Snakemake](https://snakemake.readthedocs.io/en/stable/) is required.

`snakemake --snakefile Snakefile --configfile config.json`

Note: the config file `config.json` includes general values that need to be replaced with actual values for your local environment.


