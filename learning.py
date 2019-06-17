import torch
import numpy as np
def one_hot_encode(seq):
#    map = np.asarray([[0, 0, 0, 0],
#                      [1, 0, 0, 0],
#                      [0, 1, 0, 0],
#                      [0, 0, 1, 0],
#                      [0, 0, 0, 1]])
#	numpy version
	map=torch.tensor([[0, 0, 0, 0],
	                  [1, 0, 0, 0],
	                  [0, 1, 0, 0],
	                  [0, 0, 1, 0],
	                  [0, 0, 0, 1]])
	seq = seq.upper().replace('A', '\x01').replace('C', '\x02')
	seq = seq.replace('G', '\x03').replace('T', '\x04').replace('N', '\x00')
	#return map[np.fromstring(seq, np.int8) % 5] numpy version

	map = map[np.fromstring(seq, np.int8)%5]
	return map

if __name__=='__main__':
	one_hot_encode("ATCTATCATCATCGCAT")

