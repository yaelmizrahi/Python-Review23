#2
def create_youtube_video(title, description):
	
	youtubeVid = {
	"title" : title,
	"description": description,
	"likes" : 0,
	"dislikes" : 0,
	"comments" : {}
	}

	return youtubeVid
#3
def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video
#4
def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video
#5
def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo


#6 testing 
test = create_youtube_video("cool", "hey")

like(test)
print(test["likes"])
dislike(test)
print(test["dislikes"])
add_comment(test, "nice", "i love the vid")

#495 likes
for x in range(495):
	like(test)



