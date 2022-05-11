""" URL """

import requests

resp = requests.get("https://wikipedia.org")

print(resp.status_code)

# _______________________________________________________
#
# #  build the url https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
#
# qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"
#
# from urllib import parse
#
# params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
# querystring = parse.urlencode(params)
# url = "https://www.youtube.com/watch" + "?" + querystring
#
# resp = request.urlopen(url)
#
# print(resp.isclosed())  # False means that we have a connection with the server
#
# print(resp.code)  # Means the request was fulfilled
