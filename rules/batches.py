batchSize = 200

def nbatch():
    ns = len(samples)
    floor = ns // batchSize
    if ns % batchSize == 0:
        return floor
    else:
        return floor + 1
        

nbatch = nbatch()

batches = [[] for _ in range(nbatch)]
for i in range(len(samples)):
    batch = i // batchSize
    batches[batch].append(samples[i])

batchNames = []
for i in range(nbatch):
    batchNames.append("batch" + str(i))
    
batchDict = {}
for i in range(nbatch):
	batchDict[batchNames[i]] = frozenset(batches[i])
	
