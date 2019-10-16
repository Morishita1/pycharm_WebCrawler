from pymongo import MongoClient
# MongoDB에 계정이 있거나 외부 IP인 경우
# DB_HOST = 'xxx.xx.xx.xxx:27017'
# DB_ID = 'root'
# DB_PW = 'pw'
# client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST))


class MongoDAO:
    def __init__(self, directory):
        # MongoDB 연결
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['test']  # MongoDB의 'test' DB생성
        self.collection = self.db.get_collection(directory)

    def mongo_write(self, data):
        self.collection.insert(data)

