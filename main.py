# imports
import configparser
from imgurpython import ImgurClient
import time


# setting config parser
config = configparser.ConfigParser()
config.read('auth.ini')



# setting imgur credentials
client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')
client = ImgurClient(client_id, client_secret)

# oops bad variables
day = 999
item_num = 0
pagenum = 0

while day > 0:
    # get all submissions from an account
    user_posts = client.get_account_submissions(config.get('users', 'target_user'), page=pagenum)
    for u_post in user_posts:

        # check if 'cropped is in post title'
        if 'Cropped' in u_post.title:

            # hacky bs to pull a number from the title don't think about it too much
            day = int(''.join(filter(str.isdigit, u_post.title)))

            # print some info about the post
            print(f'Title: {u_post.title}')
            print(f'Link: {u_post.link}')
            print(f'Day number: {day}')
            print(f'Item number: {item_num}')
            print(f'Page: {pagenum}\n')

            # this needs to be redone but works in a proof of concept
            item_num += 1
            if item_num == 15:
                item_num = 0
                pagenum += 1
            # sleep time to make it look cool
            #time.sleep(0.1)








# items = client.gallery() #get all posts on the front page
# for item in items: #print the link, title, and views of each post on the front page
#     print(item.link)
#     print(item.title)
#     print(item.views)



# find the item on the front page with the most views
# max_item = None
# max_views = 0
# for item in items:
#     if item.views > max_views:
#         max_item = item
# print(max_item.points)
# print(max_item.title)
# print(max_item.link)
# print(max_item.views)
# print(max_item.account_url)
# print(max_item.vote)

# random_items = client.gallery(section='hot', sort='random', page=0, window='day', show_viral=True)
# for rand_tiem in random_items:
#     print(rand_tiem.title)
#     print(rand_tiem.link)
#     print(rand_tiem.id)
