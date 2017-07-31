from zatt.client import DistributedDict

d = DistributedDict('97.107.138.108', 9000)

def regularBlocks(blockSize, blockInterval, numBlocks): # blockSize units are 50KB, blockInterval ms
	if numBlocks > 1000000: numBlocks = 1000000
	for i in range(numBlocks):
		preprefix = ('%06d'%i).encode("utf8")
		blockunit = (("*".encode("utf8"))*16384)
		for j in range(blockSize):
			prefix = ('%04d'%j).encode("utf8")
			d['block'+('%04d'%j)] = preprefix+prefix+blockunit
		Thread.sleep(blockInterval)