# imports
import configparser
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from datetime import datetime

# setting up timer
start_time = datetime.now()

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
errors = 0
post_total = 0
image_total = 0
links = []

while day > 5:
    # get all submissions from an account
    user_posts = client.get_account_submissions(config.get('users', 'target_user'), page=pagenum)

    for u_post in user_posts:
        try:
            images = client.get_album_images(u_post.id)


            # check if 'cropped is in post title'
            if 'cropped' in u_post.title.lower() or 'tasteful' in u_post.title.lower():


                # hacky bs to pull a number from the title don't think about it too much
                try:
                    day = int(''.join(filter(str.isdigit, u_post.title)))
                except ValueError:
                    day -= 1
                # print some info about the post
                print(f'Title: {u_post.title}')
                print(f'Link: {u_post.link}')
                print(f'Day number: {day}')
                print('Images:{')
                for image in images:
                    print(image.link)
                    links.append(image.link)
                    image_total += 1
                print('}')
                print(f'Item number: {item_num}')
                print(f'Page: {pagenum}')
                print(f'Errors: {errors}\n')

                item_num += 1

        except ImgurClientError as e:
            print('Oops, an error occured...')
            print('v______ERRORS______v')
            print(f'Error Message: {e.error_message}')
            print(f'Status code: {e.status_code}')
            print('Here\'s the link anyway :/')
            print(f'Link: {u_post.link}\n')
            errors += 1





    pagenum += 1
    #print(f'TESTING: {pagenum}')


print('\n\n\n\n---RESULTS---')
print(f'Total posts: {item_num}')
print(f'Total images: {image_total}')
print(f'Errors: {errors}\n\n\n\n')

print('Writing to file...')

file1 = open(r'links.txt', 'a')
for f_link in links:
    file1.write(f'{f_link}\n')
file1.close()

print(f'Finished in {datetime.now() - start_time}')



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
