from zatt.client import DistributedDict
from time import sleep

d = DistributedDict('97.107.138.108', 9000)

def regularblks(blkSize, blkInterval, numblks, miniblockSize, miniblockInterval): # blkSize units are 50KB, blkInterval ms
	if numblks > 1000000: numblks = 1000000
	for i in range(numblks):
		preprefix = ('%06d'%i).encode("utf8")
		blkunit = (("*".encode("utf8"))*miniblockSize)
		for j in range(blkSize):
			prefix = ('%04d'%j).encode("utf8")
			d['blk'+('%04d'%j)] = preprefix+"-".encode("utf8")+prefix+"-".encode("utf8")+blkunit
			sleep(float(miniblockInterval)/1000.0)
		sleep(float(blkInterval)/1000.0)