#!/bin/bash
bam_file=$1
suppressed_bam=$2
samtools view -H ${bam_file} > ${suppressed_bam}.tmp.header
samtools view ${bam_file} | python scripts/suppress_for_smf.py | cat ${suppressed_bam}.tmp.header - | samtools view -Sb -o ${suppressed_bam} -
rm ${suppressed_bam}.tmp.header 
