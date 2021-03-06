import sys
import json
import pafy
import numpy as np
sys.path.append("C:/Users/Atharva/Desktop/My stuff/BE PROJ/cce try/try/")
from youtube_videos import youtube_search, geo_query
from comments import gen_com
from sentiment import calculate_sentiment
import pandas as pd
key='AIzaSyA3iMXsV9CeY30qCB0fYb3UGOuhwT9scJI'
#key='AIzaSyB7z8IBhtBjMSbecRUReL2g2CJwapc1NHM'
pafy.set_api_key(key)

#youtube=get_authenticated_service(args)
def get_search_results(x):
    #x=input("enter search term here: ")
    results=youtube_search(x)
    #type(results)
    #print(results)
    just_json=results[1]
    #print(just_json)
    #print(type(just_json))
    dump_list=json.dumps(just_json)
    parsed=json.loads(dump_list)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    
    raw_df=[]
    for data in just_json:
        raw_df.append(data['id']['videoId'])
    df=pd.DataFrame(raw_df,columns=['VideoId'])
    #df.to_csv('videoid.csv')
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
    
    video_links=[]
    
    def create_url(vidid):
        return "https://www.youtube.com/watch?v="+(vidid)
    
    title_list=[]
    author_list=[]
    likes_list=[]
    dislikes_list=[]
    videoid_list=[]
    viewcount_list=[]
    for i in range(10):
        video=pafy.new(create_url(raw_df[i]))
        title_list.append(video.title)
        likes_list.append(video.likes)
        dislikes_list.append(video.dislikes)
        author_list.append(video.author)
        viewcount_list.append(video.viewcount)
        videoid_list.append(video.videoid)
        video_links.append(create_url(video.videoid))
    #df=pd.DataFrame(data={'Title':title_list,'Author':author_list,'VideoID':videoid_list,'View Count':viewcount_list,'Likes':likes_list,'Dislikes':dislikes_list})
    #print(df.head())
    
    def gen_link(id):
    	s="https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyA3iMXsV9CeY30qCB0fYb3UGOuhwT9scJI&textFormat=plainText&part=snippet&videoId="+id+"&maxResults=100"
    	return s
    
    #exc=geo_query('EmTz7EAYLrs')
    #print(exc)
    
    comment1_list=[]
    links=[]
    new_comms=[]
    sentiment_value=[]
    for id in videoid_list:
        link_test= gen_link(id)
        links.append(link_test)
    
    for ahaha in links:
        comment1_list.append(gen_com(ahaha))
       
        
    for comments in comment1_list:
        video=[]
        for comment in comments:
            video.append(calculate_sentiment(comment))
        sentiment_value.append(np.mean(video))
    
    
    #df=pd.DataFrame(data={'Title':title_list,'Author':author_list,'VideoID':videoid_list,'View Count':viewcount_list,'Likes':likes_list,'Dislikes':dislikes_list, 'Comments':comment1_list, 'Sentiment':sentiment_value})
    df=pd.DataFrame(data={'Link':video_links ,'Title':title_list, 'View Count':viewcount_list,'Likes':likes_list,'Dislikes':dislikes_list,'Sentiment':sentiment_value})
    #df.to_csv('try.csv')
    return df