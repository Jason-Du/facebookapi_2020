import json
import download as d
import os
import re
# for dataset before 1020 you can use show function to list the post id
def get_json_from_cloud(date):
	d.main(is_download_file_function=bool(True), download_drive_service_name=(date+'.json'), download_file_path=os.getcwd() + '/')
	with open((date+'.json'), 'r', encoding='utf-8') as f:
		dataset = json.load(f)
	return dataset
def get_all_user_ids(dataset):
	'''
	:param dataset:dataset file from get_json_from_cloud
	:return: List for Facebook Club user id
	'''
	return dataset['member_info']

def show_all_posts(dataset):
	"""
	Show the content of all post
	:param dataset:dataset file from get_json_from_cloud
	"""
	for index, comment in enumerate(dataset['post_info']):
		print('post id:{}'.format(index))
		print(dataset['post_info'][index])


def get_posts_by_post_id(dataset, post_id):
	'''
	:param dataset:
	:param post_id:
	:return: Dict ;the specific post info according to the post id
	'''
	return dataset['post_info'][post_id]



def show_all_comments_by_post_id(dataset, post_id):
	'''
	:param dataset: dataset file from get_json_from_cloud
	:param post_id:
	:return: NONE
	'''
	for index, comment in enumerate(dataset['post_info'][post_id]['comment']):
		print('post id :{} comment id:{}'.format(post_id, index))
		print(comment)



def get_all_main_comments_by_post_id_comment_id(dataset, post_id,comment_id):
	'''

	:param dataset:
	:param post_id:
	:param comment_id:
	:return:
	'''
	match_list=[]
	for single_comment in dataset['post_info'][post_id]['comment']:
		pass
		search_standard=re.match(comment_id,str(single_comment['comment_id']))
		if (search_standard!=None):
			match_list.append(single_comment)
			pass
	return match_list

def get_all_below_comments_by_post_id_comment_id(dataset, post_id, comment_id):
	match_list=[]
	for single_comment in dataset['post_info'][post_id]['comment']:
		for single_below_comment in single_comment['comment_below']:
			search_standard2 = re.match(comment_id, str(single_below_comment['comment_id']))
			if (search_standard2 != None):
				match_list.append(single_below_comment)
				pass
	return match_list

def get_all_posts_by_type(dataset,type):
	match_list=[]
	if type=='Q&A':
		pattern = '\[ Q&amp;A'
	else:
		pattern='\[ '+type
	# pattern=r'{}'.format(label)
	for single_post in dataset['post_info']:
		search_standard=re.match(pattern,str(single_post['post_content']))
		if (search_standard!=None):
			match_list.append(single_post)
			pass
	return match_list



if __name__ == '__main__':
	# pass
	# dataset = get_json_from_cloud(date="1020")
	with open(('1020' + '.json'), 'r', encoding='utf-8') as f:
		dataset = json.load(f)
	# post_list=get_all_posts_by_type(dataset=dataset,type='Q&A')

	# print(get_user_id(dataset=dataset))
	# comment_list=get_all_main_comments_by_post_id_comment_id(dataset=dataset,post_id=1,comment_id='葉羿亭')
	comment_list = get_all_below_comments_by_post_id_comment_id(dataset=dataset, post_id=1, comment_id='葉羿亭')
	print(comment_list)
