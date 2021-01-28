import requests
import json
from datetime import datetime


class WatchAgent:
    def __init__(self,start_date, end_date, start_time, end_time):
        self.start_date = self.refactorDate(start_date)
        self.end_date = self.refactorDate(end_date)
        self.start_time = start_time
        self.end_time = end_time
        self.start_watch = '{}T{}'.format(self.start_date, self.start_time)
        self.end_watch = '{}T{}'.format(self.end_date, self.end_time)
        self.match_list = []

    def requestMatches(self):
        PARAMS = {'tenant_id': '618d8202-788b-429e-9a57-4cbd4e0b9144', 'from_start_date':self.start_watch, 'to_start_date':self.end_watch}
        URL = 'https://api.playtomic.io/v1/matches'

        receive = requests.get(url=URL, params=PARAMS).json()
        match_cancel_list = []

        if not self.match_list:
            self.match_list = self.createMatchList(receive)
        else:
            match_cancel_list = [i for i in self.createMatchList(receive) if 'CANCEL' in i['status']]

            for match in match_cancel_list:
                match_id = match['match_id']
                match_to_check = (i for i in self.match_list if i[0] == match_id)
                if match_to_check['status'] == match['status']:
                    pass
                else:
                    print("Match (id: {}) has been cancelled!".format(match_id))
                    return match
                    
    def refactorDate(self, d):
        year = datetime.date.today().year
        day, month = d.split('.')

        # format 'yyyy-mm-dd' needed for HTTP requests
        date = '{}-{}-{}'.format(year, month, day)
        try:
            # refactor date to have zeroes if not two digit number
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print('Date was not in correct format (yyyy-mm-dd')
        else:
            return date.date()

    def refactorTime(self, t):
        hour, minute = t.split('.')
        second = '00'

        # format 'hh:mm:ss' needed for HTTP requests
        time = '{}:{}:{}'.format(hour, minute, second)
        try:
            # refactor time to have zeroes if not two digit number
            time = datetime.strptime(time, '%H:%M:%S')
        except ValueError:
            print('Time was not in correct format (hh:mm:ss')
        else:
            return time.time()

    def createMatchList(self, data):
        list = []
        for match in data:
            match_id = match['match_id']
            status = match['status']
            start = match['start_date']
            end = match['end_date']
            list.append((match_id, status, start, end))

        return list