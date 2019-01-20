import sys
import json
sys.path.append("C:/Users/Atharva/Desktop/My stuff/BE PROJ/cce try/try/")
from youtube_videos import youtube_search
import json
import pandas as pd
x=input("enter search term here: ")
results=youtube_search(x)
#print(results)
just_json=results[1]
#print(just_json)
#print(type(just_json))
dump_list=json.dumps(just_json)
parsed=json.loads(dump_list)
print(json.dumps(parsed, indent=4, sort_keys=True))

raw_df=[]
for data in just_json:
    raw_df.append(data['id']['videoId'])
df=pd.DataFrame(raw_df,columns=['VideoId'])
df.to_csv('videoid.csv')
#for video in just_json:
	#print (video['snippet']['title'])

#token=results[0]
#videos=results[1]

#video_dictionary={'Id':[], 'title':[] }
'''
def grab_video(search_term, token=None):
	results= youtube_search(search_term)
	token=results[0]
	videos=results[1]

	for vids in videos:
		video_dictionary['Id'].append(vids['id']['videoId'])
		video_dictionary['title'].append(vids['snippet']['title'])

	return token

token=grab_video(x)
while token != "last_page":
	token=grab_video(x, token=token)
'''
'''
for vids in videos:
		video_dictionary['Id'].append(vids['id']['videoId'])
		video_dictionary['title'].append(vids['snippet']['title'])
'''





