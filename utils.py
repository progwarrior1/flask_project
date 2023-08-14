import json


class Condidate():

    def __init__(self, path):
        self.path = path

    def load_from_file(self):
        file = open(self.path, 'r', encoding='utf-8')
        data = json.load(file)
        candidate = {}
        for i in data:
            candidate[i['id']] = i
        file.close()
        return candidate

    def work_w_x(self, x):
        file = open(self.path, 'r', encoding='utf-8')
        data = json.load(file)
        candidate = {}
        for i in data:
            candidate[i['id']] = i
        with_nedd = candidate[x]
        file.close()
        return with_nedd['picture'], with_nedd['name'], with_nedd['position'], with_nedd['skills']
