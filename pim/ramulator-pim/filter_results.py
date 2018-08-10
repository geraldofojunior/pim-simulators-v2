import os
import csv

rootdir = "/home/geraldo/Tools/ramulator-morphcore/to_filter"


cpu_rate = 0.25
hmc_rate = 0.8

#energy pJ/bit
dram_energy = 2
tsv_energy  = 0.02
control_energy  = 1.6
serdes_energy = 0.54

#energy per access	
l1_energy = 29
l2_energy = 53
l3_energy = 440

chart = open("results_hmc.csv","w") 
chart.write("Algorithm\tVersion\tInstructions\tCycles\tIPC\tTime (ns)\tL1 Access\tL2 Access\t L3 Access\tMemory Access\tEnergy (pJ)\n")
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        tmp =  os.path.join(subdir, file)
        lists = tmp.split("/")
        counter = 0 
        version = ""
        benchmark = ""
        alg = ""
        
        for t in lists:
            if(counter == 7):
                alg = t
            if(counter == 6):
                if(t.find("no_pim")!=-1):
                    version = "Host"
                else:
                    version = "PIM"
            counter=counter+1
        
        ipc = 0
        instructions = 0
        cycles = 0
        time = 0.0
        l1 = 0
        l2 = 0
        l3 = 0
        memory = 0
        reads = 0
        writes = 0
        energy = 0.0
        
        if(version  == "Host"):
            with open(tmp, "r") as ins:
                for line in ins:
                    try:
                        line_tmp = line.split()
                        if(line.find("ramulator.cpu_instructions_core_0")!=-1):
                            instructions = int(line_tmp[1])
                        if(line.find("ramulator.cpu_cycles")!=-1):
                            cycles = int(line_tmp[1])
                        if(line.find("ramulator.L1_cache_total_access")!=-1):
                            l1 = int(line_tmp[1])
                        if(line.find("ramulator.L2_cache_total_access")!=-1):
                            l2 = int(line_tmp[1])
                        if(line.find("ramulator.L3_cache_total_access")!=-1):
                            l3 = int(line_tmp[1])
                        if(line.find("ramulator.read_requests")!=-1):
                            reads = int(line_tmp[1])
                        if(line.find("ramulator.write_requests")!=-1):   
                            writes = int(line_tmp[1])
                    except:
                        p = 0
            if(cycles != 0):
                ipc = instructions/float(cycles)
            if(ipc != 0):    
                time = float(instructions*(1/ipc)*cpu_rate)
            memory = reads+writes
            energy = float(l1*l1_energy + l2*l2_energy + l3*l3_energy + memory*(64*8*(dram_energy+tsv_energy+control_energy+serdes_energy)))
            chart.write(str(alg)+"\t"+str(version)+"\t"+str(instructions)+"\t"+str(cycles)+"\t"+str(ipc)+"\t"+str(time)+"\t"+str(l1)+"\t"+str(l2)+"\t"+str(l3)+"\t"+str(memory)+"\t"+str(energy)+"\n")
        else:
            with open(tmp, "r") as ins:
                for line in ins:
                    try:
                        line_tmp = line.split()
                        if(line.find("# total cpu instructions number")!=-1):
                            instructions = int(line_tmp[1])
                        if(line.find("ramulator.cpu_cycles")!=-1):
                            cycles = int(line_tmp[1])
                        if(line.find("ramulator.read_requests")!=-1):
                            reads = int(line_tmp[1])
                        if(line.find("ramulator.write_requests")!=-1):   
                            writes = int(line_tmp[1])
                        if(line.find("ramulator.total_cache_hits_pim")!=-1):   
                            l1 = int(line_tmp[1])
                    except:
                        p = 0
            if(cycles != 0):
                ipc = instructions/float(cycles)
            if(ipc != 0):
                time = float(instructions*(1/ipc)*hmc_rate)
            memory = reads+writes
            energy = float(l1*l1_energy +  memory*(64*8*(dram_energy+tsv_energy)))
            chart.write(str(alg)+"\t"+str(version)+"\t"+str(instructions)+"\t"+str(cycles)+"\t"+str(ipc)+"\t"+str(time)+"\t"+str(l1)+"\t"+str(l2)+"\t"+str(l3)+"\t"+str(memory)+"\t"+str(energy)+"\n")