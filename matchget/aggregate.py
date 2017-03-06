
import pprint
import msgpack
import requests

f = open('../games/4to6k.txt')
match_ids = f.read().split()
total = len(match_ids)
f.close()

agg = {}

for x in enumerate(match_ids):
	index, match_id = x
	progress = "%8d of %d:" % (index,total)
	filename = '../games/individual/game'+match_id+'.dat'

	print 'working on', progress, filename, 

	f = open(filename)
	packed_data = f.read()
	data = msgpack.unpackb(packed_data)
	f.close()

	if data['match_id'] != int(match_id):
		print 'error!', match_id, 'and', data['match_id']
	else:
		agg[int(match_id)] = packed_data

		CURSOR_UP_ONE = '\x1b[1A'
		ERASE_LINE = '\x1b[2K'
		print(CURSOR_UP_ONE + ERASE_LINE)


f = open('../games/all.dat', 'w')
f.write(msgpack.packb(agg))
f.close()