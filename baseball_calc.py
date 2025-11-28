from time import sleep
from vecthree.vecthree import dot

def TB(H,_2B,_3B,HR):
	md = H-(_2B+_3B+HR)
	return dot([1,2,3,4],[md,_2B,_3B,HR])

def slug(TB,AB):
	return TB/AB

def batting(H,AB):
	return H/AB

def OPS(SLG, H, BB, AB):
	return SLG+((H+BB)/AB)

if __name__ == "__main__":
	print('Enter AB')
	AB = int(input(''))

	print('Enter Hits')
	hits = int(input(''))

	print('Enter 2B')
	_2B = int(input(''))

	print('Enter 3B')
	_3B = int(input(''))

	print('Enter HR')
	HR = int(input(''))

	print('Enter BB')
	BB = int(input(''))

	tb = TB(hits, _2B, _3B, HR)
	slugging = slug(tb, AB)

	print('TB:', tb)
	print('Avg:', batting(hits, AB))
	print('Slugging:', slugging)
	print('OPS:', OPS(slugging, hits, BB, AB))
	
	sleep(2)
