#!/bin/bash

# $1 : read id: acceptable values {1,2}. 1 indicates read 1, 2 indicates read 2 of paired-end reads
# $2 : sample id, example: Zygote1
# $3 : output file name
# $4 : metadata path: example: data_from_geo/sample_with_link.tsv

if [ $1 -eq 1 ]
then
    url=`cat $4 | awk -F '\t' '{if ($1==v){print $4}}' v=$2`
    ~/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh $url $3
    
elif [ $1 -eq 2 ] 
then
    url=`cat $4 | awk -F '\t' '{if ($1==v){print $5}}' v=$2`
    ~/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh $url $3
fi
