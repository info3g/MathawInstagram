#version is reuired :   pip install instaloader==3.0rc1
import instaloader
import pandas as pd
from instaloader import Instaloader, Post
import csv,time
hashtag = 'pilatesinstructor'
L = instaloader.Instaloader(sleep=True, quiet=False, user_agent=None, dirname_pattern=None, filename_pattern=None)

row1 = ['Hashtag', 'Username', 'User Full Name', 'User Id', 'Follower']
with open('pilatesinstructor__result.csv','w',newline='', encoding='utf-8') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(row1)

rows = []
all_tags = []
with open('datafile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       rows.append(row[0])
for tags in rows:
	tags_split = tags.split("https://www.instagram.com/explore/tags/")
	try:
		tags_splits = tags_split[1].split("/")[0]
		all_tags.append(tags_splits)
	except:
		pass

print(all_tags)
try:
	for one_tags in all_tags:
		try:
			all_post = L.get_hashtag_posts(one_tags)
			time.sleep(20)
			counts = 0
			for tags in all_post:
				try:
					SHORTCODE = tags.shortcode
					print("SHORTCODE************************************",counts,"--------------------",SHORTCODE)
					time.sleep(20)
					post = Post.from_shortcode(L, SHORTCODE)
					data= post.__dict__
					full_node_data = data['_node']
					user_details = full_node_data['owner']
					edge_followed_by_count = user_details['edge_followed_by']
					user_id = user_details['id']
					user_name =  user_details['username']
					user_full_name =  user_details['full_name']
					total_edge_followed_by_count = edge_followed_by_count['count']
					print("hashtaghashtag________________",hashtag)
					print('user_id_________________________',user_id)
					print('user_name_________________________',user_name)
					print('user_full_name_________________________',user_full_name)
					print('total_edge_followed_by_count_________________________',total_edge_followed_by_count)
					counts = counts + 1
					row = [hashtag, user_name, user_full_name, user_id, total_edge_followed_by_count]
					with open('pilatesinstructor__result.csv','+a',newline='', encoding='utf-8') as csvFile:
						writer = csv.writer(csvFile)
						writer.writerow(row)
					time.sleep(43)
				except:
					pass
		except:
			pass
except:
	pass
			