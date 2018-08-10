import os

#files = ["phoenix.kmeans","phoenix.mm","phoenix.pca","phoenix.wordcount", 
#         "rodinia.bfs","rodinia.bp1","rodinia.bp2","rodinia.kmeans","rodinia.myocyte","rodinia.nw","rodinia.sc",
#         "ligra.pagerank.rmat.emd","ligra.pagerank.usa.emd", "ligra.kcore.usa.emd", "ligra.radii.rmat.emd", "ligra.kcore.rmat.emd", "ligra.radii.usa.ems", "ligra.kcore.usa.ems", "ligra.radii.rmat.ems", "ligra.kcore.rmat.ems",
#         "graphmat.ds","graphmat.pg.usa",  
#         "select",
#         "splash.fft", "splash.luncb", "splash.ocean.jacobcalc","splash.ocean.laplacalc","splash.ocean.relax","splash.radiosity","splash.slave2"]


files = ["chai.vpack",
         "chai.vupack"]
cache_sizes = ["1", "2","8","64","128","512","0"]


for caches in cache_sizes:
    for f in files:
        cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-OoOrder.cfg --mode=cpu --stats results_morphCore_OoO/pim/"+caches+"_cache_line/"+f+".outOrder.hmc.pim --trace ../pin-3.5/new_traces/"+f+".cpu --pim-cache-lines="+caches+" --pim-org=outOrder"
        print cmd
        os.system(cmd)