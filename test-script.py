import topprApiWrapper as taw
import requests
import json

cookie = 'your cookie goes here'
token = taw.get_token(cookie)

tt_d = taw.get_assignments(token)
print(tt_d)



