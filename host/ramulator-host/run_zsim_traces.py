import os

#files = ["phoenix.kmeans","phoenix.mm","phoenix.pca","phoenix.wordcount", 
#         "rodinia.bfs","rodinia.bp1","rodinia.bp2","rodinia.kmeans","rodinia.myocyte","rodinia.nw","rodinia.sc",
#         "ligra","ligra.usa", "ligra.kcore.usa.emd", "ligra.radii.rmat.emd", "ligra.kcore.rmat.emd", "ligra.radii.usa.ems", "ligra.kcore.usa.ems", "ligra.radii.rmat.ems", "ligra.kcore.rmat.ems",
#         "graphmat.ds","graphmat.pg.usa",  
#         "select",
#         "splash.fft", "splash.luncb", "splash.ocean.jacobcalc","splash.ocean.laplacalc","splash.ocean.relax","splash.radiosity","splash.slave2"]

#files = ["select"]
#files = ["blk_matmult","dot_product","image_filter","mandelbrot","matmul","sobel","wf"]
files = ["chai.bfs_0",
"chai.ooptrns.mkl_0",
"chai.ooptrns.run_threads_0",
"ligra.kcore.rmat.emd_0",
"ligra.kcore.rmat.ems_0",
"ligra.kcore.usa.emd_0",
"ligra.kcore.usa.ems_0",
"ligra.pagerank.rmat.emd_0",
"ligra.pagerank.usa.emd_0",
"ligra.radii.rmat.emd_0",
"ligra.radii.rmat.ems_0",
"ligra.radii.usa.ems_0",
"select.cpu_0"]

for f in files:
    cmd = "./ramulator --config filtered-trace-paper-configs/HMC-config.cfg --mode=cpu --stats "+f+".hmc --trace /home/geraldo/Tools/zsim-ramulator/traces/filtered/"+f
    print cmd
    os.system(cmd) 