from urllib.parse import urlparse, parse_qs 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', type=argparse.FileType('r'))
#parser.add_argument('-o', help='Output file')
args = parser.parse_args()

p=[]
f=[]
for i in args.u.readlines():
	url=i
	parse_url= urlparse(url)
	params = parse_qs(parse_url.query)
	for j in params.keys():
		p.append(j)
f=(sorted(set(p)))
print(*f,sep="\n")

