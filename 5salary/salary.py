import random
import json


class Cash:
    def __init__(self, size=12):
        self.cash = {}
        self.size = size

    def get(self, id):
        return self.cash.get(id)

    def add(self, id, val):
        if id in self.cash.keys():
            pass
        elif len(self.cash) < self.size:
            self.cash[id] = val
        else:
            it = iter(self.cash)
            self.cash.pop(next(it))
            self.cash[id] = val


class WorkdayNum:
    def get(self):
        return random.randint(20, 23)


class Salary:
    def __init__(self, cash_size=12):
        self.cash = Cash(cash_size)

    def get(self, json_string):
        json_dict = json.loads(json_string)
        date_key = str(json_dict['year']) + json_dict['month'].strip()
        sal = int(json_dict['salary'])

        if self.cash.get(date_key):
            json_dict['hour_income'] = self.cash.get(date_key)
            return json.dumps(json_dict)
        else:
            w_days = WorkdayNum().get()
            hour_income = '{:.2f}'.format(sal/(w_days*8))
            self.cash.add(date_key, hour_income)
            json_dict['hour_income'] = hour_income
            return json.dumps(json_dict)
