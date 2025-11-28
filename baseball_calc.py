from time import sleep
from vecthree.vecthree import dot

# Total bases: Singles + 2 * doubles + 3 * triples + 4 * home runs (dot prod of [1,2,3,4] and [singles,doubles,triples,HR])
def TB(H,_2B,_3B,HR):
	md = H-(_2B+_3B+HR)
	return dot([1,2,3,4],[md,_2B,_3B,HR])

# Slugging %: total bases / at bats
def slug(TB,AB):
	return TB/AB

# Batting average: total bases / at bats
def batting(H,AB):
	return H/AB

# On-base % + slugging %
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

	# This is kept here to show the stats directly to the user when ran from a batch/shell script
	sleep(2)
