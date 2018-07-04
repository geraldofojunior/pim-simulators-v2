import os
from threading import Thread
from time import sleep

def threaded_function(type):
	#files = ["ligraKCoreEMDrmat.cfg","ligraKCoreEMDusa.cfg","ligraPageRankEMDrmat.cfg","ligraPageRankEMDusa.cfg","ligraRadiiEMDrmat.cfg","ligraRadiiEMDusa.cfg"]
	#files = ["ligraKCoreEMSrmat.cfg","ligraKCoreEMSusa.cfg","ligraRadiiEMSrmat.cfg","ligraRadiiEMSusa.cfg"]
        #files = ["selectRunCPUthreads.cfg"]
	#files = ["selectLoad.cfg"]
	files = ["rodiniaBFS.cfg", "rodiniaBackpropAdjustWeights.cfg","rodiniaCFG.cfg","rodiniaKmeans.cfg","rodiniaMyOcyteMaster.cfg","rodiniaNW.cfg","rodiniaSrad.cfg","rodiniaStreamcluster.cfg"]

	for f in files:
		if(type == "host"):
    			cmd = "./build/opt/zsim pimBenConfigs/hostConfig/rodinia/"+f
    			print cmd
    			os.system(cmd)
		elif(type == "pim"):
    			cmd = "./build/opt/zsim pimBenConfigs/pimConfig/rodinia/"+f
    			print cmd
    			os.system(cmd)

thread1 = Thread(target = threaded_function, args = ("host", ))
thread1.start()

thread2 = Thread(target = threaded_function, args = ("pim", ))
thread2.start()
