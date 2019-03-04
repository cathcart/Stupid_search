import io
from functools import reduce
import re
from argparse import ArgumentParser

class Parse:
	def __init__(self, data):


		self.index = {}

		for line in io.open(data, encoding="utf-8"):
			url = line.split(",")[0]
			title_dirty = ",".join(line.split(",")[1:])
			title = self.clean(title_dirty)
		
			#print(title.split())
			words = set(title.split())
			#print(title)
			for word in words:
				#print("\t%s: %d"%(word, title.count(word)))
				if word not in self.index.keys():
					self.index[word] = []
				count = title.count(word)
				self.index[word] += [(count, url[2:-1] )]


	def clean(self, input_line):
		title_1 = re.sub("\d","",input_line).lower()
		title_2 = re.sub("[.,\/#!$%\^&\*;:{}=\-_`~()|]","",title_1)
		title_3 = re.sub("^b","",title_2)
		title_4 = re.sub("'","",title_3)
		title = re.sub("\"","",title_4)
	
		return title

	def search(self, input_string):

		inputs = input_string.split()
		results_tmp = []
		for i in inputs:
			try:
				results_tmp += [self.index[i]]
			except KeyError:
				if len(inputs) == 1:
					return []
				else:
					pass

		if len(inputs) > 1:
			results = list(reduce(lambda x,y: set(x).intersection(set(y)), results_tmp[1:], results_tmp[0]))
		else:
			results = results_tmp[0]	

		results.sort(key=lambda x: x[0], reverse=True)
		return [x[1] for x in results]

if __name__ == "__main__":

	parser = ArgumentParser(description="Pull submmissions from a reddit subreddit")
	parser.add_argument("-f", "--file", dest="filename",
    	help="name of file to read submissions from", default="dump.csv")
	
	parser.add_argument("search_string", 
    	help="string to search dump for", nargs="+")

	args = parser.parse_args()
	
	print("Searching submission dump {filename}\nFor string {search_string}".format(**vars(args)))

	reddit = Parse(args.filename)

	search_string = " ".join(args.search_string)
	print(reddit.search(search_string))

