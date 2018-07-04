import sys

def filterTrace(inputName, outputName, maxInstructions):
    outputFile = open(outputName,"w")
    inputFile = open(inputName, "r")
    
    delta = 0
    intial = 0
    final = 0
    totalInstructions = 0
    for line in inputFile:
        if(totalInstructions % 10000 == 0):
            print "Number of Instructions: " +str(totalInstructions)
        if (line.find("THREAD_ID") == -1):
            lineSpit = line.split()
    
            try:
                final = int (line[2])
            except:
                break 
            delta = final - intial 
            initial = final 
	    totalInstructions+=delta +1
            
            outputFile.write(line)
            if(totalInstructions > maxInstructions):
                break
            
if (len(sys.argv)!= 4):
    print "Usage: python filterPisaTraces inputName outputName maxInstructions \n"
else:
    filterTrace(sys.argv[1], sys.argv[2], int(sys.argv[3]))