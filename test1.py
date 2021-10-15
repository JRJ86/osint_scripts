# https://gist.github.com/UndergroundLabs/fad38205068ffb904685
# this github example said tokens are also necessary, but I found
# they were not needed
import requests
import json

# TODO: change to dummy cred
USERNAME = ''
PASSWORD = ''

# find some way to make the search a variable
PROTECTED_URL = 'https://www.facebook.com/search/top/?q=dennis'

def login(session, email, password):

    # Attempt to login to Facebook
    response_from_webserver = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    assert response_from_webserver.status_code == 302
    assert 'c_user' in response_from_webserver.cookies
    return response_from_webserver.cookies


if __name__ == "__main__":
    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
    response = session.get(PROTECTED_URL, cookies,
                           allow_redirects=False)
    assert response.text.find('Startside') != -1

    print(session.cookies)

    # to visually see if you got into the protected page, I recomend copying
    # the value of response.text, pasting it in the HTML input field of
    # http://codebeautify.org/htmlviewer/ and hitting the run button
