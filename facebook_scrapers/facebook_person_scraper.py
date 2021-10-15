import json
from http import cookies

import facebook_scraper
from facebook_scraper import get_posts, write_posts_to_csv, get_group_info, get_page_info
import locale

name = ""

cookie = facebook_scraper.set_cookies("cookies_jvallinger.json")


