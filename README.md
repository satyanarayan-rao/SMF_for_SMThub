# NOMe-seq footprint generation pipeline for SMTHub

SMTHub hosts FootPrint BigBed files generated from NOMe-seq and dSMF data for now. User may generate the bigbed file using this pipeline for the **NOMe-seq** data. 

## Create virtual environment and install required tools

```
mamba create -n smthub_production python=3.12
mamba activate smthub_production

mamba install -c bioconda snakemake=7.26 scanf trim-galore bedtools bismark samtools bamtools pandas
```

## System Preparation

User has to perform a minimal setup before invoking the **Golden Command** that will generate the bigBed file.

We demonstrate an example of such setup using one NOMe-seq run from Mouse E16 Primordial Germ Cells stage data (PRJNA ID: [PRJNA316148](https://www.ebi.ac.uk/ena/browser/view/PRJNA316148)). The paied-end read files we use here are [SRR3288084_1.fastq.gz](ftp.sra.ebi.ac.uk/vol1/fastq/SRR328/004/SRR3288084/SRR3288084_1.fastq.gz) and [SRR3288084_2.fastq.gz](ftp.sra.ebi.ac.uk/vol1/fastq/SRR328/004/SRR3288084/SRR3288084_2.fastq.gz). 

Please follow the steps below: 

### Step 1: Download or locate data

Please either dowload the paired-end data or use your local private data. For this example, you can use the mentioned link to download these datasets. 

```
$ cd data
$ curl -JLO "ftp.sra.ebi.ac.uk/vol1/fastq/SRR328/004/SRR3288084/SRR3288084_1.fastq.gz" 
$ curl -JLO "ftp.sra.ebi.ac.uk/vol1/fastq/SRR328/004/SRR3288084/SRR3288084_2.fastq.gz"
```

### Step 2: Add a row for each sample in data/samples.tsv

Your `data/samples.tsv` should look like the following for this example.
```
$ cat data/samples.tsv
sample	paired_read_1_path	paired_read_2_path
mouse_e16_pcg	data/SRR3288084_1.fastq.gz	data/SRR3288084_2.fastq.gz
```

### Step 3: Populate config.yaml file

Under the `bam_merge_config` block in `configs/config.yaml`, you can add a key value pair like the following:

```
$ cat configs/config.yaml

sample_metadata: "data/samples.tsv"
bam_merge_config:
    mouse_e16: ["mouse_e16_pcg"]
process_footprints:
    wobble_1_min_fp_10:
        wobble_gap: 1
        min_fp_len: 10
```

### Step 4: Download the respective genome

Please decide the reference genome of your choice, and download it in the `ref_genome/<name>` folder. 

NOTE: if you plan to use pre-downloaded file, pleae make sure that it is kept in write-permission location because Bismark will write files there. We encourage keeping the reference genome in the above mentioned directory structure. 

```
$ cat ref_genome/genomes.tsv 
genome	fasta_path
mm10	ref_genome/mm10/mm10.fa
```

### Step 5: Run the Golden Command to generate bigBed file

```
snakemake -np --snakefile nome_seq_data_to_smf_bigbed.smk suppressed_merged/suppressed_merged_mouse_e16_to_mm10_with_wobble_1_min_fp_10_and_mvec.bb --configfile configs/config.yaml -j4
```
NOTE: The above command is a dry run. Please remove `-np` flag to run it in real.


File name `suppressed_merged/suppressed_merged_mouse_e16_to_mm10_with_wobble_1_min_fp_10_and_mvec.bb` has `mouse_e16` mapped to the list of samples under key `mouse_e16` in `configs/config.yaml`. So, if you wish to add one more sample to this, please i) add one row as described in _Step 2_, and ii) add that sample name in `configs/config.yaml` under key `mouse_e16` (see _Step 3_)
