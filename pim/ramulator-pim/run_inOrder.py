import os

#files = ["phoenix.kmeans","phoenix.mm","phoenix.pca","phoenix.wordcount", 
#         "rodinia.bfs","rodinia.bp1","rodinia.bp2","rodinia.kmeans","rodinia.myocyte","rodinia.nw","rodinia.sc",
#         "ligra.pagerank.rmat.emd","ligra.pagerank.usa.emd", "ligra.kcore.usa.emd", "ligra.radii.rmat.emd", "ligra.kcore.rmat.emd", "ligra.radii.usa.ems", "ligra.kcore.usa.ems", "ligra.radii.rmat.ems", "ligra.kcore.rmat.ems",
#         "graphmat.ds","graphmat.pg.usa",  
#         "select",
#         "splash.fft", "splash.luncb", "splash.ocean.jacobcalc","splash.ocean.laplacalc","splash.ocean.relax","splash.radiosity","splash.slave2"]


files = ["chai.bfs",
         "chai.ooptrns.mkl",
"chai.ooptrns.run",
"darknet",
"parsec.ferret",
"parsec.fluidanimate.2mt",
"parsec.fluidanimate.operator+",
"parsec.streamcluster",
"sandiego.sphinx.pure_channels",
"sandiego.svd3"]
for f in files:
    cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config-inOrder.cfg --mode=cpu --stats "+f+".inOrder.hmc.pim --trace ../pin-3.5/new_traces/"+f+".cpu --pim-cache-lines=0 --pim-org=inOrder"
    print cmd
    os.system(cmd)