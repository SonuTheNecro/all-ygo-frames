import tweepy,time,gdown,sys
import numpy as np
import cv2 as cv
import subprocess
import os
from dotenv import load_dotenv
# keys

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
bearer_token = os.getenv("bearer_token")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
""""
# Tweepy Setup
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)
"""

#Set default
season = 1
total_episode = 1
episode = 1

while(True):
    #Runs animdl to download a single episode
    subprocess.run(["animdl download 'Yu-Gi-Oh! -r {total_episode} -d C:/Users/Bhaar/Documents/Code/ygoframes/current_video"])

    #Converts the video into frames
    capture = cv.VideoCapture('{:02d}.mp4'.format(total_episode))
    count = 1
    success, frame = capture.read()
    while(success):
        if success and count % 24 == 0: 
            cv.imwrite(f"C:/Users/Bhaar/Documents/Code/ygoframes/current_video_frames/{count / 24}.jpg", frame)
        success, frame = capture.read()
        count += 1
    capture.release()

    os.remove('{:02d}.mp4'.format(total_episode))
    #setup episode for caption
    count = count / 24
    count2 = 1
    while count2 < count:
        caption_text = "Yu-Gi-Oh! Duel Monsters - Season {season} Episode {episode} - Frame {count2} of {count}"
        #client.create_tweet(text = caption_text, media="C:/Users/Bhaar/Documents/Code/ygoframes/current_video_frames/{count2}.jpg")
        print(caption_text)
        count2 +=1
        time.sleep(1800)
    
    total_episode +=1
    episode += 1
    #s1 1-49, s2 50-97, s3 98 - 144, s4 145 - 184, s5 185 - 224
    match total_episode:
        case 50:
            season = 2
            episode = 1
        case 98:
            season = 3
            episode = 1
        case 145:
            season = 4
            episode = 1
        case 185:
            season = 5
            episode = 1