from googleapiclient.discovery import build

api_key = 'AIzaSyAhgEI6eSn4hly9lp3wh1vvRjt3fDtV9Tk'
youtube = build('youtube', 'v3', developerKey= api_key)

def yt_searchtopic(topic, key=api_key, build_yt=youtube):

	request = youtube.search().list(
    part='snippet',
    maxResults=10,
    order='date',
    q=topic,
    relevanceLanguage='en')

	response = request.execute()	## stored as dictionary
	response_extracted = response['items']	## extract this key

	vids_urls = []
	for r in response_extracted[:]:
		vid_url = r['id']['videoId']	## 'videoId' location in each response dictionary'\
		vid_title = r['snippet']['title']

		vids_urls.append(['https://www.youtube.com/watch?v=' + vid_url,vid_title])
	return vids_urls

if __name__ == '__main__':
	topic = input('>> Insert topic: ')
	print(yt_searchtopic(topic))
