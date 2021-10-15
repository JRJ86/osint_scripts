import json
from http import cookies

import facebook_scraper
from facebook_scraper import get_posts, write_posts_to_csv, get_group_info, get_page_info
import locale

# https://pypi.org/project/facebook-scraper/
# If you do not use a vpn, facebook will block the call, and the credentials parameter does not seem to work
# The cookie parameter works:
#       - install: Quick Cookie Manager extension on Firefox, and make a file.json in the directory of this code
#         and make a json with the c_user and xs parameters from the facebook login on firefox browser

# login information TODO: Use this for something!
username = 'jvallinger@hotmail.com'
password = 'joejoe123456789'

# The group you want to scrape
group_public = "lystfiskeri"
group_private = "1983380875131654"

# Name you want to scrape info posts from!
name = ""
# txt file to write to
file_txt = "posts.txt"
# csv file to write to
file_csv = "posts.csv"
# json file to writ to
file_json = "posts.json"

i = 1

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

cookie = facebook_scraper.set_cookies("cookies_jacob.json")

group_info = get_group_info(group_private, cookies=cookie)
print(json.dumps(group_info, indent=3))

# TODO: maybe use pages instead og page_limit
for post in get_posts(group=group_private,
                      options={"comments": True, "reactors": True, "posts_per_page": 200},
                      pages=40, cookies=cookie, extra_info=True):
    print(post['username'])
    print(post["time"])
    print(post['text'])
    print(post['likes'])
    print(post['reactions'])
    print(post['shares'])
    print(post['comments'])
    print(post['post_url'])
    print("\n\n")

    with open("posts.json", "a", encoding="utf-8") as f:
        f.write("Post " + str(i or 'cant show')
                + " from user: " + post['username'] + " ( " + str(post['time'] or 'cant show') + " ): \n"
                + post['text'] + "\n"
                + "likes: " + str(post['likes'] or 'cant show') + ", Where the different reactions are: "
                + str(post['reactions'] or 'cant show')
                + "\n"
                + "Amount of comments for this post: " + str(post['comments'] or 'cant show') + "\n"
                + "Shares: " + str(post['shares'] or 'cant show') + "\n"
                + "Post URL: " + str(post['post_url'] or 'cant show') + "\n\n")

    i = i + 1

    print("Post " + str(i)
          + " from user: " + post['username'] + " ( " + (str(post['time'])) + " ): \n"
          + post['text'] + "\n"
          + "likes: " + (str(post['likes'])) + ", Where the different reactions are: " + str(post['reactions'])
          + "\n"
          + "Amount of comments for this post: " + str(post['comments']) + "\n"
          + "Shares: " + str(post['shares']) + "\n"
          + "Post URL: " + str(post['post_url']) + "\n\n")

f.close()
