import feedparser

def link_container():
	"""
	container for links
	Input:
	Output: links data
	"""
	links = ['https://www.reddit.com/r/Python/.rss', \
			'https://www.reddit.com/r/MachineLearning/.rss']
	return links

def link_seg(links):
	"""
	segregates the link the in the link structure
	INPUT: RSS links list
	OUTPUT: feeds of the link in the RSS links list
	"""
	d = []
	for link in links:
		d.append(feedparser.parse(link))
	return d

def channel_details(feeds):
	"""
	Prints the channel details
	Input: feed of the channels
	"""
	#Channel elements
	for d in feeds:
		#print(d['feed']['title'])
		print('\n')
		print('*'*50)

		try:
			print('RSS feeds for the link {l}'.format(l = d.feed.link))
		except AttributeError:
			print('##Attribute Link Not Available')

			print('_'*50)
			print('Channel Details:\n')

		try:
			print('Title: '+d.feed.title)
		except AttributeError:
			print('##Attribute Title Not Available')

		try:
			print('Link: '+d.feed.link)
		except AttributeError:
			print('##Attribute Link Not Available')

		try:
			print('Description: '+d.feed.description)
		except AttributeError:
			print('##Attribute Description Not Available')

		try:
			print('Updated on: '+d.feed.updated)
		except AttributeError:
			print('##Attribute Updated Not Available')

		finally:
			print('\n')
			print("Today's Top Feeds!")
			item_details(d)
			#print(d.feed.published)



def item_details(d):
	"""
	post details in the channel
	Input: feeds
	Output: post details in a channel
	"""
	print("\n")
	for i in range(0,len(d.entries)-1):
		try:
			print((d.entries[i].title).encode('utf-8'))
		except AttributeError:
			print('## Attribute Title Not Available')
		try:
			print("Author: "+d.entries[i].author)
		except:
			print('##Attribute Author Not Available')


def driver():
	"""
	main program to run this code
	Input:
	Output:
	"""
	links = link_container()
	feeds = link_seg(links)
	channel_details(feeds)
	#item_details(feeds)




if __name__ == '__main__':
	driver()
