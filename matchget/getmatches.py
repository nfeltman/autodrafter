
import pprint
import dota2api
from multiprocessing import Pool
import os.path
import msgpack
import requests

api_key = "12"

api = dota2api.Initialise(api_key)

f = open('../4to6k.txt')
match_ids = f.read().split()
total = len(match_ids)
f.close()

def foo(x):
	index, match_id = x
	progress = "%8d of %d:" % (index,total)
	filename = '../games/game'+match_id+'.dat'

	if os.path.isfile(filename):
		print progress, 'Skipping    ', filename
	else:
		try:
			match = api.get_match_details(match_id=int(match_id))
			print progress, 'Writing out ', filename
			out = open(filename,'w')
			out.write(msgpack.packb(match))
			out.close()
		except ValueError:
			print progress, 'No JSON with', filename
		except requests.exceptions.RequestException:
			print progress, 'Request error with', filename

	return 0


p = Pool()
p.map(foo, enumerate(match_ids), 200)
p.close()