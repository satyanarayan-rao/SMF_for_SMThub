args = commandArgs(trailingOnly = T)


dt = read.table(file("stdin"), sep = "\t", header =F, stringsAsFactors = F)

br_values = read.table(args[1], sep = "\t", header = F, stringsAsFactors = F)

dt$V1 = as.numeric(dt$V1)

pdf(args[2], height = 4, width = 6)
h_val = hist (dt$V1, breaks = br_values$V1, plot = F)
hist (dt$V1, breaks = br_values$V1, freq = F, 
      main = "Putative Footprint Length Distribution",
      xlab = "Footprint Length [bp]",
      ylab = "Norm. Freq. [AU]")
abline (v = c (10,20,30,40), lty = 2, col = "red")
dev.off()
df_to_write = data.frame(br = h_val$mids, freq = h_val$density, cnt = h_val$counts)
write.table(df_to_write,  row.names = F, col.names = F, quote =F, sep = "\t")

