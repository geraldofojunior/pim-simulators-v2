import os

#files = ["phoenix.kmeans","phoenix.mm","phoenix.pca","phoenix.wordcount", 
#         "rodinia.bfs","rodinia.bp1","rodinia.bp2","rodinia.kmeans","rodinia.myocyte","rodinia.nw","rodinia.sc",
#         "ligra.pagerank.rmat.emd","ligra.pagerank.usa.emd", "ligra.kcore.usa.emd", "ligra.radii.rmat.emd", "ligra.kcore.rmat.emd", "ligra.radii.usa.ems", "ligra.kcore.usa.ems", "ligra.radii.rmat.ems", "ligra.kcore.rmat.ems",
#         "graphmat.ds","graphmat.pg.usa",  
#         "select",
#         "splash.fft", "splash.luncb", "splash.ocean.jacobcalc","splash.ocean.laplacalc","splash.ocean.relax","splash.radiosity","splash.slave2"]


files = ["Add", "Copy","Scale","Triad"]
core_count = ["1","2","4","8","16","32","64","128","256","512"]


for f in files:
    for c in core_count:
        cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-inOrder.cfg --mode=cpu --stats /home/geraldo/Tools/ramulator-morphcore/pisa_results/fixedCacheSize/inOrder/"+c+"/STREAM."+f+".inOrder.hmc.pim --trace /home/geraldo/Tools/pisa/resultsPisa/traces/STREAM/out"+f+"1M.filtered --pim-cache-lines=512 --pim-org=inOrder --pim-core-count="+c
        print cmd
        os.system(cmd)
        
        cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-inOrder.cfg --mode=cpu --stats /home/geraldo/Tools/ramulator-morphcore/pisa_results/fixedCacheSize/outOrder/"+c+"/STREAM."+f+".inOrder.hmc.pim --trace /home/geraldo/Tools/pisa/resultsPisa/traces/STREAM/out"+f+"1M.filtered --pim-cache-lines=512 --pim-org=outOrder --pim-core-count="+c
        print cmd
        os.system(cmd)