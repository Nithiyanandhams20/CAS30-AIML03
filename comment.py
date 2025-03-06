from googleapiclient.discovery import build
import pandas as pd

API_KEY = "AIzaSyA7WrJ9_kDuS_iCgXpFCf1v5ADRQ1pvEuc"

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_video_comments(video_id, max_results=50):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    
    response = request.execute()

    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]
        comments.append({
            "comment_id": item["id"],
            "author": comment["authorDisplayName"],
            "text": comment["textDisplay"],
            "like_count": comment["likeCount"],
            "published_at": comment["publishedAt"]
        })
    
    return comments
