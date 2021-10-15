import json
import requests
from facebook_scraper import get_posts, write_posts_to_csv, get_group_info, get_page_info
import facebook

access_token = 'EAAMi1YIWPXMBACZBm3RS7f6ZC69QpTSZAp0eedIAr8xn4l8n4k8AXYFZBizqQYX45YspmV33AkFpbXYKwfByC1h56RxiTVCWz7' \
               'YpEovkr0ZCZBHb4RSNZBnYsZAyxPySnbsZAxrXEu6piHmk3uBRwRTuCCCwEp5ZBsmsKm8WKleCGF4ImZBTnEo6V1QZBT06505DZBD' \
               'gk4etEIGeZAZAWBhIfuWxuhCZB4j3KNNPvWy7RBVdnjVfi76XC0vThB4rvMQRSCOZCAz4ZD'
facebook_url = "https://www.facebook.com/search/top/?q=dennis"
facebook_login_url = "https://m.facebook.com/login.php"
headers = {'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 "
                         "(KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3 "}
login_credentials = {'email': 'jvallinger@hotmail.com', 'pass': "joejoe123456789"}
query = 'fishing'
search_type = 'page'

session = requests.session()
response = session.post(facebook_login_url, data=login_credentials, headers=headers)

# see if the response from the login server has status code 302
assert response.status_code == 200

# see if the user is in the cookies
# assert 'c_user' in response.cookies

if response.status_code != 200:
    print("Not logged in!")

else:
    print("Logged in!")
    # print(response.text)
    # print(response.content)

    # data = requests.get("https://graph.facebook.com/search?access_token="
    #                   "" + access_token + "&q=" + query + "&type=" + search_type)
    # print(data.content)

    # TODO NOT WORKING YET
    # fb = facebook.GraphAPI(access_token=access_token, version='3.1')
    # search = fb.search( q='aquafresh',
    #      type='place')

    # "print(search['data'])



