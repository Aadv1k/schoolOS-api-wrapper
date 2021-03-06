import requests as req
import json
import pickle
import os


class schoolOS:
    def __init__(self, ecode: str, pwd: str, group: str = 'ryangroup') -> None:
        """
        The main schoolOS class.

        Attributes
        ----------
        ecode: str
            the student enrollment code
        pwd: str
            the student password
        group: str
            The url name of the school {group}.toppr.school

        Methods
        -------
        get_sessionID() -> String
            returns the `session_id` token used for authentication
        get_token() -> String
            returns a jwt token generated using the `session_id`, used for
            accessing the data
        get_timetable(start: str, end: str) -> dict
            returns the weekly schedule based on the start_date and end_date
        get_assignments(complete: bool, quantity: int) -> dict
            returns `n` complete/incomplete assignments based on the quantity.

        """

        self.ecode = ecode
        self.pwd = pwd
        self.baseURL = f'https://{group}.toppr.school/'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'

    def get_sessionID(self):
        """Returns an auth cookie called `admin_sessionid`"""
        headers = {
            'User-Agent': self.userAgent,
            "origin": "https://ryangroup.toppr.school",
        }

        pl = {'ecode': self.ecode, 'password': self.pwd}

        url = f'{self.baseURL}schoolApi/api/v1/authentication/ecode-login/'
        session = req.Session()
        try:
            resp = session.post(url, headers=headers, data=pl)
            f_resp = resp.cookies.get_dict()
            return f_resp['admin_sessionid']
        except ValueError:
            print('Invalid credentials or corrupted file, delete the file and try again.')

    def get_token(self):
        """
        Uses the auth cookie `admin_sessionid` to generate a jwt token;
        Checks if a file called jwt_token exists, if it does then reads from
        that else create a new file called jwt_token and puts the token in it,
        This is dont to prevent rate limiting.

        Returns:
        a token string
        """
        session_id = self.get_sessionID()
        cookie = f'admin_sessionid={session_id};'
        token_url = f'{self.baseURL}api/v1/schools/get-jwt-token/'
        tk_headers = {'user-agent': self.userAgent, 'cookie': cookie}

        if os.path.isfile('jwt_token'):
            with open('jwt_token', 'rb') as pkl:
                token_data = pickle.load(pkl)
                token = json.loads(token_data)['token']
                pkl.close()
                return token

        else:
            token_request = req.get(token_url, headers=tk_headers).json()
            token = token_request['data']['token']

            with open('jwt_token', 'ab') as pkl:
                token_str = {
                    'token':
                    f'token {token}'
                }
                token_dict = json.dumps(token_str)
                pickle.dump(token_dict, pkl)
                pkl.close()

            with open('jwt_token', 'rb') as pkl:
                token_data = pickle.load(pkl)
                token = json.loads(token_data)['token']
                pkl.close()
                return token

    def get_timetable(self, start: str, end: str) -> dict:
        """Gets the weekly scheduled classes.

        Parameters:
        start (string): This is the start date, it must only be sundays in the yyyy-mm-dd format
        end (string): This is the end date, this date must only be saturdays in the yyyy-mm-dd format

        Returns:
        A python dictionary
        """

        jwt_token = self.get_token()
        tt_url = 'https://paathshala.toppr.school/api/v1.1/lectures/?group_by=day_of_week_and_start_time&user_type=student&start_date={start}&end_date={end}&add_student_attendance=true&add_lecture_media=true'.format(
            start=start, end=end)

        headers = {
            "authorization": jwt_token,
            "origin": self.baseURL,
            "user-agent": self.userAgent,
            "view-type": "student"
        }

        tt_request = req.get(tt_url, headers=headers).json()
        return tt_request

    def get_assignments(self, complete: bool, quantity: int) -> dict:
        """Gets `n` assignments

        Parameters:
        complete (bool): Specifies the type of assignment
        quantity (int): The quantity of assignments to be fetched, must be a multiple of 10

        Returns:
        A python dictionary
        """
        jwt_token = self.get_token()
        headers = {
            "authorization": jwt_token,
            "origin": self.baseURL,
            "user-agent": self.userAgent,
            "view-type": "student"
        }

        if quantity:
            base_a_url = f'https://paathshala.toppr.school/api/v1/homeworks/student/?page=1&page_size={quantity}&section='
        else:
            base_a_url = 'https://paathshala.toppr.school/api/v1/homeworks/student/?page=1&page_size=5&section='

        if complete == True:
            a_url = base_a_url + 'completed&view_type=student'
        else:
            a_url = base_a_url + 'pending_expired&view_type=student'

        a_request = req.get(a_url, headers=headers).json()
        return a_request
