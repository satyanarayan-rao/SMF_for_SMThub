rule download_read1:
    params: 
        metadata_path = config["sample_metadata"]
    output:
        read1 = "data_from_geo/{sample}_1.fastq.gz"
    shell:
        "sh scripts/get_url_to_download.sh 1 {wildcards.sample} {output.read1} {params.metadata_path}" 

rule download_read2:
    params: 
        metadata_path = config["sample_metadata"]
    output:
        read2 = "data_from_geo/{sample}_2.fastq.gz"
    shell:
        "sh scripts/get_url_to_download.sh 2 {wildcards.sample} {output.read2} {params.metadata_path}"  

