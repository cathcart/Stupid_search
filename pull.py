import io
import praw
from argparse import ArgumentParser

parser = ArgumentParser(description="Pull submmissions from a reddit subreddit")
parser.add_argument("-f", "--file", dest="fileout",
    help="name of file to save submissions to", default="dump.csv")
parser.add_argument("-s", "--subreddit", dest="subreddit",
    help="input subreddit to parse", default="worldnews")
parser.add_argument("-n", "--number", dest="number",
    help="number of submissions to pull", default=100, type=int)
#parser.add_argument("-n", "--number", dest="number",
#    help="number of submissions to pull", default=100)

args = parser.parse_args()

name = "Test pull app"
my_id = "hh4uW2E9HSg_Gw"
secret = "Ky5QeJY3FZzHjgrw-Whso1JrPwQ"

reddit = praw.Reddit(client_id=my_id,
                     client_secret=secret,
                     user_agent='my user agent')

#print(reddit.read_only) 

#print("Gathering data from %s\nOutput to %s"%(options.subreddit, options.fileout, options.))
print("Gathering data from {subreddit}\nOutput to {fileout}\nLimited to {number} submissions".format(**vars(args)))

file_out = args.fileout
out = io.open(file_out,"w", encoding="utf-8")

#for submission in reddit.subreddit('learnpython').hot(limit=10):
#for submission in reddit.subreddit(args.subreddit).top(limit=args.number):
for submission in reddit.subreddit(args.subreddit).hot(limit=args.number):
#for submission in reddit.subreddit('worldnews').hot(limit=10000):
#for submission in reddit.front.hot(limit=10):
    #line = "%s,%s\n" % (submission.url,submission.title.encode('ascii','ignore'))
    line = "%s,%s\n" % (submission.url.encode('utf-8'),submission.title.encode('utf-8'))
    #line = "%s,%s\n" % (submission.url.encode('ascii', 'ignore'),submission.title.encode('ascii','ignore'))

    out.write(line)
out.close()
