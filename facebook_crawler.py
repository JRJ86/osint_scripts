# crawl = "https://api.proxycrawl.com/?token=TzXQJplb2UWQa9E52ke65Q&url=https%3A%2F%2Fwww.facebook.com%2Fgroups
#          %2F198722650913932&scraper=facebook-group&scroll=true"

from proxycrawl.proxycrawl_api import ProxyCrawlAPI

# Max 2000 API calls from the free version of ProxyCrawler
# Login:
#       jrj@eagleshark.dk
#

api = ProxyCrawlAPI({'token': 'TzXQJplb2UWQa9E52ke65Q'})

response = api.get('https://www.facebook.com/groups/381067052051677',
                   {'scraper': 'facebook-group',
                    'scroll': 'true'})


if response['status_code'] == 200:
    print(response['body'])

else:
    print("Fail")
