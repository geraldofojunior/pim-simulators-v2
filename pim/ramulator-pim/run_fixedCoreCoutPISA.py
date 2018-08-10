import os

#files = ["phoenix.kmeans","phoenix.mm","phoenix.pca","phoenix.wordcount", 
#         "rodinia.bfs","rodinia.bp1","rodinia.bp2","rodinia.kmeans","rodinia.myocyte","rodinia.nw","rodinia.sc",
#         "ligra.pagerank.rmat.emd","ligra.pagerank.usa.emd", "ligra.kcore.usa.emd", "ligra.radii.rmat.emd", "ligra.kcore.rmat.emd", "ligra.radii.usa.ems", "ligra.kcore.usa.ems", "ligra.radii.rmat.ems", "ligra.kcore.rmat.ems",
#         "graphmat.ds","graphmat.pg.usa",  
#         "select",
#         "splash.fft", "splash.luncb", "splash.ocean.jacobcalc","splash.ocean.laplacalc","splash.ocean.relax","splash.radiosity","splash.slave2"]


files = ["Add", "Scale", "Copy", "Triad"]
cache_sizes = ["512","128","64","8","2","1","0"]


for f in files:
    for c in cache_sizes:
        cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-inOrder.cfg --mode=cpu --stats /home/geraldo/Tools/ramulator-morphcore/pisa_results/fixedCoreCount/inOrder/"+c+"/STREAM."+f+".inOrder.hmc.pim --trace /home/geraldo/Tools/pisa/resultsPisa/traces/STREAM/out"+f+"1M.filtered --pim-cache-lines="+c+" --pim-org=inOrder --pim-core-count=1"
        print cmd
        os.system(cmd)
        
        cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-inOrder.cfg --mode=cpu --stats /home/geraldo/Tools/ramulator-morphcore/pisa_results/fixedCoreCount/outOrder/"+c+"/STREAM."+f+".outOrder.hmc.pim --trace /home/geraldo/Tools/pisa/resultsPisa/traces/STREAM/out"+f+"1M.filtered --pim-cache-lines="+c+" --pim-org=outOrder --pim-core-count=1"
        print cmd
        os.system(cmd)