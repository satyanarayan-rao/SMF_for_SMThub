# NOMe-seq footprint generation pipeline for SMTHub

SMTHub hosts FootPrint BigBed files generated from NOMe-seq and dSMF data for now. User may generate the bigbed file using this pipeline for the **NOMe-seq** data. 

## Create virtual environment and install required tools

```
mamba create -n smthub_production python=3.12
mamba activate smthub_production

mamba install -c bioconda snakemake=7.26 scanf trim-galore bedtools bismark samtools bamtools pandas
```

### Generate the BigBed file

```
snakemake  --snakefile nome_seq_data_to_smf_bigbed.smk suppressed_merged/suppressed_merged_demo_s2_to_dm3_with_wobble_1_min_fp_10_and_mvec.bb --configfile configs/config.yaml -j4

```
