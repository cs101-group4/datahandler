import json

class Schedule:
    def __init__(self):
        self.schedule_list = []

    def get_schedule_json(self):
        """
        返回包含所有日程的JSON
        """
        return json.dumps(self.schedule_list)

    def add_schedule_from_json(self, schedule_json):
        """
        将前端请求的JSON记录到本地的一个List中
        """
        self.schedule_list.append(json.loads(schedule_json))

    def save_schedule_to_file(self, filename):
        """
        将该List实时保存到硬盘上
        """
        with open(filename, 'w') as f:
            json.dump(self.schedule_list, f)

    def load_schedule_from_file(self, filename):
        """
        打开时自动从硬盘载入List
        """
        with open(filename, 'r') as f:
            self.schedule_list = json.load(f)
