#!/usr/bin/python
# -*- coding: utf-8 -*-


def read_file(algorithm_name):
    to_read = open(algorithm_name, "r")
    output_matrix = {}
    possible_core_ids = ["@0","@1","@2","@3","@4","@5","@6","@7","@8"]
    for line in to_read: 
        split_line = line.split()
        try:
            execute = False
            for elem in possible_core_ids:
                if elem == split_line[0]:
                    execute = True
                    break
            
            if execute and line[0] == "@":
                core_id = split_line[0].replace("@","")
                instr = split_line[1]
                type_req = ""
                addr = ""
                to_write = ""
                if(len(split_line) == 3):
                    type_req = "R"
                    addr = split_line[2]
                else:
                    type_req = "W"
                    addr = split_line[3]
                to_write = instr+" "+addr+" "+type_req+"\n"
            
                if(to_write.find("@") == -1):
                    if core_id in output_matrix:
                        output_matrix[core_id].write(to_write)
                    else:
                        to_open_name = algorithm_name+"_"+core_id
                        to_open = open(to_open_name,"w") 
                        output_matrix[core_id] = to_open
                        output_matrix[core_id].write(to_write)
        except:
            p = 0

#algs = ["chai.bfs",
#"chai.ooptrns.mkl",
#"chai.ooptrns.run_threads",
#"darknet",
#"ligra.kcore.rmat.emd",
#"ligra.kcore.rmat.ems",
#"ligra.kcore.usa.emd",
#"ligra.kcore.usa.ems",
#"ligra.pagerank.rmat.emd",
#"ligra.pagerank.usa.emd",
#"ligra.radii.rmat.emd",
#"ligra.radii.rmat.ems",
#"ligra.radii.usa.ems",
#"parsec.ferret",
#"parsec.fluidanimate.processMT",
#"parsec.streamcluster",
#"phoenix.pca",
#"rodinia.backprop.ajust",
#"rodinia.backprop.layer",
#"rodinia.nw",
#"select.cpu",
#"splash.lu_ncb",
#"splash.ocean_ncp.jacobcalc",
#"splash.ocean_ncp.laplacalc",
#"splash.ocean_ncp.relax",
#"splash.ocean_ncp.slave2"]
algs = ["ligra.kcore.usa.emd","select.cpu"]
for algorithms in algs:
    read_file(algorithms)


    
