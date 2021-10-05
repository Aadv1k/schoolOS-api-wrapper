import requests as req
import json 
import os

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"

def get_token(cookie):
    token_url = 'https://ryangroup.toppr.school/api/v1/schools/get-jwt-token/'

    tk_headers = {
            'user-agent': useragent,
            'cookie': cookie
        }

    # Checks if the file exists, if it does then reads the file, else creates a new token and file
    if os.path.isfile('jwt_token.json'): 
        print('Reading from file')
        try: 
            with open('jwt_token.json', 'r') as jj : 
                token = 'token ' + json.loads(jj.read())
                return token
        except: 
            print('File empty or corrupted, getting another token and recreating the file')
            token_request = req.get(token_url, headers=tk_headers).json()
            with open('jwt_token.json', 'w') as jt: 
                json.dump(token_request['data']['token'], jt)
            with open('jwt_token.json', 'r') as ur:
                token = 'token ' + json.loads(ur.read())
                return token
    else: 
        print('File not found, creating a new file')
        token_request = req.get(token_url, headers=tk_headers).json()
        with open('jwt_token.json', 'w') as jt: 
            json.dump(token_request['data']['token'], jt)
        with open('jwt_token.json', 'r') as ur:
            token = 'token ' + json.loads(ur.read())
            return token



# gets the timetable view, takes jwt-token, a start date and an end date 
# The date needs to be in yyyy-mm-dd format
# the start and end date NEED to be sunday-saturday, else it wont accept
def get_timetable(cookie, token, start, end):
        tt_url = 'https://paathshala.toppr.school/api/v1.1/lectures/?group_by=day_of_week_and_start_time&user_type=student&start_date={start}&end_date={end}&add_student_attendance=true&add_lecture_media=true'.format(start=start, end=end)
        headers={
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'Authorization': token,
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': useragent,
            'view-type': 'student',
            'origin': 'https://ryangroup.toppr.school',
        }
        tt_request = req.get(tt_url, headers=headers).json()
        try:
            if tt_request['data']['groups']:
                return tt_request

            elif tt_request['detail'] == "Invalid jwt token.":
                os.remove('jwt_token.json')
                token=get_token(cookie)
                headers={
                    'accept': 'application/json',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'Authorization': token,
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': useragent,
                    'view-type': 'student',
                    'origin': 'https://ryangroup.toppr.school',
                }
                tt_request = req.get(tt_url, headers=headers).json()
                return tt_request
        except:
                os.remove('jwt_token.json')
                token=get_token(cookie)
                headers={
                    'accept': 'application/json',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'Authorization': token,
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': useragent,
                    'view-type': 'student',
                    'origin': 'https://ryangroup.toppr.school',
                }
                tt_request = req.get(tt_url, headers=headers).json()
                return tt_request


# Gets assignmnets, by default gives out pending/expired, however if c=True then gives out completed assignments
# Complete True, False: Gets either pending, or complete assignments  
# Quantity Any multiple of 5, if the value is too high or low, default is given
def get_assignments(token, complete=bool, quantity=int): 
    headers = {
        'user-agent': useragent,
        'Authorization': token,
    }

    if quantity:
        base_a_url=f'https://paathshala.toppr.school/api/v1/homeworks/student/?page=1&page_size={quantity}&section='
    else:
        base_a_url='https://paathshala.toppr.school/api/v1/homeworks/student/?page=1&page_size=5&section='
    if complete==True: 
        a_url = base_a_url + 'completed&view_type=student'
    else:
        a_url = base_a_url + 'pending_expired&view_type=student'
    a_request = req.get(a_url, headers=headers).json()
    return json.dumps(a_request)

