import instaloader
from instaloader import Instaloader, Post,Profile
L = instaloader.Instaloader()
hashtag = 'pilatesinstructor'
  
all_post = L.get_hashtag_posts(hashtag)     # (login)
for post in all_post:
	SHORTCODE = post.shortcode
	print(SHORTCODE)
	post = Post.from_shortcode(L.context, SHORTCODE)
	data= post.__dict__
	full_node_data = data['_node']
	user_details = full_node_data['owner']
	user_id = user_details['id']
	user_name =  user_details['username']
	user_full_name =  user_details['full_name']
	# total_edge_followed_by_count = edge_followed_by_count['count']
	print("hashtaghashtag________________",hashtag)
	print('user_id_________________________',user_id)
	print('user_name_________________________',user_name)
	print('user_full_name_________________________',user_full_name)
	from instaloader import Instaloader, Profile
	L = Instaloader()
	profile = Profile.from_username(L.context, user_name)
	data2 = profile.__dict__
	full_node_data = data2['_node']
	edge_followed_by_count = full_node_data['edge_followed_by']
	total_edge_followed_by_count = edge_followed_by_count['count']
	print('total_edge_followed_by_count_________________________',total_edge_followed_by_count)
