import tweepy,time,gdown,sys
import numpy as np
import cv2 as cv

# keys
api_key = "XXX"
api_key_secret = "XXX"
bearer_token = "XXX"
access_token = "XXX"
access_token_secret = "XXX"
client_id = "XXX"
client_secret = "XXX"

# Tweepy Setup
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Set default
season = 1
total_episode = 1
episode = 1
#Reading urls from text file
url_list = open(R"all_urls.txt","r")
Lines = url_list.readlines()

#Pulling Video from google drive
for Line in Lines:
    google_drive_url = Line
    output_file = "current_video"
    id = google_drive_url.split('/')[-2]
    gdown.download(f"https://drive.google.com/uc?id={id}", output_file)

    #Downloads all the frames of a video (1 fps video)
    capture = cv.VideoCapture("C:/Users/Bhaar/Documents/Code/ygoframes/current_video.mp4")
    count = 1
    while(True):
        success, frame = capture.read()
        if success and count % 24 == 0: 
            cv.imwrite(f"C:/Users/Bhaar/Documents/Code/ygoframes/current_video_frames/{count / 24}.jpg", frame)
        else:
            break
        count += 1
    capture.release()

    #setup episode for caption
    count = count / 24
    count2 = 1
    while count2 < count:
        caption_text = "Yu-Gi-Oh! Duel Monsters - Season {season} Episode {episode} - Frame {count2} of {count}"
        client.create_tweet(text = caption_text, media="C:/Users/Bhaar/Documents/Code/ygoframes/current_video_frames/{count2}.jpg")
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