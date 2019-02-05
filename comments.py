from urllib.request import urlopen
import json
import pandas as pd
link= "https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyA3iMXsV9CeY30qCB0fYb3UGOuhwT9scJI&textFormat=plainText&part=snippet&videoId=GlqqGKZ3Uac&maxResults=100"

def gen_com(x):
    f=urlopen(x)
    myfile=f.read()
    parsed = json.loads(myfile)
    comment_list=[]
    comment_items=parsed['items']
    for item in comment_items:
        comment=item['snippet']['topLevelComment']['snippet']['textDisplay']
        comment_list.append(comment)
    return comment_list

#print(gen_com(link))
#print(type(comment_list))
hmm=gen_com(link)
df = pd.DataFrame({'comments':hmm})
print (df)
